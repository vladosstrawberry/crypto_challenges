from itertools import combinations
from base64 import b64decode

CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}


def get_english_score(input_bytes):
    score = 0
    for byte in input_bytes:
        score += CHARACTER_FREQ.get(chr(byte).lower(), 0)
    return score

def singlechar_xor(input_bytes, key_value):
    output = b''
    for char in input_bytes:
        output += bytes([char ^ key_value])
    return output

def singlechar_xor_brute_force(ciphertext):
    candidates = []
    for key_candidate in range(256):
        plaintext_candidate = singlechar_xor(ciphertext, key_candidate)
        candidate_score = get_english_score(plaintext_candidate)
        result = {
            'key': key_candidate,
            'score': candidate_score,
            'plaintext': plaintext_candidate
        }
        candidates.append(result)
    return sorted(candidates, key=lambda c: c['score'], reverse=True)[0]



def repeating_key_xor(plaintext, key):
    ciphertext = b''
    i = 0
    for byte in plaintext:
        ciphertext += bytes([byte ^ key[i]])
        i = i + 1 if i < len(key) - 1 else 0
    return ciphertext

def hamming_distance(binary_seq_1, binary_seq_2):
    assert len(binary_seq_1) == len(binary_seq_2)
    dist = 0
    for bit1, bit2 in zip(binary_seq_1, binary_seq_2):
        diff = bit1 ^ bit2
        dist += sum([1 for bit in bin(diff) if bit == '1'])
    return dist


def break_repeating_key_xor(binary_data):
    normalized_distances = {}
    for key_size in range(2, 41):
        chunks = [binary_data[i:i + key_size] for i in range(0, len(binary_data), key_size)][:4]
        distance = 0
        pairs = combinations(chunks, 2)
        for (x, y) in pairs:
            distance += hamming_distance(x, y)
        distance /= 6
        normalized_distance = distance / key_size
        normalized_distances[key_size] = normalized_distance
    possible_key_sizes = sorted(normalized_distances, key=normalized_distances.get)[:3]
    possible_plaintexts = []
    for d in possible_key_sizes:
        key = b''
        for i in range(d):
            block = b''
            for j in range(i, len(binary_data), d):
                block += bytes([binary_data[j]])
            key += bytes([singlechar_xor_brute_force(block)['key']])
        possible_plaintexts.append((repeating_key_xor(binary_data, key), key))
    return max(possible_plaintexts, key=lambda k: get_english_score(k[0]))


def main():
    with open("file6") as input_file:
        data = b64decode(input_file.read())
    result = break_repeating_key_xor(data)
    print("Key =", result[1].decode())
    print("---------------------------------------")
    print(result[0].decode().rstrip())


if __name__ == "__main__":
    main()