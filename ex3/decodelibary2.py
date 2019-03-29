
import sys
import os.path


# if (len(sys.argv) < 4):
#     print("Please provide 'key' source_file target_file arguments")
#     exit

if len(sys.argv) < 4:
    print("Give me 3 params: password encode-file decoded-file")
    sys.exit()


key = sys.argv[1]
source_file = sys.argv[2]
target_file = sys.argv[3]

# print('Sourse file:', source_file)
# print('Target file:', target_file)
# print('key:', key)

import decodelibrary

def read_encoded_file(file_name):
    encoded = read_content_from_file(file_name)
    return decode(key, encoded)
    
if os.path.isfile(source_file):
    decoded_content = read_encoded_file(source_file)
    save_content_to_file(target_file, decoded_content)
else:
    print("Invalid source file")