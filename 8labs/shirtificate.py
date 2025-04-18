"""Lab 8.3 - CS50 Shirtificate"""

# pip install fpdf2

from fpdf import FPDF


# The 14 standard PDF fonts are
# Courier (Regular, Oblique, Bold, Bold Oblique),
# Helvetica (Regular, Oblique, Bold, Bold Oblique),
# Times (Roman, Italic, Bold, Bold Italic),
# Symbol, and
# ITC Zapf Dingbats


def main():
    """Main code"""
    name = input("Name: ")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(False)

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("helvetica", style="B", size=44)
    pdf.cell(center=True, text="CS50 Shirtificate\n", h=50)

    pdf.image("shirtificate.png", keep_aspect_ratio=True, x=10, y=70, w=pdf.epw)

    pdf.set_text_color(255, 255, 255)
    pdf.set_font("courier", style="B", size=22)
    pdf.cell(center=True, text=f"{name} took CS50", h=250)

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
