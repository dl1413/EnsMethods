# Publication Output Guide

This guide explains how to generate publication outputs for the "Enhanced Ensemble Methods for Wisconsin Breast Cancer Classification" research project.

## Overview

The publication system automatically generates multiple output formats from the source markdown file (`FINAL_PUBLICATION.md`):

1. **Standard HTML** - For web viewing and sharing
2. **PDF-Ready HTML** - Optimized for PDF conversion with print styles
3. **Complete Project Publication** - Comprehensive HTML with all content

## Quick Start

### Generate All Publication Outputs

Simply run the publishing script:

```bash
python3 publish_outputs.py
```

This will automatically generate:
- `FINAL_PUBLICATION.html` - Standard web version
- `FINAL_PUBLICATION_PDF_READY.html` - PDF-optimized version
- `COMPLETE_PROJECT_PUBLICATION.html` - Complete publication

### Generate from Custom Markdown File

```bash
python3 publish_outputs.py path/to/your/file.md
```

## Output Formats

### 1. Standard HTML (`FINAL_PUBLICATION.html`)

**Purpose**: Web viewing, sharing via email or web hosting

**Features**:
- Responsive design for different screen sizes
- Optimized for on-screen reading
- Standard web typography
- Interactive links and navigation

**Use Cases**:
- Viewing in web browser
- Sharing with colleagues
- Hosting on personal website
- Email attachments

### 2. PDF-Ready HTML (`FINAL_PUBLICATION_PDF_READY.html`)

**Purpose**: Converting to PDF via browser print function

**Features**:
- A4 page size optimization
- Print-specific CSS styling
- Page break control
- PDF-optimized typography (11pt base font)
- Academic publication formatting

**Use Cases**:
- Generating final PDF for submission
- Archival purposes
- Print publication
- Formal distribution

### 3. Complete Project Publication (`COMPLETE_PROJECT_PUBLICATION.html`)

**Purpose**: Comprehensive standalone document

**Features**:
- All project content in single file
- Self-contained (no external dependencies)
- Professional academic styling
- Complete metadata and attribution

**Use Cases**:
- Project archiving
- Complete project documentation
- Offline viewing
- Institutional repository submission

## Converting HTML to PDF

### Method 1: Browser Print (Recommended)

1. Open `FINAL_PUBLICATION_PDF_READY.html` in your web browser
   - Chrome, Firefox, Edge, or Safari

2. Open Print Dialog:
   - **Windows/Linux**: Press `Ctrl + P`
   - **Mac**: Press `Cmd + P`

3. Configure Print Settings:
   - **Destination**: "Save as PDF" or "Microsoft Print to PDF"
   - **Paper size**: A4
   - **Margins**: Default
   - **Scale**: 100%
   - **Options**:
     - ✓ Background graphics
     - ✓ Headers and footers (optional)

4. Click "Save" or "Print"

5. Save as: `Enhanced Ensemble Methods for Wisconsin Breast Cancer Classification.pdf`

### Method 2: Command Line (Advanced)

If you have `wkhtmltopdf` installed:

```bash
wkhtmltopdf FINAL_PUBLICATION_PDF_READY.html "Enhanced Ensemble Methods for Wisconsin Breast Cancer Classification.pdf"
```

Or using Chrome headless:

```bash
google-chrome --headless --disable-gpu --print-to-pdf="output.pdf" FINAL_PUBLICATION_PDF_READY.html
```

### Method 3: Python (weasyprint)

Install weasyprint:
```bash
pip install weasyprint
```

Convert:
```bash
weasyprint FINAL_PUBLICATION_PDF_READY.html "Enhanced Ensemble Methods for Wisconsin Breast Cancer Classification.pdf"
```

## Publication Statistics

The script automatically calculates and displays:
- Line count
- Word count
- Character count
- Number of headers
- Number of code blocks
- Number of tables

Example output:
```
Publication Statistics:
Lines: 922
Words: 6,244
Characters: 47,601
Headers: 98
Code Blocks: 5
Tables: 24
```

## Workflow Integration

### Development Workflow

