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


def encode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string


def decode(key, string):
    decoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        decoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        decoded_chars.append(decoded_c)
    decoded_string = ''.join(decoded_chars)
    return decoded_string


def read_content_from_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def save_content_to_file(file_name, text):
    with open(file_name, 'a') as f:
        f.write(text)


def read_encoded_file(file_name):
    encoded = read_content_from_file(file_name)
    return decode(key, encoded)


if os.path.isfile(source_file):
    decoded_content = read_encoded_file(source_file)
    save_content_to_file(target_file, decoded_content)
else:
    print("Invalid source file")
