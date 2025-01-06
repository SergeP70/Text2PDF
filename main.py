# Text to PDF
import glob
from pathlib import Path
from fpdf import FPDF


filepaths = glob.glob("files/*.txt")
pdf = FPDF(orientation='P', unit='mm', format='A4')

for filepath in filepaths:
    # Get the filename without the extension
    filename = Path(filepath).stem

    # Get the content of the text file
    with open(filepath, 'r') as file:
        content = file.read()

    pdf.add_page()

    # Header
    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=0, h=16, text=filename.title(), align='L', new_x='LMARGIN', new_y='NEXT')

    # Body
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, text=content)

pdf.output("output/animals.pdf")
