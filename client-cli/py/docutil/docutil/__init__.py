"""docutil - DOCX document analysis and formatting utilities."""

__version__ = "0.1.0"

from .core import (
    word_count,
    heading_count,
    density_metrics,
    resize_images,
    convert_to_docx,
)

__all__ = [
    "word_count",
    "heading_count",
    "density_metrics",
    "resize_images",
    "convert_to_docx",
]
