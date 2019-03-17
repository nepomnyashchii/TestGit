
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


def do_work():
    with open('1.txt', 'r') as f:
        content = f.read()

        encoded = encode("y", content)
        with open('encoded.txt', 'a') as af:
            af.write(encoded)

        decoded = decode("y", encoded)
        print(decoded)
        with open('decoded.txt', 'a') as df:
            df.write(decoded)


do_work()
