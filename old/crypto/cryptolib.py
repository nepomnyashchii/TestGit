
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


def save_encoded_file(key, file_name, text):
    encoded = encode(key, text)
    save_content_to_file(file_name, encoded)


def read_encoded_file(key, file_name):
    encoded = read_content_from_file(file_name)
    return decode(key, encoded)
