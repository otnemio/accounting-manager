from datetime import date, datetime
import pytz
import hashlib
from pathlib import Path
from .readpdf import *
from .models import GST_Challan
 
#function copied from internet
def hash_file(filename):
    h_sha256 = hashlib.sha256()
    with open(filename,'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024) 
            h_sha256.update(chunk)
    return h_sha256.hexdigest()

#function written by me
def read_files_in_dir(dir_path):
    for pdf_path in Path(dir_path).glob("*.pdf"):
        challan = read_and_tell(pdf_path)
        if challan:
            # naive datetime
            dt=datetime.strptime(challan['Deposit Date']+' '+challan['Deposit Time'], "%d/%m/%Y %H:%M:%S")
            # add proper timezone
            pst=pytz.timezone('Asia/Kolkata')
            dt=pst.localize(dt)

            fh=hash_file(pdf_path)
            chln = GST_Challan(CPIN=challan['CPIN'],
            GSTIN=challan['GSTIN'],
            DateTimeOfDeposit=dt,
            FileHash=fh)

            chln.save()

            print(challan['GSTIN'])
            print(fh)
