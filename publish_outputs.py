#!/usr/bin/env python3
"""
Comprehensive Publication Output Generator
Generates HTML, PDF-ready HTML, and other formats from the research publication
"""

import re
import os
import sys
from datetime import datetime


def markdown_to_html(md_text):
    """Convert markdown to HTML with comprehensive formatting"""

    html = md_text

    # Convert headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)

    # Convert bold (must come before italic)
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)

    # Convert italic
    html = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', html)

    # Convert inline code
    html = re.sub(r'`(.+?)`', r'<code>\1</code>', html)

    # Convert code blocks
    html = re.sub(r'```(\w*)\n(.*?)\n```', r'<pre><code class="\1">\2</code></pre>', html, flags=re.DOTALL)

    # Convert horizontal rules
    html = re.sub(r'^---+$', r'<hr>', html, flags=re.MULTILINE)

    # Convert links
    html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', html)

    # Convert tables (simple table support)
    lines = html.split('\n')
    in_table = False
    result = []

    for i, line in enumerate(lines):
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                result.append('<table>')
                in_table = True
                # This is likely a header row
                cells = [cell.strip() for cell in line.split('|')[1:-1]]
                result.append('<thead><tr>')
                for cell in cells:
                    result.append(f'<th>{cell}</th>')
                result.append('</tr></thead>')
                result.append('<tbody>')
            elif i > 0 and re.match(r'^\|[\s\-:|]+\|$', line):
                # This is a separator row, skip it
                continue
            else:
                # Regular table row
                cells = [cell.strip() for cell in line.split('|')[1:-1]]
                result.append('<tr>')
                for cell in cells:
                    result.append(f'<td>{cell}</td>')
                result.append('</tr>')
        else:
            if in_table:
                result.append('</tbody></table>')
                in_table = False
            result.append(line)

    if in_table:
        result.append('</tbody></table>')

    html = '\n'.join(result)

    # Convert unordered lists
    lines = html.split('\n')
    in_list = False
    result = []

    for line in lines:
        if re.match(r'^\s*[\-\*]\s+', line):
            if not in_list:
                result.append('<ul>')
                in_list = True
            item = re.sub(r'^\s*[\-\*]\s+(.+)$', r'<li>\1</li>', line)
            result.append(item)
        else:
            if in_list:
                result.append('</ul>')
                in_list = False
            result.append(line)

    if in_list:
        result.append('</ul>')

    html = '\n'.join(result)

    # Convert ordered lists
    lines = html.split('\n')
    in_list = False
    result = []

    for line in lines:
        if re.match(r'^\s*\d+\.\s+', line):
            if not in_list:
                result.append('<ol>')
                in_list = True
            item = re.sub(r'^\s*\d+\.\s+(.+)$', r'<li>\1</li>', line)
            result.append(item)
        else:
            if in_list:
                result.append('</ol>')
                in_list = False
            result.append(line)

    if in_list:
        result.append('</ol>')

    html = '\n'.join(result)

    # Convert paragraphs (lines not already in tags)
    lines = html.split('\n')
    result = []
    for line in lines:
        if line.strip() and not re.match(r'^\s*<', line):
            result.append(f'<p>{line}</p>')
        else:
            result.append(line)

    html = '\n'.join(result)

    return html


