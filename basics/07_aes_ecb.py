from Crypto.Cipher import AES
from base64 import b64decode

def decipher(data, key, mode):
    obj = AES.new(key, mode)
    return obj.decrypt(b64decode(data))


if __name__ == '__main__':
    key = "YELLOW SUBMARINE"
    with open("07_file") as f:
        print(decipher(f.read(), key, AES.MODE_ECB))