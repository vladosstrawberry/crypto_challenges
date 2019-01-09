
def repeating_key_xor(data, key):
    output = ""
    for block in range(0, len(data), len(key)):
        for d_char, k_char in zip(data[block:block+len(key)], key):
            output += "{0:02x}".format(ord(d_char) ^ ord(k_char))
    return output

if __name__ == '__main__':
    data = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
    key = "ICE"
    result_value = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""
    print(repeating_key_xor(data, key))
    if repeating_key_xor(data, key) == result_value:
        print("yes")

