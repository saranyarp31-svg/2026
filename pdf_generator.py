from fpdf import FPDF

def create_pdf(tamil_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, tamil_text)

    file_path = "Tamil_Translation.pdf"
    pdf.output(file_path)
    return file_path
