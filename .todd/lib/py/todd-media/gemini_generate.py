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

def build_prompt(content, direction, aspect_ratio, variant_num, density='standard'):
    """Build combined prompt for Gemini with density tier injection"""

    density_instructions = {
        'concise': """
🚨 CRITICAL: CONCISE TIER - MAXIMUM SIMPLICITY ENFORCED 🚨

ABSOLUTE REQUIREMENTS:
- HEADLINES + 3-5 KEY STATISTICS ONLY (NO detailed breakdowns, NO sub-categories)
- 40%+ WHITE SPACE MANDATORY (maximum breathing room, generous margins)
- MINIMAL LABELS (just enough to understand - NO explanatory paragraphs)
- 15-30 SECOND GLANCE COMPREHENSION (not deep study)
- "At-a-glance" understanding is THE GOAL

STRICTLY FORBIDDEN:
❌ NO explanatory text blocks or annotations
❌ NO detailed component breakdowns
❌ NO sub-categories or nested information
❌ NO paragraph-length descriptions
❌ NO more than 5 key data points visible

EXAMPLE ACCEPTABLE DENSITY:
✅ Title: "71% Skills Gap"
✅ 3-5 headline stats: "3/100 programs", "71% lack skills", "42% zero ROI"
✅ Simple visual metaphor (cycle diagram, comparison arrows)
✅ Generous white space (40%+)

This is CONCISE media - quick social sharing, NOT educational deep-dive.
""",
        'standard': """
🎯 INFORMATION DENSITY: STANDARD TIER (DEFAULT)
- Key breakdowns with 3-4 components each
- 30-60 second comprehension time
- 30% white space target
- Brief labels/descriptions (category name + value, NO paragraphs)
- Stacked bars/charts show components with dollar amounts
- Readable without requiring close study
- "Quick comprehension with enough detail to be useful"
- Perfect for: Conference presentations, blog posts, reports, general publication
""",
        'detailed': """
🎯 INFORMATION DENSITY: DETAILED TIER
- Comprehensive annotations and explanatory text
- 2-3 minute close reading required
- 25%+ white space acceptable (information-dense)
- Each component has 2-3 sentences of explanation
- Year-by-year progressions, detailed timelines, case study callouts
- Multiple detail layers (overview → drill-down capability)
- "Rewards close study, provides deep understanding"
- Perfect for: Textbooks, MBA case studies, training materials, analyst reports
"""
    }

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

    # Extract title from direction (first line starting with #)
    title = ""
    for line in direction.split('\n'):
        if line.strip().startswith('#'):
            title = line.strip().lstrip('#').strip()
            break

    prompt = f"""{title}

Create an infographic with the following specifications:

{direction}

---

{density_instructions.get(density, density_instructions['standard'])}

---

CONTENT:

{content}

---

VARIANT #{variant_num}: Generate a unique visual approach for this variant.

---

{aspect_instructions.get(aspect_ratio, aspect_instructions['landscape'])}
"""
    return prompt

async def generate_in_tab(page, content, direction, aspect_ratio, variant_num, output_dir, base_name, density='standard'):
    """Generate a single infographic in a tab (generation only, download separately)"""
    try:
        # Capture starting URL (base Gemini URL before generation)
        starting_url = page.url
        print(f"   [{variant_num}] 🔗 Starting URL: {starting_url}")

        # Build prompt
        prompt_text = build_prompt(content, direction, aspect_ratio, variant_num, density)
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

        # Wait for URL change (indicates new conversation created)
        print(f"   [{variant_num}] 🔍 Waiting for conversation URL...")
        url_change_start = time.time()
        conversation_url = starting_url

        # Poll for URL change for up to 10 seconds
        while time.time() - url_change_start < 10:
            await asyncio.sleep(0.5)
            current_url = page.url
            if current_url != starting_url:
                conversation_url = current_url
                elapsed = time.time() - url_change_start
                print(f"   [{variant_num}] 🔗 Conversation URL: {conversation_url} ({elapsed:.1f}s)")
                break

        if conversation_url == starting_url:
            print(f"   [{variant_num}] ⚠️  URL unchanged after 10s (may reuse cached conversation)")

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

        # Return the page and conversation URL for later download
        return (variant_num, page, conversation_url)

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

