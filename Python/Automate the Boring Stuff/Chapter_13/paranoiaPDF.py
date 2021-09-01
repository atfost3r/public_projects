#! python3
# paranoiaPDF.py - Walks through the every PDF in a folder and all the subfolders and
# creates an encrpyted version of the PDF using a password provided by the user via the commandline

import PyPDF2, os, re, sys

# Get password from command line
password = sys.argv[1]
path = os.getcwd()

# TODO: Set up os.walk()
for foldername, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith((".pdf", ".PDF")):
            print("Encrypting " + file + "...")
            pdf = open(os.path.join(foldername, file), "rb")
            pdf_reader = PyPDF2.PdfFileReader(pdf)
            pdf_writer = PyPDF2.PdfFileWriter()
            pdf_writer.encrypt(password)
            for page_num in range(pdf_reader.numPages):
                page_obj = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page_obj)
            file = re.sub(".pdf", "", file)
            new_pdf = open(os.path.join(foldername, file + "_encrypted.pdf"), "wb")
            pdf_writer.write(new_pdf)
            pdf.close
            new_pdf.close

# TODO: Test each file that succussfully encrypted
for folder, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith("encrypted.pdf"):
            pdf = open(os.path.join(folder, file), "rb")
            pdf_reader = PyPDF2.PdfFileReader(pdf)
            try:
                page_obj = pdf_reader.getPage(0)
            except PyPDF2.utils.PdfReadError:
                file = re.sub("_encrypted.pdf", "", file)
                print("Deleting %s..." % (os.path.join(folder, file)))
                os.remove(os.path.join(folder, file + ".pdf"))

# Save and close file

print("Done")