def create_html_document(content, title="Research Publication", pdf_ready=False):
    """
    Wrap content in a complete HTML document with CSS

    Args:
        content: HTML content to wrap
        title: Document title
        pdf_ready: If True, optimize for PDF conversion
    """

    # Enhanced CSS for better typography and PDF output
    pdf_styles = """
        @page {
            size: A4;
            margin: 2.5cm;
        }

        @media print {
            body {
                background: white;
                font-size: 11pt;
            }

            h1, h2, h3, h4, h5, h6 {
                page-break-after: avoid;
            }

            p, table, pre, blockquote {
                page-break-inside: avoid;
            }

            thead {
                display: table-header-group;
            }

            tr {
                page-break-inside: avoid;
            }
        }
    """ if pdf_ready else ""

    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Derek Lankeaux">
    <meta name="description" content="Enhanced Ensemble Methods for Wisconsin Breast Cancer Classification">
    <title>{title}</title>
    <style>
        {pdf_styles}

        body {{
            font-family: 'Georgia', 'Times New Roman', serif;
            line-height: 1.7;
            color: #333;
            max-width: {'210mm' if pdf_ready else '900px'};
            margin: 0 auto;
            padding: {'10mm' if pdf_ready else '20px'};
            background: white;
            font-size: {'11pt' if pdf_ready else '16px'};
        }}

        h1 {{
            font-size: {'26pt' if pdf_ready else '2.5em'};
            color: #1a1a1a;
            margin-top: {'40px' if pdf_ready else '30px'};
            margin-bottom: 25px;
            page-break-after: avoid;
            text-align: center;
            font-weight: 700;
        }}

        h2 {{
            font-size: {'20pt' if pdf_ready else '2em'};
            color: #2a2a2a;
            margin-top: 35px;
            margin-bottom: 20px;
            border-bottom: 3px solid #0066cc;
            padding-bottom: 8px;
            page-break-after: avoid;
            font-weight: 600;
        }}

        h3 {{
            font-size: {'16pt' if pdf_ready else '1.5em'};
            color: #3a3a3a;
            margin-top: 25px;
            margin-bottom: 15px;
            page-break-after: avoid;
            font-weight: 600;
        }}

        h4 {{
            font-size: {'13pt' if pdf_ready else '1.25em'};
            color: #4a4a4a;
            margin-top: 20px;
            margin-bottom: 10px;
            page-break-after: avoid;
            font-weight: 600;
        }}

        h5, h6 {{
            font-size: {'12pt' if pdf_ready else '1.1em'};
            color: #5a5a5a;
            margin-top: 15px;
            margin-bottom: 8px;
            page-break-after: avoid;
            font-weight: 600;
        }}

        p {{
            margin: 12px 0;
            text-align: justify;
            line-height: 1.7;
        }}

        code {{
            background-color: #f4f4f4;
            padding: 2px 8px;
            border-radius: 4px;
            font-family: 'Courier New', 'Consolas', monospace;
            font-size: {'9pt' if pdf_ready else '0.9em'};
            color: #c7254e;
            border: 1px solid #e1e1e8;
        }}

        pre {{
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-left: 4px solid #0066cc;
            border-radius: 5px;
            padding: 15px 20px;
            overflow-x: auto;
            page-break-inside: avoid;
            margin: 20px 0;
        }}

        pre code {{
            background: none;
            padding: 0;
            border: none;
            color: #333;
            font-size: {'9pt' if pdf_ready else '0.85em'};
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            page-break-inside: avoid;
            font-size: {'10pt' if pdf_ready else '0.95em'};
        }}

        th, td {{
            border: 1px solid #ddd;
            padding: 12px 15px;
            text-align: left;
        }}

        th {{
            background-color: #0066cc;
            color: white;
            font-weight: bold;
            text-align: center;
        }}

        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}

        tr:hover {{
            background-color: #f5f5f5;
        }}

        ul, ol {{
            margin: 15px 0;
            padding-left: 40px;
        }}

        li {{
            margin: 8px 0;
            line-height: 1.6;
        }}

        hr {{
            border: none;
            border-top: 2px solid #ccc;
            margin: 40px 0;
        }}

        strong {{
            font-weight: bold;
            color: #1a1a1a;
        }}

        em {{
            font-style: italic;
        }}

        a {{
            color: #0066cc;
            text-decoration: none;
            border-bottom: 1px dotted #0066cc;
        }}

        a:hover {{
            color: #004499;
            border-bottom: 1px solid #004499;
        }}

        blockquote {{
            border-left: 4px solid #0066cc;
            margin: 20px 0;
            padding: 10px 20px;
            background-color: #f9f9f9;
            font-style: italic;
        }}

        /* Header styling for author/date info */
        .publication-header {{
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 2px solid #ccc;
        }}

        .publication-header p {{
            margin: 5px 0;
            text-align: center;
        }}

        /* Footer */
        .publication-footer {{
            margin-top: 50px;
            padding-top: 20px;
            border-top: 2px solid #ccc;
            text-align: center;
            font-size: {'9pt' if pdf_ready else '0.9em'};
            color: #666;
        }}
    </style>
</head>
<body>
{content}
<div class="publication-footer">
    <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    <p>Enhanced Ensemble Methods for Wisconsin Breast Cancer Classification</p>
    <p>&copy; 2025 Derek Lankeaux - Rochester Institute of Technology</p>
