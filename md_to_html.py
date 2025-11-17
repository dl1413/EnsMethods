#!/usr/bin/env python3
"""
Simple Markdown to HTML converter for the research publication
"""

import re
import sys

def markdown_to_html(md_text):
    """Convert markdown to HTML with basic formatting"""

    html = md_text

    # Convert headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)

    # Convert bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)

    # Convert italic
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

    # Convert inline code
    html = re.sub(r'`(.+?)`', r'<code>\1</code>', html)

    # Convert code blocks
    html = re.sub(r'```(\w*)\n(.*?)\n```', r'<pre><code class="\1">\2</code></pre>', html, flags=re.DOTALL)

    # Convert horizontal rules
    html = re.sub(r'^---$', r'<hr>', html, flags=re.MULTILINE)

    # Convert links
    html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', html)

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

def create_html_document(content, title="Research Publication"):
    """Wrap content in a complete HTML document with CSS for PDF printing"""

    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        @page {{
            size: A4;
            margin: 2cm;
        }}

        body {{
            font-family: 'Georgia', 'Times New Roman', serif;
            line-height: 1.6;
            color: #333;
            max-width: 210mm;
            margin: 0 auto;
            padding: 20px;
            background: white;
        }}

        h1 {{
            font-size: 24pt;
            color: #1a1a1a;
            margin-top: 30px;
            margin-bottom: 20px;
            page-break-after: avoid;
        }}

        h2 {{
            font-size: 18pt;
            color: #2a2a2a;
            margin-top: 25px;
            margin-bottom: 15px;
            border-bottom: 2px solid #ccc;
            padding-bottom: 5px;
            page-break-after: avoid;
        }}

        h3 {{
            font-size: 14pt;
            color: #3a3a3a;
            margin-top: 20px;
            margin-bottom: 10px;
            page-break-after: avoid;
        }}

        h4 {{
            font-size: 12pt;
            color: #4a4a4a;
            margin-top: 15px;
            margin-bottom: 8px;
            page-break-after: avoid;
        }}

        p {{
            margin: 10px 0;
            text-align: justify;
        }}

        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 10pt;
        }}

        pre {{
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 15px;
            overflow-x: auto;
            page-break-inside: avoid;
        }}

        pre code {{
            background: none;
            padding: 0;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            page-break-inside: avoid;
        }}

        th, td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }}

        th {{
            background-color: #f0f0f0;
            font-weight: bold;
        }}

        ul, ol {{
            margin: 10px 0;
            padding-left: 30px;
        }}

        li {{
            margin: 5px 0;
        }}

        hr {{
            border: none;
            border-top: 2px solid #ccc;
            margin: 30px 0;
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
        }}

        a:hover {{
            text-decoration: underline;
        }}

        @media print {{
            body {{
                background: white;
            }}

            h1, h2, h3, h4 {{
                page-break-after: avoid;
            }}

            p, table, pre {{
                page-break-inside: avoid;
            }}
        }}
    </style>
</head>
<body>
{content}
</body>
</html>"""

    return template

if __name__ == "__main__":
    # Read the markdown file
    with open('FINAL_PUBLICATION.md', 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert to HTML
    html_content = markdown_to_html(md_content)

    # Create complete HTML document
    full_html = create_html_document(html_content,
                                     "Enhanced Ensemble Methods for Wisconsin Breast Cancer Classification")

    # Write to file
    with open('FINAL_PUBLICATION.html', 'w', encoding='utf-8') as f:
        f.write(full_html)

    print("✓ Successfully converted FINAL_PUBLICATION.md to FINAL_PUBLICATION.html")
    print("\nTo convert to PDF:")
    print("1. Open FINAL_PUBLICATION.html in your web browser")
    print("2. Press Ctrl+P (Cmd+P on Mac) to print")
    print("3. Select 'Save as PDF' as the destination")
    print("4. Adjust settings if needed and save")
