import sys 

_HEADER_SIZE = 16
_ZERO_INTERVAL = 500
_INTERVAL_SIZE = 8
_OUTPUT_FILE_SIZE = 8000000

write_data = ["00000000"] * int(_OUTPUT_FILE_SIZE/4)
with open(sys.argv[1], mode="r") as f:
    read_data = f.read()
    read_data_div =  read_data.split()

    read_iq_data = read_data_div[_HEADER_SIZE:]

for i in range(int(len(read_iq_data)/_ZERO_INTERVAL)):
    if i==0:
        stt_index_write = i*_ZERO_INTERVAL
    else:
        stt_index_write = i*(_ZERO_INTERVAL+_INTERVAL_SIZE)
    end_index_write = stt_index_write + _ZERO_INTERVAL
    stt_index_read = i*_ZERO_INTERVAL
    end_index_read = (i+1)*_ZERO_INTERVAL

    print(stt_index_write)

    write_data[stt_index_write:end_index_write] = \
            read_iq_data[stt_index_read:end_index_read]

with open(sys.argv[2], mode="wb") as f:
    for i in range(int(_OUTPUT_FILE_SIZE/4)):
        write_data_int = int(write_data[i], 16)
        write_data_hex = write_data_int.to_bytes(4,'big')
        #write_data_bin = bin(write_data_int)
        f.write(write_data_hex)