async def generate_infographics(content, direction, num_variants, aspect_ratio, output_dir, base_name, start_num, chrome_profile="Default", density='standard'):
    """Generate infographics using sequential submission for unique URLs, then parallel generation"""

    print("=" * 60)
    print("🎨 GEMINI INFOGRAPHIC GENERATOR (Nano Banana)")
    print("=" * 60)
    print(f"\n📁 Output: {output_dir}")
    print(f"🖼️  Name: {base_name}")
    print(f"🔢 Variants: {num_variants} (#{start_num}-{start_num + num_variants - 1})")
    print(f"📐 Aspect: {aspect_ratio}")
    print(f"👤 Profile: {chrome_profile}")
    print(f"🎯 Density: {density}")
    print(f"🚀 Mode: Sequential submission → Parallel generation")

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
            channel="chrome",
            args=["--isolated"]
        )

        # SEQUENTIAL SUBMISSION: Submit each variant one at a time to ensure unique URLs
        print(f"\n🔄 Submitting {num_variants} variants sequentially (ensures unique conversations)...")
        submitted_tabs = []  # [(variant_num, page, conversation_url), ...]

        for i in range(num_variants):
            variant_num = start_num + i

            # Create NEW tab
            print(f"\n   [{variant_num}] 📑 Opening new tab...")
            page = await context.new_page()
            await page.goto('https://gemini.google.com/')

            # Wait for input to load
            load_start = time.time()
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

            # Enable image generation mode
            print(f"   [{variant_num}] 🖼️  Enabling image mode...")
            try:
                tools_button = page.get_by_role("button", name="Tools").first
                await tools_button.click()
                await asyncio.sleep(1)

                create_images_button = page.get_by_role("button", name="Create images").first
                await create_images_button.click()
                await asyncio.sleep(1)

                await page.wait_for_selector('button:has-text("Deselect Image")', timeout=5000)
                print(f"   [{variant_num}] ✅ Image mode enabled")
            except Exception as e:
                print(f"   [{variant_num}] ⚠️  Image mode activation failed: {e}")
                print(f"   [{variant_num}] 🔄 Continuing anyway (may already be in image mode)")

            # Build and submit prompt
            starting_url = page.url
            prompt_text = build_prompt(content, direction, aspect_ratio, variant_num, density)
            print(f"   [{variant_num}] 📝 Submitting prompt ({len(prompt_text)} chars)...")

            textbox = page.locator('.ql-editor').first
            await textbox.click()
            await textbox.fill(prompt_text)
            await asyncio.sleep(0.5)
            await textbox.press('Enter')

            # CRITICAL: Wait for URL to change (indicates new conversation created)
            print(f"   [{variant_num}] ⏳ Waiting for conversation URL...")
            url_change_start = time.time()
            conversation_url = starting_url

            while time.time() - url_change_start < 15:  # Wait up to 15s for URL change
                await asyncio.sleep(0.5)
                current_url = page.url
                if current_url != starting_url:
                    conversation_url = current_url
                    elapsed = time.time() - url_change_start
                    print(f"   [{variant_num}] ✅ Conversation URL: {conversation_url} ({elapsed:.1f}s)")
                    break

            if conversation_url == starting_url:
                print(f"   [{variant_num}] ⚠️  URL unchanged after 15s - may not have created new conversation!")

            # Record this tab for parallel generation monitoring
            submitted_tabs.append((variant_num, page, conversation_url))
            print(f"   [{variant_num}] ✅ Submitted - now generating in parallel...")

        # NOW: All variants are submitted with unique URLs, generating in parallel
        print(f"\n⏱️  All {num_variants} variants submitted - now monitoring parallel generation...")
        gen_start = time.time()

        # Monitor all tabs for generation completion (wait for download button)
        successful = []
        conversation_urls = {}

        for variant_num, page, conv_url in submitted_tabs:
            print(f"\n   [{variant_num}] ⏳ Waiting for generation to complete...")
            wait_start = time.time()

            download_button_found = False
            while time.time() - wait_start < 180:  # 180s max (3 minutes)
                try:
                    await page.wait_for_selector('[data-test-id="download-generated-image-button"]', timeout=60000)
                    download_button_found = True
                    gen_time = time.time() - wait_start
                    print(f"   [{variant_num}] ✅ Generated in {gen_time:.1f}s")
                    break
                except:
                    await asyncio.sleep(60)  # Poll every 60s

            if download_button_found:
                successful.append((variant_num, page))
                conversation_urls[variant_num] = conv_url
            else:
                print(f"   [{variant_num}] ❌ Timeout (180s)")

        if not successful:
            print("\n❌ No images generated successfully")
            await context.close()
            return []

        gen_time = time.time() - gen_start
        print(f"\n⏱️  Generation time: {gen_time:.1f}s")

        # Detect duplicate conversation URLs (indicates cached/reused generations)
        print(f"\n🔍 Checking for duplicate conversation URLs...")
        url_to_variants = {}  # conversation_url -> [variant_nums]
        for variant_num, conv_url in conversation_urls.items():
            if conv_url not in url_to_variants:
                url_to_variants[conv_url] = []
            url_to_variants[conv_url].append(variant_num)

        duplicates_found = False
        for conv_url, variant_nums in url_to_variants.items():
            if len(variant_nums) > 1:
                duplicates_found = True
                print(f"  ⚠️  DUPLICATE: Variants {variant_nums} share URL: {conv_url}")
                print(f"      → These variants likely generated IDENTICAL images (cached)")
            else:
                print(f"  ✅ Variant {variant_nums[0]}: Unique URL")

        if duplicates_found:
            print(f"\n⚠️  WARNING: Duplicate conversation URLs detected!")
            print(f"  Some variants likely produced identical images due to caching.")
            print(f"  Consider regenerating affected variants or using different prompts.")

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

