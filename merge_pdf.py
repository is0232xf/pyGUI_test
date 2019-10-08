# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:44:23 2019

@author: FujiiChang
"""

# merge_pdf.py
from pathlib import Path
import PyPDF2

def merge_pdf_files(folder_path, file_path, is_reverse):
    # list of pdf in the directry
    pdf_dir = Path(folder_path)
    pdf_files = sorted(pdf_dir.glob("*.pdf"), reverse=is_reverse)

    # join pdf files to one file
    pdf_writer = PyPDF2.PdfFileWriter()
    for pdf_file in pdf_files:
        pdf_reader = PyPDF2.PdfFileReader(str(pdf_file))
        for i in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(i))

    # save
    with open(file_path, "wb") as f:
        pdf_writer.write(f)


if __name__ == "__main__":
    merge_pdf_files("./pdf_files", "test.pdf", False)