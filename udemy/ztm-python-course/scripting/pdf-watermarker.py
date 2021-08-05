import PyPDF2
import sys

from PyPDF2.pdf import PdfFileReader, PdfFileWriter
import os
import sys

# everything other than the name of the script
# allows user to input as many pdfs as they want watermarked
try:
    watermark = sys.argv[1]
    inputs = sys.argv[2:]
except IndexError:
    print('Please provide a watermark pdf and files to add it to')
    sys.exit()


# Will add provided watermark to each individual page of a file
# then create a new file with said watermark
def pdf_watermarker(file, watermark):
    output = PdfFileWriter()
    pdf_file = PdfFileReader(open(file, 'rb'))
    for i in range(pdf_file.getNumPages()):
        page = pdf_file.getPage(i)
        page.mergePage(watermark)
        output.addPage(page)

    with open(f'{os.path.splitext(file)[0]}-wtr.pdf', 'wb') as w:
        output.write(w)


# Gets the reader version of the watermark and calls the watermark
# function for each file provided
def watermark_list(pdf_list, watermark):
    watermark_file = PdfFileReader(open(watermark, 'rb'))
    for file in pdf_list:
        pdf_watermarker(file, watermark_file.getPage(0))


watermark_list(inputs, watermark)
