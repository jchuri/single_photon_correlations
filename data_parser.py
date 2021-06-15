
def seperate_data(data):
    timestamp = data & 0x3FFFFFF
    ch = data >> 26 & 0x0F
    cleared = data >> 31
    chs = [ch & i for i in (0x1, 0x2, 0x4, 0x8)]
    return (timestamp, cleared, chs)

def checkchannel(chs, channel_num):
    for ch in chs:
        if ch == channel_num:
            return True
    return False

def collect_data(datastream):
    chs = [[data[0] for data in datastream if checkchannel(data[2], i**2)] for i in range(1,5)]
    return chs

def little_endian_to_big_endian(d):
    return int(bin(int(d,16))[2:].zfill(32)[::-1], 2)

def convert_to_usable_data(in_file, out_file):
    with open(in_file, "r") as f:
        data = [little_endian_to_big_endian(d) for d in f.readlines()]
    with open(out_file, "w") as f:
        for i in data:
            f.write(str(i) + "\n")