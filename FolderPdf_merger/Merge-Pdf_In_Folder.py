import os
from PyPDF2 import  PdfMerger
# may need pip install PyPDF2
# set the directory containing the PDF files to merge in the input response
print("please enter the folder location \n")
input_value=input()
pdf_files = [f for f in os.listdir(input_value) if f.endswith('.pdf')]
pdf_merger =  PdfMerger()
for pdf in pdf_files:
    with open(os.path.join(input_value, pdf), 'rb') as file:
        pdf_merger.append(file)
with open("merged_file.pdf", 'wb') as file:
    pdf_merger.write(file)