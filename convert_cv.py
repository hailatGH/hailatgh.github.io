import datetime
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

def convert_cv_to_pdf():
    today = datetime.datetime.now().strftime("%b_%d_%Y").upper()
    pdf_filename = f"{today}.pdf"
    
    try:
        with open("CV.md", "r", encoding="utf-8") as f:
            md_content = f.read()
    except FileNotFoundError:
        print("Error: CV.md not found in the current directory.")
        return

    # Convert Markdown to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['extra']
    )
    
    # Wrap HTML with proper structure
    html_doc = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Hailemichael Atrsaw Tibebu - DevOps Engineer CV</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Professional CV CSS styling
    css_content = """
    @page {
        size: A4;
        margin: 2cm 2.5cm;
    }
    
    body {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 9.5pt;
        line-height: 1.35;
        color: #222;
        text-align: justify;
        hyphens: auto;
    }
    
    h1 {
        font-size: 20pt;
        font-weight: bold;
        color: #000;
        text-align: center;
        margin-top: 0;
        margin-bottom: 0.15em;
        border-bottom: 2.5px solid #000;
        padding-bottom: 0.25em;
        letter-spacing: 0.5px;
    }
    
    h1 + p {
        text-align: center;
        margin-top: 0.4em;
        margin-bottom: 0.25em;
    }
    
    h2 {
        font-size: 12.5pt;
        font-weight: bold;
        color: #000;
        margin-top: 0.9em;
        margin-bottom: 0.45em;
        border-bottom: 1.5px solid #444;
        padding-bottom: 0.15em;
        page-break-after: avoid;
    }
    
    h3 {
        font-size: 10.5pt;
        font-weight: bold;
        color: #111;
        margin-top: 0.65em;
        margin-bottom: 0.3em;
        page-break-after: avoid;
    }
    
    p {
        margin-bottom: 0.35em;
        text-align: justify;
        orphans: 3;
        widows: 3;
    }
    
    ul {
        display: block;
        margin-left: 0;
        margin-bottom: 0.6em;
        margin-top: 0.35em;
        padding-left: 1.5em;
        list-style-type: disc;
        list-style-position: outside;
    }
    
    li {
        display: list-item;
        text-align: justify;
        margin-bottom: 0.4em;
        margin-top: 0;
        padding-left: 0.3em;
        line-height: 1.4;
        orphans: 2;
        widows: 2;
        page-break-inside: avoid;
        white-space: normal;
    }
    
    li::marker {
        font-size: 12pt;
        font-weight: bold;
        color: #000;
    }
    
    /* Force line breaks after each list item */
    li::after {
        content: "";
        display: block;
        height: 0;
        clear: both;
    }
    
    strong {
        font-weight: bold;
        color: #000;
    }
    
    em {
        font-style: italic;
        color: #333;
    }
    
    a {
        color: #0066cc;
        text-decoration: none;
    }
    
    a:hover {
        text-decoration: underline;
    }
    
    code {
        font-family: 'Courier New', 'Consolas', monospace;
        background-color: #f5f5f5;
        padding: 1px 3px;
        font-size: 8.5pt;
        border-radius: 2px;
    }
    
    /* Prevent page breaks inside project sections */
    h3 + ul {
        page-break-inside: avoid;
    }
    """
    
    # Configure fonts
    font_config = FontConfiguration()
    
    # Generate PDF
    html = HTML(string=html_doc, base_url=".")
    css = CSS(string=css_content, font_config=font_config)
    html.write_pdf(pdf_filename, stylesheets=[css], font_config=font_config)
    
    print(f"✓ Successfully converted CV.md to {pdf_filename}")

if __name__ == "__main__":
    convert_cv_to_pdf()
