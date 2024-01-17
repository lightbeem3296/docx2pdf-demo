import os
import sys
from pathlib import Path

from docx2pdf import convert

CUR_DIR = str(Path(__file__).parent.absolute())
os.chdir(CUR_DIR)

if len(sys.argv) == 3:
    src_path,dst_path = sys.argv[1].strip(), sys.argv[2].strip()
    src_path, dst_path = os.path.abspath(src_path), os.path.abspath(dst_path)
    convert(src_path, dst_path)
else:
    print("usage: <path to bin> <word file path> <pdf file path>")
