#!/usr/bin/env python3
"""Apply justified text alignment to DOCX file."""

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
import sys

def justify_document(filepath):
    """Apply justified alignment to body paragraphs, keep headings left-aligned."""
    doc = Document(filepath)

    modified_count = 0
    for paragraph in doc.paragraphs:
        # Skip headings (keep left-aligned)
        if paragraph.style.name.startswith('Heading'):
            continue

        # Skip blockquotes and other special styles
        if paragraph.style.name in ['Quote', 'Block Text', 'Caption']:
            continue

        # Apply justified alignment to body text
        paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        modified_count += 1

    doc.save(filepath)
    print(f"✅ Justified {modified_count} paragraphs in {filepath}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python justify_docx.py <file.docx>")
        sys.exit(1)

    justify_document(sys.argv[1])
