"""Lab 8.3 - CS50 Shirtificate"""

# pip install fpdf2

from fpdf import FPDF


def main():
    """Main code"""
    name = input("Name: ")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(False)

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("arial", style="B", size=44)
    pdf.cell(center=True, text="CS50 Shirtificate\n", h=50)

    pdf.image("shirtificate.png", keep_aspect_ratio=True, x=10, y=70, w=pdf.epw)

    pdf.set_text_color(255, 255, 255)
    pdf.set_font("calibri", style="B", size=22)
    pdf.cell(center=True, text=f"{name} took CS50", h=250)

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
