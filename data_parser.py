
def from_little_endian_to_int(file):
    with open(file, 'r') as f: 
        x = [i.strip('\n') for i in f.readlines()]
    y = [bytearray.fromhex(i) for i in x]

    for i in y: 
        i.reverse()

    return [int(bytearray.hex(i), 16) for i in y]

def split_into_parts(data):
    x = [bin(i)[2:].zfill(32) for i in data]
    return [(i[0], i[1:5], int(i[5:],2)) for i in x]
    
def in_channel(data, ch_num):
    ch = 4 - ch_num
    if data[1][ch] == '1':
        return True
    elif data[0] == '1':
        return True
    else: 
        return False

def get_channels(data):
    return [[d[2] for d in data if in_channel(d, i)] for i in range(1,5)]