import binascii

def decode(string):
    nums = binascii.unhexlify(string)
    strings = (''.join(chr(num ^ key) for num in nums) for key in range(256))
    return max(strings, key=lambda s: s.count(' '))

if __name__ == '__main__':
    answer = decode("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    print(answer)