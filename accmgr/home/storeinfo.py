import hashlib
from pathlib import Path
from readpdf import *

h = hashlib.sha256()

for txt_path in Path(".").glob("*.pdf"):
  print(read_and_tell(txt_path))
