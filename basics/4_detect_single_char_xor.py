import binascii


#       from  3d challenge

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

#    ---------------------------------------------------

def decode_all(data):
    max_score = 0
    max_strin = ""
    for i in range(len(data)):
        strin, score = decode(data[i])
        if score > max_score:
            max_score = score
            max_strin = strin
    return max_strin

def detect_single_char_xor(data):
    data_list = data.split()
    return decode_all(data_list)

if __name__ == '__main__':
    with open('file') as f:
        content = f.read();
    print(detect_single_char_xor(content))