import binascii

def score(string):
    dictionary = {"E": 12, "T":11, "A":10, "O":9, "I":8, "N":7, " ":6, "S":5, "H":4, "R":3, "D":2, "L":1, "U":0}
    score = 0;
    for i in string:
        if i.upper() in "ETAOIN SHRDLU":
            score += dictionary[i.upper()]
    return score

def decode(string):
    nums = binascii.unhexlify(string)
    strings = (''.join(chr(num ^ key) for num in nums) for key in range(256))
    ret_string = max(strings, key=lambda s: score(s));
    return (ret_string, score(ret_string))

if __name__ == '__main__':
    answer = decode("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")[0]
    print(answer)
