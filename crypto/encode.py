import cryptolib as edlib
import os.path
import sys as sss

params = sss.argv

if len(params) < 4:
    print("Give me 3 params: password decoded-file encode-file")
    sss.exit()


key = params[1]
source_file = params[2]
target_file = params[3]


if os.path.isfile(source_file):
    content = edlib.read_content_from_file(source_file)
    edlib.save_encoded_file(key, target_file, content)
else:
    print("Invalid source file")
