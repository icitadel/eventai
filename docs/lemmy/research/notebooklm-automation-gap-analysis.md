# NotebookLM Automation Gap Analysis

**Date**: December 28, 2025
**Purpose**: Evaluate automation feasibility for NotebookLM infographic generation
**Scope**: API access, browser automation, and manual workflow comparison

---

## Executive Summary

**Key Finding**: Full automation of NotebookLM infographic generation is **NOT currently possible** without significant workarounds or paid alternatives.

### What Works
✅ NotebookLM Enterprise API for audio overview generation (alpha)
✅ Browser automation for source uploading (proven by community)
✅ Manual workflow is well-documented and efficient (~17 min per infographic)

### What Doesn't Work
❌ No API for infographic generation (Enterprise or free)
❌ No API for slide deck generation
❌ No API for video overview generation
❌ Google authentication required (blocks headless automation)
❌ No official automation support

### Recommendation
**Use manual workflow** for first content generation. The manual process is fast (~17 minutes), well-documented, and includes necessary human quality review. Automation would save time but introduce authentication complexity and still require human review.

---

## Detailed Findings

### 1. NotebookLM API Availability

#### Enterprise API (Alpha)
**Status**: Available with Google Cloud setup
**Version**: v1alpha (subject to change)
**Access**: Requires Google Cloud project, billing enabled

**Available Endpoints**:
- ✅ `notebooks.create` - Create new notebooks
- ✅ `notebooks.get` - Retrieve notebook details
- ✅ `notebooks.listRecentlyViewed` - List recent notebooks
- ✅ `notebooks.batchDelete` - Delete multiple notebooks
- ✅ `notebooks.share` - Share notebooks
- ✅ `notebooks.sources.batchCreate` - Add data sources
- ✅ **Audio Overview Generation** - Create audio/podcast from sources

**NOT Available via API**:
❌ Infographic generation
❌ Slide deck generation
❌ Video overview generation
❌ Customization prompt application
❌ Download/export automation

**Source**: [Google Cloud NotebookLM Enterprise Documentation](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks)

#### Free NotebookLM
**Status**: No API access
**Access**: Web interface only at notebooklm.google.com
**Automation**: Not supported or documented

