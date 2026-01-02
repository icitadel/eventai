# docutil

DOCX document analysis and formatting utilities for academic content workflows.

## Installation

```bash
pipx install -e /path/to/docutil
```

## Usage

### Convert to DOCX (using Pandoc)
```bash
# Convert Markdown to DOCX
docutil convert document.md

# Specify output path
docutil convert document.md -o output.docx

# With resource path for images
docutil convert document.md --resource-path ../
```

### Count Words
```bash
docutil count-words document.docx
```

### Analyze Heading Levels
```bash
docutil count-headings document.docx
```

### Analyze Density Metrics
```bash
docutil analyze-density document.docx
```

### Resize Images
```bash
docutil resize-images document.docx --width 6.5
```

## Features

- **File conversion** using Pandoc (Markdown, HTML, RST, LaTeX → DOCX)
- Word counting (excluding headers/footers)
- Heading level analysis (H1-H6)
- Density metrics (words/sentence, sentences/paragraph, paragraphs/section)
- Image resizing with aspect ratio preservation
- Text wrapping control ("Above and Below")
