"""Command-line interface for docutil."""

import click
from pathlib import Path
from .core import word_count, heading_count, density_metrics, resize_images, convert_to_docx, justify_text


@click.group()
@click.version_option(version="0.1.0")
def main():
    """DOCX document analysis and formatting utilities."""
    pass


@main.command()
@click.argument('filepath', type=click.Path(exists=True))
def count_words(filepath):
    """Count words in a DOCX file (excluding headers/footers)."""
    try:
        count = word_count(filepath)
        click.echo(f"Word count: {count:,}")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()


@main.command()
@click.argument('filepath', type=click.Path(exists=True))
def count_headings(filepath):
    """Count heading levels (H1-H6) in a DOCX file."""
    try:
        counts = heading_count(filepath)
        if not counts:
            click.echo("No headings found.")
            return
        
        click.echo("Heading counts:")
        for level in sorted(counts.keys()):
            click.echo(f"  {level}: {counts[level]}")
        
        total = sum(counts.values())
        click.echo(f"\nTotal headings: {total}")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()


@main.command()
@click.argument('filepath', type=click.Path(exists=True))
def analyze_density(filepath):
    """Analyze density metrics (words/sentence, sentences/paragraph, etc.)."""
    try:
        metrics = density_metrics(filepath)
        
        click.echo("Document Structure:")
        click.echo(f"  Total words: {metrics['total_words']:,}")
        click.echo(f"  Total sentences: {metrics['total_sentences']:,}")
        click.echo(f"  Total paragraphs: {metrics['total_paragraphs']:,}")
        click.echo(f"  Total sections: {metrics['total_sections']:,}")
        
        click.echo("\nDensity Metrics:")
        click.echo(f"  Words per sentence: {metrics['words_per_sentence']:.1f}")
        click.echo(f"  Sentences per paragraph: {metrics['sentences_per_paragraph']:.1f}")
        click.echo(f"  Paragraphs per section: {metrics['paragraphs_per_section']:.1f}")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()


@main.command(name='resize-images')
@click.argument('filepath', type=click.Path(exists=True))
@click.option('--width', type=float, default=6.5, help='Target image width in inches (default: 6.5)')
@click.option('--wrap', type=click.Choice(['top-bottom', 'inline']), default='top-bottom',
              help='Text wrapping style (default: top-bottom)')
def format_images_cmd(filepath, width, wrap):
    """Resize images in a DOCX file to specified width."""
    try:
        from .core import resize_images as _resize_images
        count = _resize_images(filepath, width_inches=width, wrap_style=wrap)
        click.echo(f"✅ Formatted {count} images to {width}\" wide")
        if wrap == 'top-bottom':
            click.echo(f"   Text wrapping: Above and Below")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()


@main.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('-o', '--output', type=click.Path(), help='Output DOCX file path (default: replace input extension)')
@click.option('--resource-path', type=click.Path(exists=True), help='Path for resolving relative image/resource paths')
@click.option('--width', type=float, help='Resize images to specified width in inches (e.g., 6.5)')
@click.option('--justify/--no-justify', default=False, help='Apply justified alignment to body paragraphs')
def convert(input_file, output, resource_path, width, justify):
    """Convert a file to DOCX format using Pandoc (supports Markdown, HTML, etc.)."""
    try:
        output_path = convert_to_docx(input_file, output, resource_path, image_width=width, justify=justify)
        click.echo(f"✅ Converted to: {output_path}")
        if width:
            click.echo(f"✅ Resized images to {width}\" wide")
        if justify:
            click.echo(f"✅ Applied justified text alignment")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()


if __name__ == '__main__':
    main()
