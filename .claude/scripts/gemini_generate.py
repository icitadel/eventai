#!/usr/bin/env python3
"""
Gemini Infographic Generator (Nano Banana Workflow Automation)

Automates gemini.google.com infographic generation using Playwright.

Usage:
    gemini-generate --content file.md --prompt style.md --output-dir ./visuals --name barriers
    gemini-generate --content "Data here" --prompt "Style instructions" --variants 5 --aspect-ratio portrait
"""

import argparse
import asyncio
import sys
from pathlib import Path
import subprocess
import time

async def setup_playwright():
    """Initialize Playwright with browser automation"""
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("ERROR: Playwright not installed")
        print("Install with: pip install playwright")
        print("Then run: playwright install")
        sys.exit(1)

    return async_playwright()

def read_file_or_text(input_str):
    """Read content from file path or return as text"""
    # Check if it's a file path
    path = Path(input_str)
    if path.exists() and path.is_file():
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        # Treat as direct text content
        return input_str

def build_prompt(content, direction, aspect_ratio, variant_num):
    """Build combined prompt for Gemini"""

    # Aspect ratio instructions
    aspect_instructions = {
        'landscape': """
CRITICAL: LANDSCAPE ASPECT RATIO (16:9 or similar, wider than tall)
Dimensions should be approximately 2752 x 1536 or similar landscape proportions.
AVOID: PORTRAIT orientation (taller than wide)
""",
        'portrait': """
ASPECT RATIO: PORTRAIT (taller than wide, approximately 9:16)
Dimensions should be approximately 1792 x 2400 or similar portrait proportions.
""",
        'square': """
ASPECT RATIO: SQUARE (1:1, equal width and height)
Dimensions should be approximately 2048 x 2048.
"""
    }

    prompt = f"""Create an infographic with the following specifications:

{aspect_instructions.get(aspect_ratio, aspect_instructions['landscape'])}

{direction}

---

CONTENT:

{content}

---

VARIANT #{variant_num}: Generate a unique visual approach for this variant.
"""

    return prompt

async def generate_infographics(content, direction, num_variants, aspect_ratio, output_dir, base_name, start_num):
    """Generate infographics using Gemini chat interface"""

    print("=" * 60)
    print("🎨 GEMINI INFOGRAPHIC GENERATOR (Nano Banana)")
    print("=" * 60)
    print(f"\n📁 Output directory: {output_dir}")
    print(f"🖼️  Base name: {base_name}")
    print(f"🔢 Variants: {num_variants} (starting from #{start_num})")
    print(f"📐 Aspect ratio: {aspect_ratio}")

    playwright = await setup_playwright()

    async with playwright as p:
        # Launch browser
        print("\n🌐 Launching browser...")
        browser = await p.chromium.launch(headless=False)  # headless=False so user can see
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to Gemini
        print("🔗 Navigating to gemini.google.com...")
        await page.goto('https://gemini.google.com/app')

        # Wait for user to sign in if needed
        print("\n⏸️  Checking sign-in status...")
        try:
            # Check if already signed in by looking for prompt input
            await page.wait_for_selector('[data-test-id="input-area"]', timeout=5000)
            print("✅ Already signed in!")
        except:
            print("⚠️  Not signed in. Please sign in to Gemini...")
            print("   Press ENTER when you're signed in and ready to continue...")
            input()
            # Wait for prompt input to appear after sign-in
            await page.wait_for_selector('[data-test-id="input-area"]', timeout=30000)
            print("✅ Sign-in detected!")

        generated_files = []

        # Generate each variant
        for i in range(start_num, start_num + num_variants):
            variant_num = i - start_num + 1
            print(f"\n🎨 Generating variant {i} ({variant_num}/{num_variants})...")

            # Build prompt
            prompt_text = build_prompt(content, direction, aspect_ratio, i)

            print(f"   📝 Prompt length: {len(prompt_text)} chars")

            # Find and fill the textbox
            textbox = page.get_by_test_id('text-input')
            await textbox.fill(prompt_text)

            # Submit
            print("   ⏳ Submitting prompt...")
            await textbox.press('Enter')

            # Wait for image generation (look for download button)
            print("   🖼️  Waiting for image generation...")
            try:
                await page.wait_for_selector('[data-test-id="download-generated-image-button"]', timeout=120000)  # 2 min max
                print("   ✅ Image generated!")
            except:
                print(f"   ❌ Timeout waiting for image {i}")
                continue

            # Download the image
            print("   ⬇️  Downloading image...")
            async with page.expect_download() as download_info:
                await page.locator('[data-test-id="download-generated-image-button"]').click()
            download = await download_info.value

            # Save to output directory with proper naming
            output_path = output_dir / f"{base_name}-{i}.png"
            await download.save_as(str(output_path))
            generated_files.append(output_path)
            print(f"   ✅ Saved: {output_path.name}")

            # Small delay between requests to avoid rate limiting
            if variant_num < num_variants:
                print("   ⏸️  Pausing 3 seconds before next variant...")
                await asyncio.sleep(3)

        # Close browser
        print("\n🔒 Closing browser...")
        await browser.close()

        return generated_files

