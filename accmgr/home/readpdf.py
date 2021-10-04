from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

#function copied from internet
def convert_pdf_to_string(file_path):

	output_string = StringIO()
	with open(file_path, 'rb') as in_file:
	    parser = PDFParser(in_file)
	    doc = PDFDocument(parser)
	    rsrcmgr = PDFResourceManager()
	    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
	    interpreter = PDFPageInterpreter(rsrcmgr, device)
	    for page in PDFPage.create_pages(doc):
	        interpreter.process_page(page)

	return(output_string.getvalue())

#function copied from internet
def convert_title_to_filename(title):
    filename = title.lower()
    filename = filename.replace(' ', '_')
    return filename

#function copied from internet
def split_to_title_and_pagenum(table_of_contents_entry):
    title_and_pagenum = table_of_contents_entry.strip()
    
    title = None
    pagenum = None
    
    if len(title_and_pagenum) > 0:
        if title_and_pagenum[-1].isdigit():
            i = -2
            while title_and_pagenum[i].isdigit():
                i -= 1

            title = title_and_pagenum[:i].strip()
            pagenum = int(title_and_pagenum[i:].strip())
        
    return title, pagenum

#function written by me
def read_and_tell(file_path):
    d = dict()
    content_string=convert_pdf_to_string(file_path)

    matches = ["This is a system generated receipt", "PAYMENT RECEIPT", "GOODS AND SERVICES TAX"]

    if all(x in content_string for x in matches):
        print("Yes, It's a challan receipt.")
        if content_string.splitlines(True)[0].split(':')[0].strip()=="CPIN":
            d['CPIN'] = content_string.splitlines(True)[0].split(':')[1].strip()
        if content_string.splitlines(True)[4].split(':')[0].strip()=="GSTIN":
            d['GSTIN'] = content_string.splitlines(True)[4].split(':')[1].strip()
    else:
        print("No, It's not a challan receipt.")
    
    return d
  
