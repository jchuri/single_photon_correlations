import os.path
import os
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

def fix_overflow(channel_data): 
    size = len(channel_data)
    idx_list = [idx + 1 for idx, val in
            enumerate(channel_data) if val == 0]  
    res = [channel_data[i: j-1] for i, j in
        zip([0] + idx_list, idx_list + 
        ([size] if idx_list[-1] != size else []))]

    result = [j + (2**27 -1)*i for i, ch in enumerate(res) for j in ch]
    return result


def create_channels(file): 
    channels = get_channels(split_into_parts(from_little_endian_to_int(file)))

    if os.path.isdir("./channels"):
        pass
    else: 
        os.mkdir("./channels")
    for channel_num, ch in enumerate(channels):
        tmp = fix_overflow(ch)
        with open(f"./channels/ch{channel_num}.txt", "w") as f: 
            for i in tmp: 
                f.write(str(i) + "\n")

def extact_data(file): 
    tmp = "tmp.txt"
    os.system(f"xxd -c -4 -b -g -4 -p {file} > {tmp}")
    create_channels(tmp)


            