1. Edit source markdown: `FINAL_PUBLICATION.md`
2. Generate outputs: `python3 publish_outputs.py`
3. Review HTML: Open `FINAL_PUBLICATION.html` in browser
4. Generate PDF: Print `FINAL_PUBLICATION_PDF_READY.html` to PDF
5. Commit changes: `git add . && git commit -m "Update publication"`

### Automated Publishing

You can integrate the script into your CI/CD pipeline:

```yaml
# Example GitHub Actions workflow
name: Generate Publications
on: [push]
jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Generate outputs
        run: python3 publish_outputs.py
      - name: Upload artifacts
        uses: actions/upload-artifact@v2
        with:
          name: publications
          path: |
            FINAL_PUBLICATION.html
            FINAL_PUBLICATION_PDF_READY.html
            COMPLETE_PROJECT_PUBLICATION.html
```

## Customization

### Modifying Styles

Edit the CSS in `publish_outputs.py`:

```python
def create_html_document(content, title="Research Publication", pdf_ready=False):
    # Modify styles in the template string
    # Look for the <style> section
```

### Adding New Output Formats

Extend `generate_publication_outputs()`:

```python
def generate_publication_outputs(markdown_file='FINAL_PUBLICATION.md'):
    # Add your custom format generation here
    # Example: generate LaTeX, DOCX, etc.
```

### Custom Markdown Extensions

Modify `markdown_to_html()` to support additional markdown features:

```python
def markdown_to_html(md_text):
    # Add regex patterns for custom markdown syntax
    # Example: footnotes, citations, etc.
```

## File Structure

```
EnsMethods/
├── FINAL_PUBLICATION.md              # Source markdown (edit this)
├── publish_outputs.py                # Publication generator script
├── PUBLISHING_GUIDE.md               # This file
├── FINAL_PUBLICATION.html            # Generated: standard HTML
├── FINAL_PUBLICATION_PDF_READY.html  # Generated: PDF-ready HTML
├── COMPLETE_PROJECT_PUBLICATION.html # Generated: complete publication
└── Enhanced Ensemble Methods.pdf     # Manual: generated PDF
```

## Best Practices

### Source Control

- **Commit**: `FINAL_PUBLICATION.md` (source)
- **Commit**: `publish_outputs.py` (generator script)
- **Optional**: Generated HTML files (can be regenerated)
- **Commit**: Final PDF (for archival)

### Version Control

Add version information to your markdown:

```markdown
**Version:** 2.0 (Enhanced)
**Last Updated:** 2025-11-18
```

### Quality Checks

Before finalizing:
1. ✓ Run spell check on markdown
2. ✓ Verify all links work
3. ✓ Check table formatting
4. ✓ Review code blocks for syntax
5. ✓ Validate references and citations
6. ✓ Test PDF generation
7. ✓ Verify page breaks in PDF

## Troubleshooting

### HTML Not Rendering Properly

- Clear browser cache
- Try different browser
- Check for unclosed HTML tags in generated output

### PDF Formatting Issues

- Ensure "Background graphics" is enabled in print settings
- Try different browsers (Chrome usually works best)
- Adjust margins in print dialog
- Use `FINAL_PUBLICATION_PDF_READY.html` (not standard HTML)

### Script Errors

```bash
# Check Python version (requires 3.6+)
python3 --version

# Verify file exists
ls -la FINAL_PUBLICATION.md

# Run with verbose error messages
python3 -u publish_outputs.py
```

### Missing Dependencies

The script uses only Python standard library, no external dependencies needed!

## Advanced Features

### Metadata Injection

Add metadata to generated HTML:

```python
# In create_html_document()
<meta name="author" content="Derek Lankeaux">
<meta name="description" content="...">
<meta name="keywords" content="breast cancer, machine learning, ensemble methods">
```

### Accessibility

The generated HTML includes:
- Semantic HTML5 tags
- Proper heading hierarchy
- Alt text for tables
- High contrast ratios

### SEO Optimization

For web publication:
- Descriptive page titles
- Meta descriptions
- Semantic markup
- Proper heading structure

## Support

For issues or questions:
1. Check this guide
2. Review error messages
3. Verify Python version and file paths
4. Open issue on GitHub repository

## License

This publication system is part of the EnsMethods research project.
For educational and research purposes.

---

**Last Updated**: 2025-11-18
**Author**: Derek Lankeaux
**Institution**: Rochester Institute of Technology
