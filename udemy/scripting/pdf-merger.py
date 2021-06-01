import PyPDF2
import sys

# everything other than the name of the script
# allows user to input as many pdfs as they want merged
inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('pdfs/merged.pdf')


pdf_combiner(inputs)
