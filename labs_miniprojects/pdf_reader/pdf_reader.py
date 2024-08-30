import PyPDF2
fname = input("Enter File Directory: ")
if len(fname) < 1 : fname = 'test.pdf'

pdf_file = open(fname, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]    
    print(page.extract_text())

pdf_file.close()