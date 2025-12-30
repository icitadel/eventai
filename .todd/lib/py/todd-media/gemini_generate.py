#!/usr/bin/env python3
"""
Gemini Infographic Generator (Nano Banana Workflow Automation)

Automates gemini.google.com infographic generation using Playwright with parallel tabs.

Usage:
    gemini-generate --content file.md --prompt style.md --output-dir ./visuals --name barriers
    gemini-generate --content "Data here" --prompt "Style instructions" --variants 5
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
    path = Path(input_str)
    if path.exists() and path.is_file():
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return input_str

def build_prompt(content, direction, aspect_ratio, variant_num):
    """Build combined prompt for Gemini"""
    aspect_instructions = {
        'landscape': """
🚨 CRITICAL FINAL REQUIREMENT - LANDSCAPE ORIENTATION 🚨
WIDTH MUST BE GREATER THAN HEIGHT (e.g., 2752 x 1536)
LANDSCAPE = WIDER THAN TALL = HORIZONTAL
IGNORE ANY PREVIOUS ASPECT RATIO MENTIONS
THIS IS THE ABSOLUTE FINAL ASPECT RATIO REQUIREMENT
""",
        'portrait': """
ASPECT RATIO REQUIREMENT: PORTRAIT (taller than wide, approximately 9:16)
Dimensions should be approximately 1792 x 2400 or similar portrait proportions.
""",
        'square': """
ASPECT RATIO REQUIREMENT: SQUARE (1:1, equal width and height)
Dimensions should be approximately 2048 x 2048.
"""
    }

    prompt = f"""Create an infographic with the following specifications:

{direction}

---

CONTENT:

{content}

---

VARIANT #{variant_num}: Generate a unique visual approach for this variant.

---

