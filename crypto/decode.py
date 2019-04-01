import cryptolib as edlib
import os.path
import sys


if len(sys.argv) < 4:
    print("Give me 3 params: password encode-file decoded-file")
    sys.exit()


key = sys.argv[1]
source_file = sys.argv[2]
target_file = sys.argv[3]


if os.path.isfile(source_file):
    decoded_content = edlib.read_encoded_file(key, source_file)
    edlib.save_content_to_file(target_file, decoded_content)
else:
    print("Invalid source file")
