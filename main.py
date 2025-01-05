# Text to PDF
import glob
from pathlib import Path
from fpdf import FPDF

filepath = glob.glob("files/*")
pdf = FPDF(orientation='P', unit='mm', format='A4')

for file in filepath:
    filename = Path(file).stem
    print(filename)
    pdf.add_page()

    # Header
    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=0, h=12, text=filename, align='L', new_x='LMARGIN', new_y='NEXT')


pdf.output("output/animals.pdf")




