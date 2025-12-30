#!/usr/bin/env python3
"""
Generate infographics using Gemini API (Imagen)

Fully automated workflow:
1. Read prompt.md and content.md
2. Generate N variants using Gemini API
3. Convert to WebP using todd-image-convert
4. Run /ig-evaluate
5. Return recommendation

Free tier: 500 images/day
"""

import os
import sys
import argparse
from pathlib import Path
import subprocess
import time

def setup_gemini():
    """Initialize Gemini API"""
    try:
        import google.generativeai as genai
    except ImportError:
        print("ERROR: google-generativeai not installed")
        print("Install with: pip install google-generativeai")
        sys.exit(1)

    # Get API key from environment
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("ERROR: GEMINI_API_KEY not set")
        print("Get your API key from: https://aistudio.google.com/apikey")
        print("Then: export GEMINI_API_KEY='your-key-here'")
        sys.exit(1)

    genai.configure(api_key=api_key)
    return genai

def read_file(path):
    """Read file content"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"ERROR: File not found: {path}")
        sys.exit(1)

def generate_images(genai, combined_prompt, output_dir, num_variants=3, base_name="infographic", batch=1):
    """Generate infographic variants using Gemini API"""
    # Calculate starting variant number based on batch
    start_num = (batch - 1) * num_variants + 1
    end_num = batch * num_variants

    print(f"\n🎨 Generating batch {batch} ({num_variants} variants: #{start_num}-#{end_num})...")

    # Use Gemini 2.5 Flash Image (best for infographics)
    model = genai.GenerativeModel('gemini-2.5-flash-image')

    generated_files = []

    for i in range(start_num, end_num + 1):
        variant_num = i - start_num + 1
        print(f"\n  [{variant_num}/{num_variants}] Generating variant {i}...")

        try:
            # Generate image
            response = model.generate_content([combined_prompt])

            # Save to file
            output_path = output_dir / f"{base_name}-{i}.png"

            # Extract image from response and save
            if hasattr(response, 'images') and response.images:
                response.images[0].save(str(output_path))
                generated_files.append(output_path)
                print(f"  ✅ Saved: {output_path.name}")
            else:
                print(f"  ❌ No image in response for variant {i}")

            # Rate limiting: small delay between requests (free tier: ~10 req/min)
            if i < end_num:
                time.sleep(6)  # 6 seconds = 10/min max

        except Exception as e:
            print(f"  ❌ Error generating variant {i}: {e}")
            continue

    return generated_files

def convert_to_webp(png_files):
    """Convert PNGs to WebP using todd-image-convert"""
    print(f"\n🔄 Converting {len(png_files)} files to WebP...")

    # Set environment variables for todd-image-convert
    env = os.environ.copy()
    env['PYTHONPATH'] = "/Users/ja/Documents/CodeProjects/todd-lab/.todd/lib/py/todd-media/image-converter:" + env.get('PYTHONPATH', '')
    env['DYLD_LIBRARY_PATH'] = "/opt/homebrew/opt/vips/lib:" + env.get('DYLD_LIBRARY_PATH', '')

    # Build command
    cmd = [
        'todd-image-convert',
        *[str(f) for f in png_files],
        '--resolution', '1080p',
        '--output-format', 'webp',
        '--no-replace'
    ]

    try:
        result = subprocess.run(cmd, env=env, capture_output=True, text=True, check=True)
        print("  ✅ Conversion complete")
        print(f"  {result.stdout.strip()}")

        # Return webp filenames
        return [f.with_suffix('.webp') for f in png_files]
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Conversion failed: {e}")
        print(f"  stdout: {e.stdout}")
        print(f"  stderr: {e.stderr}")
        return []

def run_evaluation(output_dir):
    """Run /ig-evaluate on generated webp files"""
    print(f"\n📊 Running evaluation...")

    # Note: This would ideally call the ig-evaluate skill
    # For now, provide instructions
    print(f"\n  Manual step required:")
    print(f"  Run: /ig-evaluate {output_dir}/*.webp")
    print(f"\n  Or in Claude Code:")
    print(f"  /ig-evaluate")
    print(f"  Then select the webp files when prompted")

    # TODO: Integrate with ig-evaluate skill when available as callable function

def main():
    parser = argparse.ArgumentParser(
        description="Generate infographics using Gemini API"
    )
    parser.add_argument(
        'directory',
        type=Path,
        help='Directory containing prompt.md and content.md'
    )
    parser.add_argument(
        '--variants',
        type=int,
        default=3,
        help='Number of variants to generate (default: 3)'
    )
    parser.add_argument(
        '--name',
        default='infographic',
        help='Base name for output files (default: infographic)'
    )
    parser.add_argument(
        '--batch',
        type=int,
        default=1,
        help='Batch number for iterative generation (default: 1)'
    )

    args = parser.parse_args()

    # Validate directory
    if not args.directory.exists():
        print(f"ERROR: Directory not found: {args.directory}")
        sys.exit(1)

    # Find prompt and content files
    prompt_file = args.directory / f"{args.directory.name}.prompt.md"
    content_file = args.directory / f"{args.directory.name}.content.md"

    # Fallback to generic names
    if not prompt_file.exists():
        prompt_file = args.directory / "prompt.md"
    if not content_file.exists():
        content_file = args.directory / "content.md"

    # Validate files exist
    if not prompt_file.exists():
        print(f"ERROR: Prompt file not found: {prompt_file}")
        print(f"Expected: {args.directory.name}.prompt.md or prompt.md")
        sys.exit(1)
    if not content_file.exists():
        print(f"ERROR: Content file not found: {content_file}")
        print(f"Expected: {args.directory.name}.content.md or content.md")
        sys.exit(1)

    print("=" * 60)
    print("🎨 GEMINI INFOGRAPHIC GENERATOR")
    print("=" * 60)
    print(f"\n📁 Directory: {args.directory}")
    print(f"📝 Prompt: {prompt_file.name}")
    print(f"📄 Content: {content_file.name}")
    print(f"🔢 Variants: {args.variants}")
    print(f"📦 Batch: {args.batch}")
    print(f"💰 Cost: FREE (using Gemini free tier - 500/day)")

    # Setup Gemini
    genai = setup_gemini()

    # Read files
    print(f"\n📖 Reading files...")
    prompt_content = read_file(prompt_file)
    content_data = read_file(content_file)

    # Combine prompt and content
    combined_prompt = f"{prompt_content}\n\n---\n\nCONTENT:\n\n{content_data}"

    print(f"  ✅ Prompt: {len(prompt_content)} chars")
    print(f"  ✅ Content: {len(content_data)} chars")
    print(f"  ✅ Combined: {len(combined_prompt)} chars")

    # Generate images
    png_files = generate_images(
        genai,
        combined_prompt,
        args.directory,
        args.variants,
        args.name,
        args.batch
    )

    if not png_files:
        print("\n❌ No images generated. Exiting.")
        sys.exit(1)

    print(f"\n✅ Generated {len(png_files)} PNG files")

    # Convert to WebP
    webp_files = convert_to_webp(png_files)

    if not webp_files:
        print("\n⚠️  Conversion failed, but PNG files are available")
    else:
        print(f"\n✅ Converted {len(webp_files)} WebP files")

    # Run evaluation
    run_evaluation(args.directory)

    print("\n" + "=" * 60)
    print("✅ GENERATION COMPLETE")
    print("=" * 60)
    print(f"\n📁 Output directory: {args.directory}")
    print(f"🖼️  PNG files: {len(png_files)}")
    print(f"🌐 WebP files: {len(webp_files)}")
    print(f"\n🎯 Next steps:")
    print(f"  1. Review generated images in: {args.directory}")
    print(f"  2. Run: /ig-evaluate {args.directory}/*.webp")
    print(f"  3. Select best variant based on evaluation")

if __name__ == '__main__':
    main()