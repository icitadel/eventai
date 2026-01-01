# Todd Media Library

Media processing and generation tools for the EventAI project.

## Directory Structure

```
todd-media/
├── gemini-generate/          # Infographic generation & validation
│   ├── gemini_generate.py   # Main CLI tool
│   ├── tests/               # Automated test suite (23 tests)
│   ├── package.json         # npm test scripts
│   ├── VALIDATION_USAGE.md  # CLI usage guide
│   └── README.md            # Detailed documentation
└── README.md                # This file
```

## Tools

### Gemini Infographic Generator

AI-powered infographic generation with density tier validation.

**Features:**
- Generate multiple infographic variants using Gemini
- Validate prompts/images against density tiers (Concise/Standard/Detailed)
- Automated structural analysis (concept count × hierarchy depth)
- Comprehensive test suite (23 automated tests)

**Quick start:**
```bash
cd gemini-generate

# Generate infographics
python3 gemini_generate.py \
  --content source.md \
  --prompt infographic.md \
  --density concise \
  --variants 3

# Validate prompt
python3 gemini_generate.py \
  --validate-prompt my-prompt.md \
  --density concise

# Run tests
npm test
```

See [gemini-generate/README.md](gemini-generate/README.md) for detailed documentation.

## Future Tools

This directory will contain additional media processing tools:
- Image conversion and optimization
- Video processing
- Audio generation
- Media asset management

---

*Last updated: January 1, 2026*
*Part of: EventAI Todd Automation System*
