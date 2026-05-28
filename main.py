from pathlib import Path
from datetime import datetime

def generate_pdf_weasyprint():
    try:
        from weasyprint import HTML, CSS

        now = datetime.now()
        month = now.strftime("%B").upper()  # JANUARY, FEBRUARY, etc.
        day = now.strftime("%d")  # 01, 02, ..., 31
        year = now.strftime("%Y")  # 2026
        filename = f"{month}_{day}_{year}_CV.pdf"
        
        current_dir = Path(__file__).parent
        html_file = current_dir / "src" / "main.html"
        output_file = current_dir / "docs" / filename
        
        print("Generating SINGLE PAGE PDF using weasyprint...")
        print(f"Input: {html_file}")
        print(f"Output: {output_file}")
        
        css_style = '''
            @page {
                size: 210mm 1200mm;  /* A4 width, auto height */
                margin: 1cm;
            }
            body {
                margin: 0;
                padding: 0;
            }
        '''
        
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

def main():
    print("=" * 60)
    print("CV PDF Generator")
    print("=" * 60)
    print()
    generate_pdf_weasyprint()
    print()
    print("=" * 60)
    print("Success! Your CV PDF is ready.")
    print("=" * 60)
    print()

if __name__ == "__main__":
    main()
