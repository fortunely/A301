# -*- coding: utf-8 -*-
import sys


class CanFrameInfo:
    def __init__(self):
        self.recevie_time = 0
        self.duration = self.recevie_time
        self.can_id = 0
        self.can_length = 0
        self.can_data = []
        self.can_type = "Rx"
        self.line_number = 0


    def show(self):
        print("------------------------"),
        print(self.__class__.__name__)
        print("------------------------")
        print("received time: %f"%self.recevie_time, end=", ")
        print("duration: %fS"%self.duration, end=", ")
        print("can id: %x"%self.can_id, end=", "),
        print("can type: %s"%self.can_type, end=", ")
        print("can length: %d"%self.can_length, end=", ")
        print("can data: [", end="")
        for data in self.can_data:
            print(data, end=" ")
        print("]")


    def filter_duration(self, filterValue):
        if self.duration >= filterValue:
            print("can received time: %f"%self.recevie_time, end=", ")
            print("duration: %fS" % self.duration, end=", ")


def can_data_parse_beam(can_frame_list):
    # file = open("G:\\willing\\A301\\测试文档\\漠河 远近光的CAN报文丢帧\\20191214170000_20191214180000.asc") # 远近光灯报文丢失
    file = open("G:\\willing\A301\测试文档\\漠河 黑屏\\20191216093000_20191216100000\\20191216093000_20191216100000.asc") # 黑屏
    filter_string = " 380 "

    old_receive_time = 0

    line_str = file.readline().strip()
    n = 100000000000
    # n = 1000
    i = 0

    while line_str and n > 0:
        ## parase a line text
        if filter_string in line_str:
            # print(line_str)
            can_frame = CanFrameInfo()

            line_list = line_str.split(" ")
            # print(line_list)
            # print("length of line text: %d"%len(line_list))

            split_str_id = 0
            # received time
            while not line_list[split_str_id]:
                split_str_id += 1

            can_frame.recevie_time = float(line_list[split_str_id])
            split_str_id += 1

            # duration - by calculation
            if i > 0:
                can_frame.duration = can_frame.recevie_time - old_receive_time

            old_receive_time = can_frame.recevie_time

            # filter "3" or “1” following received time
            split_str_id += 1

            # can id
            while not line_list[split_str_id]:
                split_str_id += 1

            can_frame.can_id = int(line_list[split_str_id], 16)
            split_str_id += 1

            # can type
            while not line_list[split_str_id]:
                split_str_id += 1

            can_frame.can_type = line_list[split_str_id]
            split_str_id += 1

            #filter char "d"
            while not line_list[split_str_id]:
                split_str_id += 1

            if line_list[split_str_id] == "d":
                split_str_id += 1

            # can length
            while not line_list[split_str_id]:
                split_str_id += 1

            # print(line_list[split_str_id])
            can_frame.can_length = int(line_list[split_str_id])
            split_str_id += 1

            # can data
            while split_str_id < len(line_list) and line_list[split_str_id]:
                can_frame.can_data.append(int(line_list[split_str_id] , 16))
                split_str_id += 1

            # line number
            can_frame.line_number = i

            can_frame_list.append(can_frame)
            # can_frame.show()
            # print("index: %d"%i, end=" ")
            # print("duration: %f"%can_frame.duration)

        line_str = file.readline().strip()
        n -= 1
        i += 1

    file.close()


def can_data_filter_duration(list, duration_min):
    print("can_data_filter_duration begin...")
    print("can id = %x"%can_frame_list[0].can_id)
    i = 0
    while i < len(list):
        data = list[i]
        if data.duration >= duration_min:
            print("line number = %d"%data.line_number, end=", ")
            print("index = %d" % i, end=", ")
            print("duration = %f"%(data.duration * 1000),"ms")

        i += 1

    print("can_data_filter_duration end.")


can_frame_list = []
can_data_parse_beam(can_frame_list)
can_data_filter_duration(can_frame_list, 0.01)
