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

def get_next_variant_number(output_dir, base_name):
    """
    Scan output directory for existing variants and return the next available number.

    Looks for files matching {base_name}-{number}.png or {base_name}-{number}.webp,
    extracts the numbers, finds the maximum, and returns max + 1.

    Args:
        output_dir: Path to output directory
        base_name: Base filename (e.g., 'consent-spectrum')

    Returns:
        int: Next available variant number (starting from 1 if no variants exist)

    Examples:
        >>> # If folder has: consent-spectrum-1.png, consent-spectrum-3.png, consent-spectrum-7.webp
        >>> get_next_variant_number(Path('.'), 'consent-spectrum')
        8  # Returns max(1, 3, 7) + 1
    """
    import re

    output_path = Path(output_dir)
    if not output_path.exists():
        return 1

    # Pattern to match: {base_name}-{number}.{ext}
    pattern = re.compile(rf'^{re.escape(base_name)}-(\d+)\.(png|webp)$')

    existing_numbers = []
    for file in output_path.iterdir():
        if file.is_file():
            match = pattern.match(file.name)
            if match:
                existing_numbers.append(int(match.group(1)))

    if not existing_numbers:
        return 1

    return max(existing_numbers) + 1

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

def categorize_section(heading_text, heading_level):
    """
    Categorize a section heading as content or meta.
    
    Rules:
    - # H1 (title) → ALWAYS exclude
    - ## Style → ALWAYS exclude
    - ## Structure → ALWAYS exclude
    - Everything else → Include as content (default)
    
    Args:
        heading_text: The heading text (e.g., "Data Points", "Style")
        heading_level: 1 for #, 2 for ##, etc.
    
    Returns:
        'title', 'content', or 'meta'
    """
    heading_stripped = heading_text.strip()
    heading_lower = heading_stripped.lower()
    
    # H1 title - always exclude
    if heading_level == 1:
        return 'title'
    
    # Explicit meta sections (always exclude)
    if heading_lower in ['style', 'structure']:
        return 'meta'
    
    # Default: treat as content
    return 'content'

