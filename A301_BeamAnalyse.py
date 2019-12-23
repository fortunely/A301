# -*- coding: utf-8 -*-
import sys
import os.path
from pathlib import Path

IP_280_50ms = "280"
IP_380_500ms = "380"

log_file_path_list = [
    # 长安提供
    r"F:\工作\A301\测试文档\漠河\远近光灯丢失\远近光突然熄灭_20191221\20191220165000_20191220172000.asc", #远近光突然熄灭_20191221
    r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191217\黑屏\20191216093000_20191216100000.asc",
    r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191220\远近光灯突然熄灭\20191220165000_20191220172000.asc",

    #荣乐提供
    r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191220\正常行驶\Bus Traffic201912201500 12-20-2019 4-59-56 pm.asc",
    r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191220\正常到出现灭灯\Bus Traffic201912201514 12-20-2019 5-14-37 pm.asc",
    r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191221\行驶正常\Bus Traffic201912211656 12-21-2019 4-56-12 pm.asc",
    r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191221\静态近光熄灭\Bus Traffic201912211916 12-21-2019 7-16-38 pm.asc",
    r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191221\静态正常\Bus Traffic201912211547 12-21-2019 3-47-58 pm.asc"
]

log_file_path = log_file_path_list[2]


filter_canid =  str(IP_280_50ms)
filter_time = 10#0.06 # unit: s
print("filter_canid = %s"%filter_canid)


class CanFrameInfo:
    def __init__(self):
        self.recevie_time = 0 # unit: s
        self.duration = self.recevie_time  # unit: s
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


def get_file_type(filepath):
    os.path.splitext(filepath)[0]

def convert_filepath_style_from_win_to_python(filepath):
    if not filepath.endswith(".asc"):
        print("%s is not a valid asc file."%filepath)
        return ""

    s1 = "\\" # \
    s2 = "\\\\" # \\

    if s1 in filepath:
        filepath.replace(s1, s2)
        return filepath
    else:
        print("%s is not a valid file path"%filepath)

        return ""


def can_data_parse_beam(can_frame_list):
    filepath = convert_filepath_style_from_win_to_python(log_file_path)
    if filepath == "":
        return

    print("Now parsing file %s ..."%filepath)
    file = open(filepath)

    filter_string = " " + filter_canid + " "

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

            line_list = line_str.split(" ") # split one line string by space character (" ")
            # print(line_list)
            # print("length of line text: %d"%len(line_list))

            #parase every filed of a line string, dont change the sequence of the fileds
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
            can_frame.line_number = i + 1

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

    if not list:
        print("list is null")
        return

    f = open("out.txt", "w") # open file for writing
    if not f:
        print("fail to open output file")
        return

    # print("can id = %x"%list[0].can_id)

    f.write("can id = %x \n"%list[0].can_id)
    f.write("Can frame list of duration >= %.2f ms:\n"%(duration_min * 1000))
    i = 0
    while i < len(list):
        data = list[i]
        if data.duration >= duration_min:
            f.write("line number = %d  "%data.line_number)
            f.write("index = %d  " % i)
            f.write("duration = %.2f ms"%(data.duration * 1000))
            f.write("\n")

            # print("line number = %d"%data.line_number, end=", ")
            # print("index = %d" % i, end=", ")
            # print("duration = %fms"%(data.duration * 1000))

        i += 1

    f.close()

    print("can_data_filter_duration end.")


can_frame_list = []
can_data_parse_beam(can_frame_list)
can_data_filter_duration(can_frame_list, filter_time)
print("length of can_frame_list = %d"%len(can_frame_list))