{aspect_instructions.get(aspect_ratio, aspect_instructions['landscape'])}
"""
    return prompt

async def generate_in_tab(page, content, direction, aspect_ratio, variant_num, output_dir, base_name):
    """Generate a single infographic in a tab (generation only, download separately)"""
    try:
        # Build prompt
        prompt_text = build_prompt(content, direction, aspect_ratio, variant_num)
        print(f"   [{variant_num}] 📝 Prompt: {len(prompt_text)} chars")

        # Fill input (.ql-editor is most reliable)
        print(f"   [{variant_num}] ⌨️  Filling...")
        textbox = page.locator('.ql-editor').first
        await textbox.click()
        await textbox.fill(prompt_text)
        await asyncio.sleep(0.5)  # Brief pause
        print(f"   [{variant_num}] ✅ Filled")

        # Submit
        print(f"   [{variant_num}] ⏳ Submitting...")
        await textbox.press('Enter')

        # Wait for image generation (10-15s typical, 180s max for complex infographics)
        print(f"   [{variant_num}] 🖼️  Generating...")
        gen_start = time.time()

        download_button_found = False
        while time.time() - gen_start < 180:  # 180s max for generation (3 minutes)
            try:
                await page.wait_for_selector('[data-test-id="download-generated-image-button"]', timeout=60000)
                download_button_found = True
                gen_time = time.time() - gen_start
                print(f"   [{variant_num}] ✅ Generated in {gen_time:.1f}s")
                break
            except:
                await asyncio.sleep(60)  # Poll every 60s (1 minute)

        if not download_button_found:
            print(f"   [{variant_num}] ❌ Timeout (180s)")
            return None

        # Return the page for later download
        return (variant_num, page)

    except Exception as e:
        print(f"   [{variant_num}] ❌ Error: {e}")
        return None

async def download_from_tab(variant_num, page, output_dir, base_name):
    """Download generated image from a tab with verification"""
    try:
        print(f"   [{variant_num}] ⬇️  Downloading...")
        download_start = time.time()

        # Wait for button to be clickable
        download_button = page.locator('[data-test-id="download-generated-image-button"]').first
        await download_button.wait_for(state='visible', timeout=5000)
        print(f"   [{variant_num}] 📍 Button visible, clicking...")

        # Click and wait for download with longer timeout (90s)
        async with page.expect_download(timeout=90000) as download_info:
            await download_button.click()
            print(f"   [{variant_num}] 🖱️  Clicked download button")

        download = await download_info.value
        download_time = time.time() - download_start
        print(f"   [{variant_num}] ✅ Downloaded in {download_time:.1f}s")

        # Save and verify
        output_path = output_dir / f"{base_name}-{variant_num}.png"
        await download.save_as(str(output_path))

        # CRITICAL FIX: Poll continuously for 2 minutes until file exists
        verify_start = time.time()
        verify_timeout = 120  # 2 minutes
        poll_interval = 2  # Check every 2 seconds

        while time.time() - verify_start < verify_timeout:
            if output_path.exists() and output_path.stat().st_size > 0:
                elapsed = time.time() - verify_start
                print(f"   [{variant_num}] 💾 Verified: {output_path.name} ({output_path.stat().st_size / 1024 / 1024:.1f}MB) after {elapsed:.1f}s")
                return output_path
            else:
                elapsed = time.time() - verify_start
                print(f"   [{variant_num}] ⏳ Waiting for file write... ({elapsed:.1f}s / {verify_timeout}s)")
                await asyncio.sleep(poll_interval)

        # If we get here, timeout occurred
        print(f"   [{variant_num}] ❌ File verification timeout after {verify_timeout}s")
        print(f"   [{variant_num}] ❌ Expected: {output_path}")
        print(f"   [{variant_num}] ❌ Exists: {output_path.exists()}")
        if output_path.exists():
            print(f"   [{variant_num}] ❌ Size: {output_path.stat().st_size} bytes")
        return None

    except Exception as e:
        print(f"   [{variant_num}] ❌ Download error: {e}")
        return None

async def generate_infographics(content, direction, num_variants, aspect_ratio, output_dir, base_name, start_num, chrome_profile="Default"):
    """Generate infographics using parallel tabs"""

    print("=" * 60)
    print("🎨 GEMINI INFOGRAPHIC GENERATOR (Nano Banana)")
    print("=" * 60)
    print(f"\n📁 Output: {output_dir}")
    print(f"🖼️  Name: {base_name}")
    print(f"🔢 Variants: {num_variants} (#{start_num}-{start_num + num_variants - 1})")
    print(f"📐 Aspect: {aspect_ratio}")
    print(f"👤 Profile: {chrome_profile}")
    print(f"🚀 Mode: {num_variants} parallel tabs")

    playwright = await setup_playwright()

    # Chrome user data directory
    import os
    chrome_user_data = os.path.expanduser(f"~/Library/Application Support/Google/Chrome")
    profile_dir = os.path.join(chrome_user_data, chrome_profile)

    async with playwright as p:
        # Launch browser
        print(f"\n🌐 Launching Chrome...")
        context = await p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=False,
            channel="chrome"
        )

        # Create tabs for each variant
        print(f"\n📑 Creating {num_variants} tabs...")
        tabs = []
        for i in range(num_variants):
            page = await context.new_page()
            await page.goto('https://gemini.google.com/app')
            tabs.append(page)

        # Wait for all tabs to load
        print("⏸️  Waiting for tabs to load...")
        for i, page in enumerate(tabs):
            variant_num = start_num + i
            load_start = time.time()

            # Smart wait for input
            found = False
            while time.time() - load_start < 30:
                try:
                    await page.wait_for_selector('.ql-editor', timeout=2000)
                    found = True
                    elapsed = time.time() - load_start
                    print(f"   [{variant_num}] ✅ Loaded in {elapsed:.1f}s")
                    break
                except:
                    await asyncio.sleep(2)

            if not found:
                print(f"   [{variant_num}] ❌ Load timeout")
                await context.close()
                return []

        # Enable image generation mode on all tabs
        print("\n🖼️  Enabling image generation mode...")
        for i, page in enumerate(tabs):
            variant_num = start_num + i
            try:
                # CRITICAL FIX: Use .first to get the first Tools button in THIS page context
                # (avoids strict mode violation from multiple tabs/conversations)
                tools_button = page.get_by_role("button", name="Tools").first
                await tools_button.click()
                await asyncio.sleep(1)

                # Click Create images button (also use .first for safety)
                create_images_button = page.get_by_role("button", name="Create images").first
                await create_images_button.click()
                await asyncio.sleep(1)

                # Verify image mode is active - look for the deselect button
                await page.wait_for_selector('button:has-text("Deselect Image")', timeout=5000)
                print(f"   [{variant_num}] ✅ Image mode enabled")
            except Exception as e:
                print(f"   [{variant_num}] ⚠️  Image mode activation failed: {e}")
                print(f"   [{variant_num}] 🔄 Attempting to continue anyway (may already be in image mode)")
                # Continue anyway - might already be in image mode

        # Generate all variants in parallel
        print(f"\n🎨 Generating {num_variants} variants in parallel...")
        gen_start = time.time()

        tasks = []
        for i, page in enumerate(tabs):
            variant_num = start_num + i
            task = generate_in_tab(page, content, direction, aspect_ratio, variant_num, output_dir, base_name)
            tasks.append(task)

        # Wait for all generations to complete
        gen_results = await asyncio.gather(*tasks)
        gen_time = time.time() - gen_start
        print(f"\n⏱️  Generation time: {gen_time:.1f}s")

        # Filter successful generations
        successful = [(num, pg) for result in gen_results if result is not None for num, pg in [result]]

        if not successful:
            print("\n❌ No images generated successfully")
            await context.close()
            return []

        # Download sequentially (avoid Chrome simultaneous download limit)
        print(f"\n⬇️  Downloading {len(successful)} images sequentially...")
        download_start = time.time()

        generated_files = []
        for variant_num, page in successful:
            output_path = await download_from_tab(variant_num, page, output_dir, base_name)
            if output_path:
                generated_files.append(output_path)

        download_time = time.time() - download_start
        print(f"\n⏱️  Download time: {download_time:.1f}s")
        print(f"⏱️  Total time: {gen_time + download_time:.1f}s")

        # SAFETY: Final verification that all files exist
        print(f"\n🔍 Final verification of {len(generated_files)} files...")
        verified_files = []
        for f in generated_files:
            if f.exists() and f.stat().st_size > 0:
                print(f"  ✅ {f.name} ({f.stat().st_size / 1024 / 1024:.1f}MB)")
                verified_files.append(f)
            else:
                print(f"  ❌ {f.name} - File missing or empty!")

        # Extra safety delay before closing browser (ensure all file writes complete)
        if verified_files:
            print("\n⏸️  Waiting 2s for filesystem sync...")
            await asyncio.sleep(2)

        # Close browser
        print("\n🔒 Closing browser...")
        await context.close()

        return verified_files

def convert_to_webp(png_files, resolution='1080p'):
    """Convert PNGs to WebP using todd-image-convert"""
    if not png_files:
        return []

    print(f"\n🔄 Converting {len(png_files)} files to WebP ({resolution})...")

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
        return [f.with_suffix('.webp') for f in png_files]
    except subprocess.CalledProcessError as e:
        print(f"  ⚠️  Conversion failed: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(
        description="Generate infographics using Gemini with parallel tabs",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('--content', required=True, help='Content file or text')
    parser.add_argument('--prompt', required=True, help='Prompt file or text')
    parser.add_argument('--output-dir', type=Path, default=Path.cwd(), help='Output directory')
    parser.add_argument('--name', default='infographic', help='Base filename')
    parser.add_argument('--variants', type=int, default=3, help='Number of variants (1-5)')
    parser.add_argument('--aspect-ratio', choices=['landscape', 'portrait', 'square'], default='landscape', help='Aspect ratio')
    parser.add_argument('--batch', type=int, default=1, help='Batch number')
    parser.add_argument('--skip-webp', action='store_true', help='Skip WebP conversion')
    parser.add_argument('--resolution', default='1080p', help='WebP resolution')
    parser.add_argument('--chrome-profile', default='Default', help='Chrome profile')

    args = parser.parse_args()

    if args.variants < 1 or args.variants > 5:
        print("ERROR: Variants must be 1-5")
        sys.exit(1)

    args.output_dir.mkdir(parents=True, exist_ok=True)

    # Read content and prompt
    print("📖 Reading content and prompt...")
    content = read_file_or_text(args.content)
    direction = read_file_or_text(args.prompt)
    print(f"  ✅ Content: {len(content)} chars")
    print(f"  ✅ Prompt: {len(direction)} chars")

    # Calculate starting variant number
    start_num = (args.batch - 1) * args.variants + 1

    # Generate
    png_files = asyncio.run(generate_infographics(
        content=content,
        direction=direction,
        num_variants=args.variants,
        aspect_ratio=args.aspect_ratio,
        output_dir=args.output_dir,
        base_name=args.name,
        start_num=start_num,
        chrome_profile=args.chrome_profile
    ))

    if not png_files:
        print("\n❌ No images generated")
        sys.exit(1)

    print(f"\n✅ Generated {len(png_files)} PNG files:")
    for f in png_files:
        print(f"  - {f.name}")

    # Convert to WebP
    webp_files = []
    if not args.skip_webp:
        webp_files = convert_to_webp(png_files, args.resolution)
        if webp_files:
            print(f"\n✅ Converted {len(webp_files)} WebP files:")
            for f in webp_files:
                print(f"  - {f.name}")

    # Summary
    print("\n" + "=" * 60)
    print("✅ GENERATION COMPLETE")
    print("=" * 60)
    print(f"\n📁 Output: {args.output_dir}")
    print(f"🖼️  PNG: {len(png_files)}")
    print(f"🌐 WebP: {len(webp_files)}")
    print(f"\n🎯 Next: /ig-evaluate {args.output_dir}/*.webp")

if __name__ == '__main__':
    main()