**Source**: [AutoContent API Analysis](https://autocontentapi.com/blog/does-notebooklm-have-an-api)

### 2. Browser Automation Assessment

#### Playwright Feasibility

**Proven Capabilities** (from community projects):
- ✅ Source uploading automation
- ✅ Notebook creation
- ✅ Navigation to NotebookLM interface

**GitHub Evidence**:
- [DataNath/notebooklm_source_automation](https://github.com/DataNath/notebooklm_source_automation) - Python/Playwright for link uploads
- [Databasyx Blog](https://oboe-violin-w3kd.squarespace.com/blogs/automating-link-uploads-to-notebooklm-using-python-and-playwright) - Tutorial on link automation
- NotebookLM MCP Server (khengyun) - Selenium-based automation for chat interactions

#### Critical Blocker: Google Authentication

**Issue Discovered**: NotebookLM redirects to Google Sign-In page
**Test Result**: When navigating to `https://notebooklm.google.com/`:
```
Redirect → https://accounts.google.com/v3/signin/identifier
Page Title: Sign in - Google Accounts
```

**Authentication Challenges**:
1. **OAuth Required**: NotebookLM requires Google account authentication
2. **2FA/Security**: Many accounts have 2-factor authentication
3. **Session Management**: Cookies/tokens expire, requiring re-auth
4. **Terms Violation Risk**: Automated access may violate Google TOS
5. **Maintenance Burden**: Auth flow changes break automation

**Workarounds** (all have drawbacks):
- **Option A**: Store credentials (security risk, violates best practices)
- **Option B**: Manual login, save session (expires, fragile)
- **Option C**: Use Google Cloud Identity (complex setup, Enterprise only)
- **Option D**: Browser profile reuse (brittle, still requires periodic re-auth)

**Recommendation**: Authentication complexity outweighs benefits for current use case

#### Infographic Generation Automation

**Theoretical Steps** (untested):
1. Navigate to notebook
2. Click "Infographic" button
3. Select detail level, orientation
4. Paste customization prompt
5. Click "Generate"
6. Wait for completion (~1-2 minutes)
7. Click download icon
8. Save file

**Unknown Feasibility**:
- ❓ Can Playwright reliably detect generation completion?
- ❓ Does NotebookLM use dynamic element IDs (fragile selectors)?
- ❓ Are there rate limits on generation?
- ❓ How does download dialog work (may require special handling)?

**Human Review Required**:
Even with full automation, quality control is mandatory:
- ✅ Data accuracy verification (AI can hallucinate)
- ✅ Style compliance check (EventAI brand)
- ✅ Text legibility confirmation
- ✅ Festival context appropriateness

**Time Saved vs. Complexity**:
- Manual generation: ~10 minutes active work (17 min total)
- Automation development: 8-16 hours (authentication, testing, error handling)
- Automation maintenance: Ongoing (UI changes, auth issues)
- **ROI**: Negative for 20 infographics, potentially positive for 100+

### 3. Alternative Approaches

#### Option A: Paid Infographic APIs
**Services**:
- Venngage API (enterprise tier)
- Canva API (limited access)
- Piktochart API (custom pricing)
- Custom Gemini/DALL-E prompting

**Pros**:
- ✅ Full API access
- ✅ No authentication issues
- ✅ Programmatic generation

**Cons**:
- ❌ Additional cost ($500-5,000/month typical)
- ❌ Different quality/style than NotebookLM
- ❌ Requires custom prompt development
- ❌ May not match EventAI style guide

#### Option B: Nano Banana (Google Gemini Image Model)
**Already Documented**: [../prompts/images/nano-banana.prompt.md](../prompts/images/nano-banana.prompt.md)

**Pros**:
- ✅ Programmatic access via Gemini API
- ✅ High-quality image generation
- ✅ Customizable prompts

**Cons**:
- ❌ Not optimized for infographics (better for illustrations)
- ❌ Less structured data visualization
- ❌ Requires more detailed prompts
- ❌ Different workflow than NotebookLM

**Best Use**: Custom diagrams (VIS-1.3, VIS-2.2, VIS-4.2, VIS-4.4) rather than data-heavy infographics

#### Option C: Hybrid Approach
**Strategy**:
- Use NotebookLM (manual) for data-heavy infographics
- Use Nano Banana (API) for conceptual diagrams
- Use Claude Code to prepare prompts and sources

**Pros**:
- ✅ Best tool for each visual type
- ✅ Some automation where it matters
- ✅ Human review still integrated

**Cons**:
- ❌ More complex workflow management
- ❌ Consistency between tools

---

## Manual Workflow Performance

### Current Documentation Quality
**Excellent**: Step-by-step instructions exist for all workflows
- [notebooklm-workflows.md](../workflows/notebooklm-workflows.md)
- [VIS-1.1-GENERATE-INSTRUCTIONS.md](../../writing/1-transformation/visuals/VIS-1.1-GENERATE-INSTRUCTIONS.md)
- [infographic.prompt.md](../prompts/notebooklm/infographic.prompt.md)

### Time Breakdown (Manual)
Per infographic:
- **2 min**: Upload source to NotebookLM
- **10 min**: Configure and generate (includes customization prompt)
- **3 min**: Review quality
- **2 min**: Download and save
- **Total**: ~17 minutes active work

**For 20 infographics**: 5-6 hours total (one session)

### Quality Advantages
✅ **Human review inherent**: Quality check happens naturally during manual workflow
✅ **Iteration flexibility**: Easy to regenerate with prompt adjustments
✅ **Learning opportunity**: User sees NotebookLM capabilities firsthand
✅ **No debugging**: No brittle automation to maintain

### When Automation Would Be Valuable
- **Scale**: 50+ infographics regularly
- **Repetition**: Generating same infographic types repeatedly
- **Batch processing**: Need to generate many variations
- **Integration**: Part of larger automated content pipeline

**EventAI Use Case**: 20 infographics (one-time generation)
→ Automation ROI is **negative** (development time > time saved)

---

## Gap Analysis Matrix

| Requirement | Manual | Playwright | Enterprise API | Alternative API |
|------------|--------|------------|----------------|-----------------|
| **Infographic Generation** | ✅ 17 min | ❓ Untested | ❌ Not available | ✅ Paid services |
| **Audio Overview** | ✅ 13 min | ❓ Untested | ✅ Available | ❌ N/A |
| **Slide Deck** | ✅ 10 min | ❓ Untested | ❌ Not available | ✅ Google Slides API |
| **Video Overview** | ✅ 14 min | ❓ Untested | ❌ Not available | ❌ Limited options |
| **Source Upload** | ✅ 2 min | ✅ Proven | ✅ Available | N/A |
| **Customization Prompts** | ✅ Copy/paste | ❓ Possible | ❓ Unknown | ✅ Varies |
| **Quality Review** | ✅ Built-in | ❌ Separate step | ❌ Separate step | ❌ Separate step |
| **Authentication** | ✅ Standard login | ❌ **Major blocker** | ✅ Cloud Identity | ✅ API keys |
| **Maintenance** | ✅ None | ❌ High (UI changes) | ⚠️ Alpha (may change) | ✅ Stable APIs |
| **Cost** | ✅ Free | ✅ Free (dev time) | ⚠️ GCP billing | ❌ $$$$ |
| **Setup Time** | ✅ 0 min | ❌ 8-16 hours | ⚠️ 2-4 hours | ⚠️ 1-2 hours |

---

## Recommendations

### For EventAI (20 infographics, one-time generation)

**Primary Recommendation**: **Use manual NotebookLM workflow**

**Rationale**:
1. **Time Efficient**: 5-6 hours for 20 infographics (manual) vs. 8-16 hours automation development + 2-3 hours execution
2. **Quality Built-In**: Human review happens during workflow, not as separate step
3. **No Authentication Issues**: Standard Google login, no TOS violations
4. **No Maintenance**: One-time task, no ongoing maintenance burden
5. **Well-Documented**: Complete instructions exist, ready to execute

**Workflow**:
```
For each infographic:
1. Upload source to NotebookLM (use prepared .md files)
2. Click "Infographic", select orientation and detail level
3. Paste EventAI customization prompt
4. Generate (1-2 min wait)
5. Review for accuracy and style
6. Download PNG to visuals/ folder
7. Update VISUAL-CONTENT-PLAN.md status
```

**Next Actions**:
→ See "What You Need to Do Next" section below

### For Future Scaled Operations (100+ infographics)

If EventAI scales to regular infographic generation:

**Consider**: NotebookLM Enterprise API + Playwright hybrid
- Use Enterprise API for audio overviews (proven)
- Investigate Playwright for infographic automation (once authenticated)
- Build quality review workflow (still requires human check)

**Alternative**: Paid infographic APIs (Venngage, Canva, Piktochart)
- Fully programmatic
- Higher cost but no authentication issues
- Requires custom template development

---

## Technical Specifications

### NotebookLM Enterprise API Setup (if pursued)

**Prerequisites**:
1. Google Cloud Project
2. Billing account enabled
3. Gemini API enabled
4. NotebookLM Enterprise access

**Example API Call** (Python):
```python
from google.cloud import discoveryengine

client = discoveryengine.NotebooksClient()

# Create notebook
notebook = client.create_notebook(
    parent=f"projects/{project_id}/locations/{location}",
    notebook={"display_name": "EventAI - Test"}
)

# Add source
client.batch_create_sources(
    parent=notebook.name,
    sources=[{"file_path": "gs://bucket/source.md"}]
)

# Generate audio overview (ONLY this works for rich content)
audio = client.create_audio_overview(
    notebook=notebook.name,
    customization="Create audio for university students..."
)

# Download audio
download_url = audio.download_uri
```

**What Doesn't Work**:
```python
# ❌ No such method exists (as of Dec 2025)
infographic = client.create_infographic(...)  # API ERROR
slide_deck = client.create_slide_deck(...)    # API ERROR
video = client.create_video_overview(...)     # API ERROR
```

### Playwright Automation Template (untested)

**Note**: This is theoretical code. Authentication would need to be solved first.

```python
from playwright.sync_api import sync_playwright

def generate_infographic_automated(source_path, prompt, output_path):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Need user to login
        page = browser.new_page()

        # Navigate (will redirect to login if not authenticated)
        page.goto("https://notebooklm.google.com/")

        # ⚠️ BLOCKER: Need to handle Google OAuth here
        # Manual intervention required for initial login

        # Upload source
        page.click("text=Add sources")
        page.set_input_files("input[type=file]", source_path)
        page.wait_for_selector("text=Processing complete")

        # Generate infographic
        page.click("text=Infographic")
        page.select_option("select#detail-level", "Detailed")
        page.select_option("select#orientation", "Landscape")
        page.fill("textarea#customization", prompt)
        page.click("button:has-text('Generate')")

        # Wait for completion (timing unknown)
        page.wait_for_selector("text=Download", timeout=120000)

        # Download (may require special handling)
        with page.expect_download() as download_info:
            page.click("text=Download")
        download = download_info.value
        download.save_as(output_path)

        browser.close()

# Usage (theoretical)
generate_infographic_automated(
    source_path="VIS-1.1-source.md",
    prompt=open("VIS-1.1-prompt.txt").read(),
    output_path="transformation-infographic-adoption-timeline.png"
)
```

**Unresolved Issues**:
- Google authentication (OAuth flow)
- Session persistence
- Selector stability (may break with UI changes)
- Error handling (network issues, generation failures)
- Rate limiting

---

## Conclusion

### Summary Assessment

**Question**: Can we automate NotebookLM infographic generation without paid APIs?

**Answer**: **Partially, but not recommended for EventAI's current use case**

**Why**:
1. ✅ **Technically Possible**: Browser automation can interact with NotebookLM
2. ❌ **Authentication Blocker**: Google OAuth is significant complexity
3. ❌ **No API for Infographics**: Enterprise API doesn't support visual content generation
4. ⚠️ **ROI Negative**: Development time (8-16 hrs) > time saved (5-6 hrs manual)
5. ✅ **Manual Workflow Excellent**: Well-documented, fast, includes quality review

### Final Recommendation

**For First Content Generation**: Use manual workflow with prepared materials
- Source documents ready: [VIS-1.1-source.md](../../writing/1-transformation/visuals/VIS-1.1-source.md)
- Instructions ready: [VIS-1.1-GENERATE-INSTRUCTIONS.md](../../writing/1-transformation/visuals/VIS-1.1-GENERATE-INSTRUCTIONS.md)
- Estimated time: ~17 minutes for first infographic
- Proven process, no technical blockers

**For Future Consideration**: If scaling to 100+ regular infographics
- Investigate NotebookLM Enterprise API (when infographic generation added)
- OR migrate to paid infographic APIs (Venngage, Canva)
- OR develop Playwright automation with managed authentication

### What Makes Sense Now

**High-Value, Low-Effort**:
- ✅ Use manual NotebookLM for infographics (fast, proven)
- ✅ Use prepared source documents and prompts (ready to go)
- ✅ Human quality review (essential anyway)
- ✅ Complete 20 infographics in single 5-6 hour session

**High-Effort, Low-Value** (avoid for now):
- ❌ Build Playwright automation for 20 one-time infographics
- ❌ Set up NotebookLM Enterprise (doesn't support infographics anyway)
- ❌ Migrate to paid APIs (unnecessary for current scale)

---

## References

**Google Documentation**:
- [NotebookLM Enterprise API - Notebooks](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks)
- [NotebookLM Enterprise API - Sources](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks-sources)

**Community Projects**:
- [DataNath/notebooklm_source_automation](https://github.com/DataNath/notebooklm_source_automation)
- [Automating Link Uploads to NotebookLM](https://oboe-violin-w3kd.squarespace.com/blogs/automating-link-uploads-to-notebooklm-using-python-and-playwright)
- [NotebookLM MCP Server](https://www.pulsemcp.com/servers/khengyun-notebooklm)

**Analysis Articles**:
- [Does NotebookLM Have an API?](https://autocontentapi.com/blog/does-notebooklm-have-an-api)
- [NotebookLM API Alternative](https://autocontentapi.com/notebooklm-api)

**Playwright Resources**:
- [Playwright Official Documentation](https://playwright.dev/)
- [Playwright MCP Guide](https://medium.com/@bluudit/playwright-mcp-comprehensive-guide-to-ai-powered-browser-automation-in-2025-712c9fd6cffa)

---

*Gap Analysis Completed: December 28, 2025*
*Conclusion: Manual workflow recommended for EventAI first content generation*
*Next Step: Execute VIS-1.1 generation using prepared materials*
