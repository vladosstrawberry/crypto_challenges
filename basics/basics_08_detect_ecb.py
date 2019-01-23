import base64



def detect(data, key_size):
    blocks = [data[i: i+ key_size] for i in range(0, len(data), key_size)]
    blocks_seen = set()

    for block in blocks:
        if block in blocks_seen:
            return True
        blocks_seen.add(block)
    return False

def detect_ecb(data, key_size):
    found = False
    unbased_data = [base64.b64decode(dat) for dat in data.split()]
    for i in range(len(unbased_data)):
        if detect(unbased_data[i], key_size):
            print("Found! index: " + str(i)  + "\nstring : "+ str(unbased_data[i]))
            found = True
    if not found:
        print("Not found")



if __name__ == '__main__':
    with open("08_file") as f:
        detect_ecb(f.read(), 16)