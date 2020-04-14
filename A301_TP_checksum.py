cmd_id = "0xF2"
byte1 = "0x00"
byte2 = "0x01"
byte3 = "0x80"
slave_addr = "0x34"

def get_i2c_data():
    # file = open("./tp/i2c_log_checksum_UPGRADE.txt")
    file = open("./tp/i2c_log_checksum.txt")
    i2c_data_128byte = []

    line_text = file.readline().strip()
    while line_text:
        if line_text:
            datas = line_text.split(" ")
            print(line_text)

            for t in datas:
                if t:
                    i2c_data_128byte.append(int(t, 16))

        line_text = file.readline().strip()

    i2c_data_128byte.insert(0, int(byte3, 16))
    i2c_data_128byte.insert(0, int(byte2, 16))
    i2c_data_128byte.insert(0, int(byte1, 16))
    i2c_data_128byte.insert(0, int(cmd_id, 16))

    HEAD = 3
    byte_idx = 0
    print("[")
    for data in i2c_data_128byte:
        if byte_idx == HEAD:
            print()
        print("%x"%data, end=", ")
        byte_idx += 1

    print("]")

    print(i2c_data_128byte)
    checksum = calcluate_checksum(i2c_data_128byte)
    print("checksum = %x"%checksum)
    file.close()


def calcluate_checksum(checksum_data):
    checksum = 0
    line_data_max_length = 15
    line_idx = 0

    print("calcluate_checksum")
    print("checksum_data: {")
    for t in checksum_data:
        # print(" %x"%t, end="")
        # if line_idx == line_data_max_length:
        #     print()
        #     line_idx = 0
        # else:
        #     line_idx += 1

        checksum += t
    print()
    print("}")

    checksum += 1
    return checksum


get_i2c_data()