def analyze_prompt_structure(prompt_text):
    """
    Extract structural metrics from Markdown prompt: concepts and hierarchy depth.
    
    IMPORTANT: Only counts concepts from CONTENT sections (excludes title, Style, Structure).
    
    Concepts = content sections + top-level bullets in content sections
    Depth = max(heading depth, list nesting depth)
    
    Returns: dict with concepts, depth, complexity, section breakdown, and details
    """
    import re
    
    # Parse document structure
    lines = prompt_text.split('\n')
    
    # Track current section and its category
    current_section = None
    current_section_type = None
    
    # Metrics
    title = None
    content_sections = []
    meta_sections = []
    content_bullets = 0
    all_bullets = 0
    max_heading_depth = 0
    max_list_depth = 0
    
    for line in lines:
        # Check for heading
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if heading_match:
            hashes, heading_text = heading_match.groups()
            heading_level = len(hashes)
            max_heading_depth = max(max_heading_depth, heading_level)
            
            section_type = categorize_section(heading_text, heading_level)
            
            # Track title separately (never counts)
            if section_type == 'title':
                title = heading_text
                current_section = None
                current_section_type = None
                continue
            
            # Only track ## level 2 sections (top-level content sections)
            if heading_level == 2:
                current_section = heading_text
                current_section_type = section_type
                
                if section_type == 'content':
                    content_sections.append(heading_text)
                else:  # meta
                    meta_sections.append(heading_text)
            continue
        
        # Check for bullet points
        stripped = line.lstrip()
        if stripped.startswith(('-', '*', '•')):
            # Calculate indent level (each 2 spaces = 1 level)
            indent = len(line) - len(stripped)
            depth_level = (indent // 2) + 1
            max_list_depth = max(max_list_depth, depth_level)
            
            # Only count top-level bullets
            if indent == 0:
                all_bullets += 1
                # Only count if in content section
                if current_section_type == 'content':
                    content_bullets += 1
    
    # Concept count: ONLY content sections + bullets in content sections
    concepts = len(content_sections) + content_bullets
    
    # Hierarchy depth: max of heading depth or list depth
    depth = max(max_heading_depth, max_list_depth)
    
    return {
        'concepts': concepts,
        'depth': depth,
        'complexity': concepts * depth,
        'title': title,
        'content_sections': content_sections,
        'content_bullets': content_bullets,
        'meta_sections': meta_sections,
        'total_sections': len(content_sections) + len(meta_sections),
        'total_bullets': all_bullets,
        'max_heading_depth': max_heading_depth,
        'max_list_depth': max_list_depth,
        # Legacy fields for compatibility
        'headings': len(content_sections),  # Only content sections
        'bullets': content_bullets  # Only content bullets
    }

def validate_text_patterns(prompt_text, tier):
    """
    Validate text patterns per tier (3-5 words for Concise, etc.).

    Critical: Tier density comes from TEXT PER CONCEPT, not concept count.
    - Concise: 3-5 words max, no drilldown (topic - detail)
    - Standard: 10-15 words max, one level of detail allowed
    - Detailed: Multi-level explanations expected

    Returns: list of issues (empty if all patterns correct)
    """
    import re

    issues = []

    # Extract content bullets (not from Style or Structure sections)
    current_section_type = None
    content_bullets = []

    for line in prompt_text.split('\n'):
        # Track section type
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if heading_match:
            heading_level = len(heading_match.group(1))
            heading_text = heading_match.group(2).strip()

            if heading_level == 2:
                section_type = categorize_section(heading_text, heading_level)
                current_section_type = section_type

        # Extract bullets from content sections only
        bullet_match = re.match(r'^\s*[-•]\s+(.+)$', line)
        if bullet_match and current_section_type == 'content':
            bullet_text = bullet_match.group(1).strip()
            # Remove bold markers for word counting
            bullet_text = re.sub(r'\*\*(.+?)\*\*', r'\1', bullet_text)
            content_bullets.append(bullet_text)

    # Tier-specific validation
    if tier == 'concise':
        for bullet in content_bullets:
            # Check word count FIRST (3-5 words max total)
            words = bullet.split()
            if len(words) > 5:
                issues.append(f"❌ Too many words in Concise tier: '{bullet[:50]}...' ({len(words)} words, max 5)")

                # If over 5 words AND has drilldown pattern, check descriptor length
                if ' - ' in bullet:
                    parts = bullet.split(' - ', 1)
                    if len(parts) == 2:
                        descriptor_words = parts[1].split()
                        if len(descriptor_words) > 3:
                            issues.append(f"⚠️  Long descriptor in drilldown: '{parts[1][:30]}...' ({len(descriptor_words)} words, prefer ≤3 for brief drilldown)")

            # Check for multi-sentence
            if '. ' in bullet and not bullet.endswith('.'):
                issues.append(f"❌ Multi-sentence in Concise tier: '{bullet[:50]}...' (should be single label)")

    elif tier == 'standard':
        for bullet in content_bullets:
            # Check word count (10-15 words max)
            words = bullet.split()
            if len(words) > 15:
                issues.append(f"⚠️  Too many words in Standard tier: '{bullet[:50]}...' ({len(words)} words, max 15)")

            # Check for multi-sentence (more than one period not at end)
            periods = bullet.count('. ')
            if periods > 1:
                issues.append(f"❌ Multi-sentence in Standard tier: '{bullet[:50]}...' (max 1 sentence)")

    elif tier == 'detailed':
        # Check for nested bullets (should have multi-level structure)
        has_nested = re.search(r'^\s{2,}-', prompt_text, re.MULTILINE)
        if not has_nested:
            issues.append("⚠️  No nested bullets in Detailed tier (should have multi-level structure)")

    return issues

def validate_prompt_against_tier(prompt_path, tier='concise'):
    """
    Analyze prompt structure and validate against density tier.

    Args:
        prompt_path: Path to prompt.md file
        tier: 'concise', 'standard', or 'detailed'

    Returns:
        dict with validation results and metrics
    """
    with open(prompt_path, 'r', encoding='utf-8') as f:
        prompt_text = f.read()

    # Structural analysis
    metrics = analyze_prompt_structure(prompt_text)

    # Text pattern validation (NEW: checks text per concept)
    text_issues = validate_text_patterns(prompt_text, tier)

    # Tier expectations (adjusted based on real-world prompts)
    tier_specs = {
        'concise': {
            'concepts': (5, 16),
            'depth': (1, 2),
            'description': 'Few to moderate concepts (5-16), shallow depth (1-2 levels)'
        },
        'standard_breadth': {
            'concepts': (15, 25),
            'depth': (1, 2),
            'description': 'Many concepts (15-25) at shallow depth (1-2 levels) - BREADTH'
        },
        'standard_depth': {
            'concepts': (8, 15),
            'depth': (3, 3),
            'description': 'Moderate concepts (8-15) at medium depth (3 levels) - DEPTH'
        },
        'detailed': {
            'concepts': (25, 999),  # 25+ concepts, no practical upper limit
            'depth': (4, 10),
            'description': 'Many concepts (25+) AND deep detail (4+ levels) - BOTH'
        }
    }

    # Validate
    if tier == 'standard':
        # Check if it matches breadth OR depth variant
        spec_breadth = tier_specs['standard_breadth']
        spec_depth = tier_specs['standard_depth']

        matches_breadth = (
            spec_breadth['concepts'][0] <= metrics['concepts'] <= spec_breadth['concepts'][1] and
            spec_breadth['depth'][0] <= metrics['depth'] <= spec_breadth['depth'][1]
        )
        matches_depth = (
            spec_depth['concepts'][0] <= metrics['concepts'] <= spec_depth['concepts'][1] and
            metrics['depth'] == spec_depth['depth'][0]
        )

        valid = matches_breadth or matches_depth
        variant = 'breadth' if matches_breadth else 'depth' if matches_depth else 'neither'
        expected = spec_breadth if matches_breadth else spec_depth if matches_depth else spec_breadth
    else:
        spec = tier_specs.get(tier, tier_specs['concise'])
        valid = (
            spec['concepts'][0] <= metrics['concepts'] <= spec['concepts'][1] and
            spec['depth'][0] <= metrics['depth'] <= spec['depth'][1]
        )
        variant = None
        expected = spec

    return {
        'valid': valid and len(text_issues) == 0,  # Must pass both structure AND text patterns
        'tier': tier,
        'variant': variant,
        'metrics': metrics,
        'expected': expected,
        'text_issues': text_issues,  # NEW: text pattern validation results
        'prompt_path': prompt_path
    }

def analyze_infographic_structure(image_path):
    """
    Analyze infographic via OCR to extract concepts and hierarchy depth.

    Uses Tesseract OCR to extract text with bounding boxes, then:
    - Clusters font sizes (from bbox heights) into hierarchy levels
    - Counts large text blocks as concepts

    Returns: dict with concepts, depth, complexity, and text blocks

    NOTE: Requires tesseract-ocr installed (brew install tesseract on macOS)
    """
    try:
        from PIL import Image
        import pytesseract
        import numpy as np
        from sklearn.cluster import KMeans
    except ImportError:
        print("ERROR: Required libraries not installed")
        print("Install with: pip install pillow pytesseract scikit-learn")
        print("Also install tesseract: brew install tesseract (macOS) or apt-get install tesseract-ocr (Linux)")
        return {
            'concepts': 0,
            'depth': 0,
            'complexity': 0,
            'text_blocks': [],
            'error': 'Missing dependencies'
        }

    # Run OCR with bounding boxes
    image = Image.open(image_path)
    ocr_data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    # Extract text blocks with sizes (bbox height = font size proxy)
    text_blocks = []
    for i in range(len(ocr_data['text'])):
        text = ocr_data['text'][i].strip()
        if text and len(text) > 2:  # Skip single chars
            height = ocr_data['height'][i]
            text_blocks.append({
                'text': text,
                'size': height,
                'x': ocr_data['left'][i],
                'y': ocr_data['top'][i],
                'width': ocr_data['width'][i],
                'height': height
            })

    if not text_blocks:
        return {
            'concepts': 0,
            'depth': 0,
            'complexity': 0,
            'text_blocks': [],
            'error': 'No text detected in image'
        }

    # Cluster font sizes into hierarchy levels (k-means)
    sizes = np.array([b['size'] for b in text_blocks]).reshape(-1, 1)
    n_clusters = min(4, len(set(sizes.flatten())))  # Max 4 levels, or fewer if not enough variety

    if n_clusters > 1:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        labels = kmeans.fit_predict(sizes)

        # Sort clusters by size (largest = level 1, smallest = level n)
        cluster_sizes = sorted([(i, kmeans.cluster_centers_[i][0]) for i in range(n_clusters)],
                              key=lambda x: x[1], reverse=True)

        # Assign hierarchy levels to text blocks
        for i, block in enumerate(text_blocks):
            cluster_id = labels[i]
            # Find level (1 = largest, n = smallest)
            level = next(idx + 1 for idx, (cid, _) in enumerate(cluster_sizes) if cid == cluster_id)
            block['level'] = level

        # Count concepts (large text blocks = level 1 or 2)
        concepts = sum(1 for b in text_blocks if b.get('level', 99) <= 2)
        depth = n_clusters
    else:
        # All same size - flat hierarchy
        for block in text_blocks:
            block['level'] = 1
        concepts = len(text_blocks)
        depth = 1

    return {
        'concepts': concepts,
        'depth': depth,
        'complexity': concepts * depth,
        'text_blocks': text_blocks,
        'n_clusters': n_clusters
    }

def validate_image_against_tier(image_path, tier='concise'):
    """
    Analyze infographic via OCR and validate against density tier.

    Args:
        image_path: Path to image file (.png, .webp, .jpg)
        tier: 'concise', 'standard', or 'detailed'

    Returns:
        dict with validation results and metrics
    """
    # OCR extraction with layout
    metrics = analyze_infographic_structure(image_path)

    if 'error' in metrics:
        return {
            'valid': False,
            'tier': tier,
            'variant': None,
            'metrics': metrics,
            'error': metrics['error']
        }

    # Use same tier specs as prompts
    tier_specs = {
        'concise': {
            'concepts': (5, 8),
            'depth': (1, 2),
            'description': 'Few concepts (5-8), shallow depth (1-2 levels)'
        },
        'standard_breadth': {
            'concepts': (10, 15),
            'depth': (1, 2),
            'description': 'Many concepts (10-15) at shallow depth (1-2 levels) - BREADTH'
        },
        'standard_depth': {
            'concepts': (5, 8),
            'depth': (3, 3),
            'description': 'Few concepts (5-8) at medium depth (3 levels) - DEPTH'
        },
        'detailed': {
            'concepts': (20, 30),
            'depth': (4, 10),
            'description': 'Many concepts (20-30+) AND deep detail (4+ levels) - BOTH'
        }
    }

    # Validate (same logic as prompts)
    if tier == 'standard':
        spec_breadth = tier_specs['standard_breadth']
        spec_depth = tier_specs['standard_depth']

        matches_breadth = (
            spec_breadth['concepts'][0] <= metrics['concepts'] <= spec_breadth['concepts'][1] and
            spec_breadth['depth'][0] <= metrics['depth'] <= spec_breadth['depth'][1]
        )
        matches_depth = (
            spec_depth['concepts'][0] <= metrics['concepts'] <= spec_depth['concepts'][1] and
            metrics['depth'] == spec_depth['depth'][0]
        )

        valid = matches_breadth or matches_depth
        variant = 'breadth' if matches_breadth else 'depth' if matches_depth else 'neither'
        expected = spec_breadth if matches_breadth else spec_depth if matches_depth else spec_breadth
    else:
        spec = tier_specs.get(tier, tier_specs['concise'])
        valid = (
            spec['concepts'][0] <= metrics['concepts'] <= spec['concepts'][1] and
            spec['depth'][0] <= metrics['depth'] <= spec['depth'][1]
        )
        variant = None
        expected = spec

    return {
        'valid': valid,
        'tier': tier,
        'variant': variant,
        'metrics': metrics,
        'expected': expected,
        'image_path': image_path
    }

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
        description="Generate infographics using Gemini with parallel tabs, or validate prompts/images against density tiers",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Generation mode arguments
    parser.add_argument('--content', help='Content file or text (required for generation)')
    parser.add_argument('--prompt', help='Prompt file or text (required for generation)')
    parser.add_argument('--output-dir', type=Path, default=Path.cwd(), help='Output directory')
    parser.add_argument('--name', default='infographic', help='Base filename')
    parser.add_argument('--variants', type=int, default=1, help='Number of variants to generate (auto-detects starting number)')
    parser.add_argument('--aspect-ratio', choices=['landscape', 'portrait', 'square'], default='landscape', help='Aspect ratio')
    parser.add_argument('--density', choices=['concise', 'standard', 'detailed'], default='standard', help='Information density tier (default: standard)')
    parser.add_argument('--skip-webp', action='store_true', help='Skip WebP conversion')
    parser.add_argument('--resolution', default='1080p', help='WebP resolution')
    parser.add_argument('--chrome-profile', default='Default', help='Chrome profile')
    
    # Validation mode arguments
    parser.add_argument('--validate-prompt', type=Path, help='Validate prompt file against tier')
    parser.add_argument('--validate-image', type=Path, help='Validate infographic image against tier')

    args = parser.parse_args()

    # Validation mode
    if args.validate_prompt or args.validate_image:
        if args.validate_prompt:
            print(f"📊 Validating prompt: {args.validate_prompt}")
            print(f"🎯 Target tier: {args.density}\n")
            
            result = validate_prompt_against_tier(args.validate_prompt, args.density)
            
            print("=" * 60)
            print(f"{'✅ VALID' if result['valid'] else '❌ INVALID'}: {args.density.upper()} TIER")
            print("=" * 60)
            
            metrics = result['metrics']
            expected = result['expected']
            
            print(f"\n📈 Structural Metrics:")
            # Show title (excluded from count)
            if metrics.get('title'):
                print(f"\n  Title: \"{metrics['title']}\" (excluded from count)")
            
            print(f"\n  Concepts: {metrics['concepts']} (expected: {expected['concepts'][0]}-{expected['concepts'][1]})")
            print(f"    Breakdown:")
            
            # Content sections (counted)
            if metrics.get('content_sections'):
                print(f"      ✅ Content sections: {len(metrics['content_sections'])} (counted)")
                for section in metrics['content_sections']:
                    print(f"         • {section}")
            
            # Content bullets (counted)
            if metrics.get('content_bullets', 0) > 0:
                print(f"      ✅ Content bullets: {metrics['content_bullets']} (counted)")
            
            # Meta sections (ignored)
            if metrics.get('meta_sections'):
                print(f"      ⏭️  Meta sections: {len(metrics['meta_sections'])} (ignored)")
                for section in metrics['meta_sections']:
                    print(f"         • {section}")
            print(f"  Depth: {metrics['depth']} levels (expected: {expected['depth'][0]}-{expected['depth'][1]})")
            print(f"    - Max heading depth: {metrics['max_heading_depth']}")
            print(f"    - Max list nesting: {metrics['max_list_depth']}")
            print(f"  Complexity: {metrics['complexity']} (concepts × depth)")
            
            if args.density == 'standard' and result['valid']:
                print(f"\n💡 Standard tier variant: {result['variant']}")
                if result['variant'] == 'breadth':
                    print(f"   Strategy: Wide (many concepts, shallow depth)")
                elif result['variant'] == 'depth':
                    print(f"   Strategy: Deep (few concepts, deep detail)")
            
            # Text pattern issues (always show if present, even if structural metrics pass)
            if result['text_issues']:
                print(f"\n⚠️  Text Pattern Issues:")
                for issue in result['text_issues']:
                    print(f"  {issue}")

            # Structural issues
            if not result['valid']:
                structural_issues = []
                if metrics['concepts'] < expected['concepts'][0]:
                    structural_issues.append(f"  - Too few concepts: {metrics['concepts']} < {expected['concepts'][0]}")
                elif metrics['concepts'] > expected['concepts'][1]:
                    structural_issues.append(f"  - Too many concepts: {metrics['concepts']} > {expected['concepts'][1]}")

                if metrics['depth'] < expected['depth'][0]:
                    structural_issues.append(f"  - Too shallow: {metrics['depth']} < {expected['depth'][0]} levels")
                elif metrics['depth'] > expected['depth'][1]:
                    structural_issues.append(f"  - Too deep: {metrics['depth']} > {expected['depth'][1]} levels")

                if structural_issues and not result['text_issues']:
                    print(f"\n⚠️  Structural Issues:")
                elif structural_issues and result['text_issues']:
                    print(f"\n⚠️  Structural Issues:")

                for issue in structural_issues:
                    print(issue)

            sys.exit(0 if result['valid'] else 1)
        
        elif args.validate_image:
            print(f"🖼️  Validating infographic: {args.validate_image}")
            print(f"🎯 Target tier: {args.density}\n")
            
            try:
                result = validate_image_against_tier(args.validate_image, args.density)
                
                print("=" * 60)
                print(f"{'✅ VALID' if result['valid'] else '❌ INVALID'}: {args.density.upper()} TIER")
                print("=" * 60)
                
                metrics = result['metrics']
                expected = result['expected']
                
                print(f"\n📈 OCR-Based Metrics:")
                print(f"  Concepts: {metrics['concepts']} (expected: {expected['concepts'][0]}-{expected['concepts'][1]})")
                print(f"  Depth: {metrics['depth']} hierarchy levels (expected: {expected['depth'][0]}-{expected['depth'][1]})")
                print(f"  Complexity: {metrics['complexity']} (concepts × depth)")
                print(f"  Text blocks extracted: {len(metrics.get('text_blocks', []))}")
                
                if args.density == 'standard' and result['valid']:
                    print(f"\n💡 Standard tier variant: {result['variant']}")
                    if result['variant'] == 'breadth':
                        print(f"   Strategy: Wide (many concepts, shallow depth)")
                    elif result['variant'] == 'depth':
                        print(f"   Strategy: Deep (few concepts, deep detail)")
                
                if not result['valid']:
                    print(f"\n⚠️  Issues:")
                    if metrics['concepts'] < expected['concepts'][0]:
                        print(f"  - Too few concepts: {metrics['concepts']} < {expected['concepts'][0]}")
                    elif metrics['concepts'] > expected['concepts'][1]:
                        print(f"  - Too many concepts: {metrics['concepts']} > {expected['concepts'][1]}")
                    
                    if metrics['depth'] < expected['depth'][0]:
                        print(f"  - Too shallow: {metrics['depth']} < {expected['depth'][0]} levels")
                    elif metrics['depth'] > expected['depth'][1]:
                        print(f"  - Too deep: {metrics['depth']} > {expected['depth'][1]} levels")
                
                sys.exit(0 if result['valid'] else 1)
            
            except Exception as e:
                print(f"❌ Error during image validation: {e}")
                import traceback
                traceback.print_exc()
                sys.exit(1)

    # Generation mode - require content and prompt
    if not args.content or not args.prompt:
        parser.error("--content and --prompt are required for generation mode")

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

    # Auto-detect next available variant number
    start_num = get_next_variant_number(args.output_dir, args.name)
    print(f"\n🔍 Auto-detected next variant number: {start_num}")
    print(f"   (scanned {args.output_dir} for existing {args.name}-*.png/webp files)")

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
