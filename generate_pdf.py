#!/usr/bin/env python3
"""
Generate PDF from HTML CV
Uses weasyprint library for high-quality HTML/CSS to PDF conversion
"""

import os
from pathlib import Path

def generate_pdf_weasyprint(single_page=False):
    """Generate PDF using weasyprint (best quality)"""
    try:
        from weasyprint import HTML, CSS
        
        # Get the current directory
        current_dir = Path(__file__).parent
        html_file = current_dir / "index.html"
        
        if single_page:
            output_file = current_dir / "CV_single_page.pdf"
            print("Generating SINGLE PAGE PDF using weasyprint...")
            print(f"Input: {html_file}")
            print(f"Output: {output_file}")
            
            # Create a page that automatically fits content height
            # Use A4 width but let height be determined by content
            css_style = '''
                @page {
                    size: 210mm auto;  /* A4 width, auto height */
                    margin: 1cm;
                }
                body {
                    margin: 0;
                    padding: 0;
                }
            '''
            
        else:
            output_file = current_dir / "CV.pdf"
            print("Generating PDF using weasyprint...")
            print(f"Input: {html_file}")
            print(f"Output: {output_file}")
            
            css_style = '@page { size: A4; margin: 1.5cm; }'
        
        # Convert HTML to PDF
        HTML(filename=str(html_file)).write_pdf(
            str(output_file),
            stylesheets=[CSS(string=css_style)]
        )
        
        print(f"✓ PDF generated successfully: {output_file}")
        return True
        
    except ImportError:
        print("✗ weasyprint not installed")
        return False
    except Exception as e:
        print(f"✗ Error with weasyprint: {e}")
        return False


def generate_pdf_pdfkit():
    """Generate PDF using pdfkit (requires wkhtmltopdf)"""
    try:
        import pdfkit
        
        current_dir = Path(__file__).parent
        html_file = current_dir / "index.html"
        output_file = current_dir / "CV.pdf"
        
        print("Generating PDF using pdfkit...")
        print(f"Input: {html_file}")
        print(f"Output: {output_file}")
        
        options = {
            'page-size': 'A4',
            'margin-top': '1.5cm',
            'margin-right': '1.5cm',
            'margin-bottom': '1.5cm',
            'margin-left': '1.5cm',
            'encoding': "UTF-8",
            'enable-local-file-access': None
        }
        
        pdfkit.from_file(str(html_file), str(output_file), options=options)
        
        print(f"✓ PDF generated successfully: {output_file}")
        return True
        
    except ImportError:
        print("✗ pdfkit not installed")
        return False
    except Exception as e:
        print(f"✗ Error with pdfkit: {e}")
        return False


def generate_pdf_playwright():
    """Generate PDF using playwright (requires playwright)"""
    try:
        from playwright.sync_api import sync_playwright
        
        current_dir = Path(__file__).parent
        html_file = current_dir / "index.html"
        output_file = current_dir / "CV.pdf"
        
        print("Generating PDF using playwright...")
        print(f"Input: {html_file}")
        print(f"Output: {output_file}")
        
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f'file://{html_file.absolute()}')
            page.pdf(
                path=str(output_file),
                format='A4',
                margin={
                    'top': '1.5cm',
                    'right': '1.5cm',
                    'bottom': '1.5cm',
                    'left': '1.5cm'
                },
                print_background=True
            )
            browser.close()
        
        print(f"✓ PDF generated successfully: {output_file}")
        return True
        
    except ImportError:
        print("✗ playwright not installed")
        return False
    except Exception as e:
        print(f"✗ Error with playwright: {e}")
        return False


def main():
    import sys
    
    # Check for single-page flag
    single_page = '--single-page' in sys.argv or '-s' in sys.argv
    
    print("=" * 60)
    if single_page:
        print("CV PDF Generator - SINGLE PAGE MODE")
    else:
        print("CV PDF Generator - MULTI PAGE MODE")
    print("=" * 60)
    print()
    
    # Try different methods in order of preference
    methods = [
        ("weasyprint", lambda: generate_pdf_weasyprint(single_page)),
        ("pdfkit", generate_pdf_pdfkit),
        ("playwright", generate_pdf_playwright),
    ]
    
    for method_name, method_func in methods:
        if method_func():
            print()
            print("=" * 60)
            print("Success! Your CV PDF is ready.")
            if not single_page:
                print()
                print("TIP: Want a single-page PDF?")
                print("Run: poetry run python generate_pdf.py --single-page")
            print("=" * 60)
            return
    
    # If all methods fail, show installation instructions
    print()
    print("=" * 60)
    print("No PDF library found. Please install one of the following:")
    print("=" * 60)
    print()
    print("Option 1 (Recommended): weasyprint")
    print("  pip install weasyprint")
    print()
    print("Option 2: pdfkit (requires wkhtmltopdf)")
    print("  pip install pdfkit")
    print("  sudo apt-get install wkhtmltopdf  # On Ubuntu/Debian")
    print()
    print("Option 3: playwright")
    print("  pip install playwright")
    print("  playwright install chromium")
    print()


if __name__ == "__main__":
    main()
