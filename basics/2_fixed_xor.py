

def fixed_xor(first_buf, second_buf):
    unhex1 = bytes.fromhex(first_buf)
    unhex2 = bytes.fromhex(second_buf)
    return bytes(byte1 ^ byte2 for byte1, byte2 in zip(unhex1, unhex2)).hex()

if __name__ == '__main__':
    answer = fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
    if answer == "746865206b696420646f6e277420706c6179":
        print("Okay")