def analyze_prompt_complexity(prompt_text, density_tier='standard'):
    """
    Analyze prompt complexity and check against density tier expectations.

    Returns: dict with metrics and warnings
    """
    import re

    # Count metrics
    char_count = len(prompt_text)
    sections = len(re.findall(r'^##\s+', prompt_text, re.MULTILINE))
    bullets = len(re.findall(r'^\s*[-•]\s+', prompt_text, re.MULTILINE))
    critical_flags = len(re.findall(r'🚨|CRITICAL', prompt_text, re.IGNORECASE))
    avoid_items = len(re.findall(r'^\s*[-•]\s*❌', prompt_text, re.MULTILINE))

    # Expected ranges per tier
    tier_expectations = {
        'concise': {
            'char_range': (2000, 3000),
            'sections_range': (3, 4),
            'bullets_range': (8, 12),
            'critical_range': (0, 1),
            'avoid_range': (0, 3)
        },
        'standard': {
            'char_range': (4000, 6000),
            'sections_range': (4, 6),
            'bullets_range': (15, 25),
            'critical_range': (1, 2),
            'avoid_range': (5, 7)
        },
        'detailed': {
            'char_range': (7000, 10000),
            'sections_range': (6, 10),
            'bullets_range': (30, 50),
            'critical_range': (2, 4),
            'avoid_range': (10, 15)
        }
    }

    expected = tier_expectations.get(density_tier, tier_expectations['standard'])

    # Check for mismatches
    warnings = []
    char_min, char_max = expected['char_range']
    if char_count < char_min:
        warnings.append(f"⚠️  Prompt too sparse: {char_count} chars (expected {char_min}-{char_max} for {density_tier})")
    elif char_count > char_max:
        warnings.append(f"⚠️  Prompt too verbose: {char_count} chars (expected {char_min}-{char_max} for {density_tier})")

    sec_min, sec_max = expected['sections_range']
    if sections < sec_min or sections > sec_max:
        warnings.append(f"⚠️  Section count mismatch: {sections} sections (expected {sec_min}-{sec_max} for {density_tier})")

    bul_min, bul_max = expected['bullets_range']
    if bullets < bul_min or bullets > bul_max:
        warnings.append(f"⚠️  Bullet count mismatch: {bullets} bullets (expected {bul_min}-{bul_max} for {density_tier})")

    crit_min, crit_max = expected['critical_range']
    if critical_flags > crit_max:
        warnings.append(f"⚠️  Too many CRITICAL flags: {critical_flags} (expected {crit_min}-{crit_max} for {density_tier})")

    avoid_min, avoid_max = expected['avoid_range']
    if avoid_items > avoid_max:
        warnings.append(f"⚠️  AVOID list too long: {avoid_items} items (expected {avoid_min}-{avoid_max} for {density_tier})")

    return {
        'char_count': char_count,
        'sections': sections,
        'bullets': bullets,
        'critical_flags': critical_flags,
        'avoid_items': avoid_items,
        'warnings': warnings,
        'tier': density_tier,
        'tier_match': len(warnings) == 0
    }

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
    parser.add_argument('--density', choices=['concise', 'standard', 'detailed'], default='standard', help='Information density tier (default: standard)')
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

    # Analyze prompt complexity
    analysis = analyze_prompt_complexity(direction, args.density)
    print(f"\n📊 Prompt Complexity Analysis ({args.density} tier):")
    print(f"  Characters: {analysis['char_count']}")
    print(f"  Sections: {analysis['sections']}")
    print(f"  Bullets: {analysis['bullets']}")
    print(f"  CRITICAL flags: {analysis['critical_flags']}")
    print(f"  AVOID items: {analysis['avoid_items']}")

    if analysis['warnings']:
        print(f"\n⚠️  Complexity Warnings ({len(analysis['warnings'])}):")
        for warning in analysis['warnings']:
            print(f"  {warning}")
        print(f"\n💡 Tip: Simplify prompt to match {args.density} tier expectations")
        print(f"    See: .claude/commands/ig-generate.md (Tier-Specific Prompt Generation Guidelines)")
    else:
        print(f"  ✅ Prompt matches {args.density} tier expectations")

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
        chrome_profile=args.chrome_profile,
        density=args.density
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
