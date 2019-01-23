import base64

def hex_to_base64(hex_value):
    raw_bytes = bytes.fromhex(hex_value)
    print(raw_bytes)
    return base64.b64encode(raw_bytes).decode("utf-8")

if __name__ == '__main__':
    answer = hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
    if answer == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t":
        print("OKAY")
