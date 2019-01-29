

def addpadd(data, blocksize):
    data   = data.encode()
    op = len(data) % blocksize
    if op:
        count = blocksize - op
        data = data + (count.to_bytes(1, 'big') * count)
    return data.decode()

if __name__ == '__main__':
    got = addpadd("YELLOW SUBMARINE", 20)
    print(got)
    print(got.encode())

    

