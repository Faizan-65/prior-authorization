# Merge multiple files(img, docx, pdfs) in single pdf

from PyPDF2 import PdfMerger
from PIL import Image
from docx2pdf import convert
from fpdf import FPDF
import os

def docx_to_pdf(docx_file, output_pdf):
    convert(docx_file, output_pdf)

def image_to_pdf(image_path, output_path):
    pdf = FPDF()
    image = Image.open(image_path)
    pdf.add_page()
    pdf.image(image_path, 0, 0, pdf.w, 0)
    pdf.output(output_path, "F")

def merge_files(files, output_pdf):
    merger = PdfMerger()
    for file in files:
        if file.endswith(".pdf"):
            merger.append(file)
        elif file.endswith(".docx"):
            temp_pdf = file.replace(".docx", ".temp.pdf")
            docx_to_pdf(file, temp_pdf)
            merger.append(temp_pdf)
            os.remove(temp_pdf)
        elif file.lower().endswith(('.png', '.jpg', '.jpeg')):
            temp_pdf = file.replace(file.split('.')[-1], "temp.pdf")
            image_to_pdf(file, temp_pdf)
            merger.append(temp_pdf)
            os.remove(temp_pdf)
    merger.write(output_pdf)
    merger.close()

filepath_pa_form = "/Users/dev/Desktop/Data Product/Prior Authorization/Sample PA Request PDFs/Filled PA Forms/Aetna PA-1.pdf"
filepath_diagnostic_report = "/Users/dev/Desktop/Data Product/Prior Authorization/Sample PA Request PDFs/Diagnostic Reports/Diagnostic Report-1 copy 1.docx"
filepath_patient_history = "/Users/dev/Desktop/Data Product/Prior Authorization/Sample PA Request PDFs/Patient History Documents/Patient History copy 1.docx"
filepath_rationale = "/Users/dev/Desktop/Data Product/Prior Authorization/Sample PA Request PDFs/Rationale Letters/Rationale Letter 1.docx"

# List your files here
files_to_merge = [filepath_pa_form, filepath_diagnostic_report, filepath_patient_history, filepath_rationale]
output_file = "merged_output.pdf"

merge_files(files_to_merge, output_file)
print(f"All files have been merged into {output_file}")
