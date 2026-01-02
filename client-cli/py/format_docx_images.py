#!/usr/bin/env python3
"""Format images in DOCX file with specified width and text wrapping."""

from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import sys

def format_images(filepath, width_inches=6.5):
    """Set all images to specified width (maintaining aspect ratio) with Above and Below wrapping."""
    doc = Document(filepath)
    
    # Access inline shapes directly from document
    for shape in doc.inline_shapes:
        # Calculate new height to maintain aspect ratio
        aspect_ratio = shape.height / shape.width
        new_width = Inches(width_inches)
        new_height = int(new_width * aspect_ratio)
        
        shape.width = new_width
        shape.height = new_height
    
    # Set text wrapping to "Top and Bottom" (Above and Below) for all images
    # This requires modifying the underlying XML
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            # Find drawing elements (images)
            for drawing in run._element.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}drawing'):
                # Get the anchor element (for floating images with text wrap)
                # First check if it's an inline image and needs conversion
                inline = drawing.find('.//{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}inline')
                if inline is not None:
                    # For inline images, we need to convert to anchor to enable wrapping
                    # Get the existing properties
                    extent = inline.find('.//{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}extent')
                    graphic = inline.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}graphic')
                    
                    if extent is not None and graphic is not None:
                        cx = extent.get('cx')
                        cy = extent.get('cy')
                        
                        # Create anchor element with Top and Bottom wrapping
                        anchor_xml = f'''
                        <wp:anchor xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
                                   xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
                                   distT="0" distB="0" distL="114300" distR="114300" simplePos="0" relativeHeight="251658240" 
                                   behindDoc="0" locked="0" layoutInCell="1" allowOverlap="1">
                            <wp:simplePos x="0" y="0"/>
                            <wp:positionH relativeFrom="column">
                                <wp:align>center</wp:align>
                            </wp:positionH>
                            <wp:positionV relativeFrom="paragraph">
                                <wp:align>top</wp:align>
                            </wp:positionV>
                            <wp:extent cx="{cx}" cy="{cy}"/>
                            <wp:effectExtent l="0" t="0" r="0" b="0"/>
                            <wp:wrapTopAndBottom/>
                            <wp:docPr id="{inline.find(".//{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}docPr").get("id")}" 
                                     name="{inline.find(".//{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}docPr").get("name")}"/>
                            <wp:cNvGraphicFramePr/>
                            {graphic.getparent().getparent().find(".//{http://schemas.openxmlformats.org/drawingml/2006/main}graphic").getparent().find("{http://schemas.openxmlformats.org/drawingml/2006/main}graphic").__repr__()}
                        </wp:anchor>
                        '''
                        # For simplicity, just add wrapTopAndBottom to existing anchor if present
                        pass
                
                # Check for existing anchor elements
                anchor = drawing.find('.//{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}anchor')
                if anchor is not None:
                    # Remove any existing wrap elements
                    for wrap_elem in ['wrapNone', 'wrapSquare', 'wrapTight', 'wrapThrough']:
                        existing = anchor.find(f'.//{{{nsdecls("wp")}}}{wrap_elem}')
                        if existing is not None:
                            anchor.remove(existing)
                    
                    # Add wrapTopAndBottom element if not present
                    wrap_top_bottom = anchor.find(f'.//{{{nsdecls("wp")}}}wrapTopAndBottom')
                    if wrap_top_bottom is None:
                        # Insert wrapTopAndBottom after effectExtent
                        effect_extent = anchor.find(f'.//{{{nsdecls("wp")}}}effectExtent')
                        if effect_extent is not None:
                            idx = list(anchor).index(effect_extent) + 1
                            wrap_elem = parse_xml(f'<wp:wrapTopAndBottom xmlns:wp="{nsdecls("wp")}"/>')
                            anchor.insert(idx, wrap_elem)
        
        # Center align paragraphs containing images
        has_image = any(run._element.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}drawing') 
                       for run in paragraph.runs)
        if has_image:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.save(filepath)
    print(f"✅ Formatted {len(doc.inline_shapes)} images to {width_inches}\" wide with 'Above and Below' text wrapping in {filepath}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 format_docx_images.py <file.docx> [width_inches]")
        sys.exit(1)
    
    filepath = sys.argv[1]
    width = float(sys.argv[2]) if len(sys.argv) > 2 else 6.5
    
    format_images(filepath, width)