def convert_to_webp(png_files, resolution='1080p'):
    """Convert PNGs to WebP using todd-image-convert"""
    if not png_files:
        return []

    print(f"\n🔄 Converting {len(png_files)} files to WebP ({resolution})...")

    # Build command
    cmd = [
        'todd-image-convert',
        *[str(f) for f in png_files],
        '--resolution', resolution,
        '--output-format', 'webp',
        '--no-replace'
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("  ✅ Conversion complete")

        # Return webp filenames
        return [f.with_suffix('.webp') for f in png_files]
    except subprocess.CalledProcessError as e:
        print(f"  ⚠️  Conversion failed: {e}")
        print(f"  stdout: {e.stdout}")
        print(f"  stderr: {e.stderr}")
        return []

def main():
    parser = argparse.ArgumentParser(
        description="Generate infographics using Gemini (gemini.google.com) with Playwright automation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate 3 landscape infographics from files
  gemini-generate --content data.md --prompt style.md --output-dir ./visuals --name barriers

  # Generate 5 portrait variants with direct text
  gemini-generate --content "Your data here" --prompt "Style guide" --variants 5 --aspect-ratio portrait

  # Generate batch 2 (variants 4-6) for iteration
  gemini-generate --content data.md --prompt style.md --batch 2 --name barriers
        """
    )

    parser.add_argument(
        '--content',
        required=True,
        help='Content/data (file path or direct text)'
    )
    parser.add_argument(
        '--prompt',
        required=True,
        help='Style/direction prompt (file path or direct text)'
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path.cwd(),
        help='Output directory (default: current directory)'
    )
    parser.add_argument(
        '--name',
        default='infographic',
        help='Base name for output files (default: infographic)'
    )
    parser.add_argument(
        '--variants',
        type=int,
        default=3,
        help='Number of variants to generate (1-5, default: 3)'
    )
    parser.add_argument(
        '--aspect-ratio',
        choices=['landscape', 'portrait', 'square'],
        default='landscape',
        help='Aspect ratio for infographics (default: landscape)'
    )
    parser.add_argument(
        '--batch',
        type=int,
        default=1,
        help='Batch number for iterative generation (default: 1)'
    )
    parser.add_argument(
        '--skip-webp',
        action='store_true',
        help='Skip WebP conversion (only generate PNGs)'
    )
    parser.add_argument(
        '--resolution',
        default='1080p',
        help='Resolution for WebP conversion (default: 1080p)'
    )

    args = parser.parse_args()

    # Validate variants
    if args.variants < 1 or args.variants > 5:
        print("ERROR: Variants must be between 1 and 5")
        sys.exit(1)

    # Create output directory if needed
    args.output_dir.mkdir(parents=True, exist_ok=True)

    # Read content and prompt
    print("📖 Reading content and prompt...")
    content = read_file_or_text(args.content)
    direction = read_file_or_text(args.prompt)

    print(f"  ✅ Content: {len(content)} chars")
    print(f"  ✅ Prompt: {len(direction)} chars")

    # Calculate starting variant number based on batch
    start_num = (args.batch - 1) * args.variants + 1

    # Generate infographics
    png_files = asyncio.run(generate_infographics(
        content=content,
        direction=direction,
        num_variants=args.variants,
        aspect_ratio=args.aspect_ratio,
        output_dir=args.output_dir,
        base_name=args.name,
        start_num=start_num
    ))

    if not png_files:
        print("\n❌ No images generated. Exiting.")
        sys.exit(1)

    print(f"\n✅ Generated {len(png_files)} PNG files:")
    for f in png_files:
        print(f"  - {f.name}")

    # Convert to WebP
    webp_files = []
    if not args.skip_webp:
        webp_files = convert_to_webp(png_files, args.resolution)
        if webp_files:
            print(f"\n✅ Converted to {len(webp_files)} WebP files:")
            for f in webp_files:
                print(f"  - {f.name}")

    # Summary
    print("\n" + "=" * 60)
    print("✅ GENERATION COMPLETE")
    print("=" * 60)
    print(f"\n📁 Output directory: {args.output_dir}")
    print(f"🖼️  PNG files: {len(png_files)}")
    print(f"🌐 WebP files: {len(webp_files)}")
    print(f"\n🎯 Next steps:")
    print(f"  1. Review generated images in: {args.output_dir}")
    if webp_files:
        print(f"  2. Run: /ig-evaluate {args.output_dir}/*.webp")
    print(f"  3. Select best variant based on evaluation")

if __name__ == '__main__':
    main()