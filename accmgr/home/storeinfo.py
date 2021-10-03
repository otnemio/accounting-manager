import hashlib
from pathlib import Path
from readpdf import *
 
#function copied from internet
def hash_file(filename):
    h_sha256 = hashlib.sha256()
    with open(filename,'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024) 
            h_sha256.update(chunk)
    return h_sha256.hexdigest()

for txt_path in Path(".").glob("*.pdf"):
  print(read_and_tell(txt_path))
  print(hash_file(txt_path))