</div>
</body>
</html>"""

    return template


def generate_publication_outputs(markdown_file='FINAL_PUBLICATION.md'):
    """
    Generate all publication outputs from the markdown source

    Args:
        markdown_file: Path to the source markdown file
    """

    if not os.path.exists(markdown_file):
        print(f"Error: {markdown_file} not found!")
        return False

    print(f"Reading {markdown_file}...")
    with open(markdown_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    print("Converting markdown to HTML...")
    html_content = markdown_to_html(md_content)

    # Generate standard HTML version
    print("Generating standard HTML version...")
    standard_html = create_html_document(
        html_content,
        "Enhanced Ensemble Methods for Wisconsin Breast Cancer Classification",
        pdf_ready=False
    )

    output_file = 'FINAL_PUBLICATION.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(standard_html)
    print(f"✓ Created {output_file}")

    # Generate PDF-ready HTML version
    print("Generating PDF-ready HTML version...")
    pdf_ready_html = create_html_document(
        html_content,
        "Enhanced Ensemble Methods for Wisconsin Breast Cancer Classification",
        pdf_ready=True
    )

    pdf_output_file = 'FINAL_PUBLICATION_PDF_READY.html'
    with open(pdf_output_file, 'w', encoding='utf-8') as f:
        f.write(pdf_ready_html)
    print(f"✓ Created {pdf_output_file}")

    # Generate complete project publication
    print("Generating complete project publication...")
    complete_html = create_html_document(
        html_content,
        "Complete Project Publication - Enhanced Ensemble Methods",
        pdf_ready=True
    )

    complete_output_file = 'COMPLETE_PROJECT_PUBLICATION.html'
    with open(complete_output_file, 'w', encoding='utf-8') as f:
        f.write(complete_html)
    print(f"✓ Created {complete_output_file}")

    # Generate summary statistics
    stats = {
        'lines': len(md_content.split('\n')),
        'words': len(md_content.split()),
        'characters': len(md_content),
        'headers': len(re.findall(r'^#+\s+', md_content, re.MULTILINE)),
        'code_blocks': len(re.findall(r'```', md_content)) // 2,
        'tables': len(re.findall(r'^\|.+\|$', md_content, re.MULTILINE)) // 2,
    }

    print("\n" + "="*60)
    print("Publication Statistics:")
    print("="*60)
    print(f"Lines: {stats['lines']:,}")
    print(f"Words: {stats['words']:,}")
    print(f"Characters: {stats['characters']:,}")
    print(f"Headers: {stats['headers']}")
    print(f"Code Blocks: {stats['code_blocks']}")
    print(f"Tables: {stats['tables']}")
    print("="*60)

    print("\n" + "="*60)
    print("Generated Outputs:")
    print("="*60)
    print(f"1. {output_file} - Standard HTML for web viewing")
    print(f"2. {pdf_output_file} - PDF-ready HTML (optimized for printing)")
    print(f"3. {complete_output_file} - Complete project publication")
    print("="*60)

    print("\n" + "="*60)
    print("To Generate PDF:")
    print("="*60)
    print(f"1. Open {pdf_output_file} in your web browser")
    print("2. Press Ctrl+P (Cmd+P on Mac)")
    print("3. Select 'Save as PDF' as the destination")
    print("4. Recommended settings:")
    print("   - Paper size: A4")
    print("   - Margins: Default")
    print("   - Scale: 100%")
    print("   - Background graphics: Enabled")
    print("5. Save as 'Enhanced Ensemble Methods for Wisconsin Breast Cancer Classification.pdf'")
    print("="*60)

    return True


def main():
    """Main entry point"""
    print("\n" + "="*60)
    print("Publication Output Generator")
    print("Enhanced Ensemble Methods for Wisconsin Breast Cancer Classification")
    print("="*60 + "\n")

    markdown_file = 'FINAL_PUBLICATION.md'

    if len(sys.argv) > 1:
        markdown_file = sys.argv[1]

    success = generate_publication_outputs(markdown_file)

    if success:
        print("\n✓ Publication outputs generated successfully!\n")
        return 0
    else:
        print("\n✗ Failed to generate publication outputs\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
