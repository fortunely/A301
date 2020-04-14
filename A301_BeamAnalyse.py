# -*- coding: utf-8 -*-
import sys
import os.path
from CanFrameInfo import CanFrameInfo
from BCM import BCM
from pathlib import Path

log_file_path_dict = {
    # Changan提供
    "CA_1":r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191217\黑屏\20191216093000_20191216100000.asc",
    "CA_2":r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191220\远近光灯突然熄灭\20191220165000_20191220172000.asc",  #远近光突然熄灭_20191221
    "CA_3":r"F:\工作\SVN\Department\RD\Project\A301_IP\10_客户反馈\PP4\自动重启（亏电）\Trace4.asc", #自动重启问题_20200327
    "CA_4":r"F:\工作\SVN\Department\RD\Project\A301_IP\10_客户反馈\PP4\花屏&黑屏问题\20200330\20200330130200_20200330140200.asc", # 黑屏_20200330
    "CA_5":r"F:\工作\SVN\Department\RD\Project\A301_IP\10_客户反馈\PP4\转向灯频率偶发跳变\20200413103500_20200413113500.asc", #转向灯频率偶发跳变_20200414

    # Rongle提供
    "RL_1":r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191220\正常行驶\Bus Traffic201912201500 12-20-2019 4-59-56 pm.asc",
    "RL_2":r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191220\正常到出现灭灯\Bus Traffic201912201514 12-20-2019 5-14-37 pm.asc",
    "RL_3":r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191221\行驶正常\Bus Traffic201912211656 12-21-2019 4-56-12 pm.asc",
    "RL_4":r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191221\静态近光熄灭\Bus Traffic201912211916 12-21-2019 7-16-38 pm.asc",
    "RL_5":r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191221\静态正常\Bus Traffic201912211547 12-21-2019 3-47-58 pm.asc",
    
    "RL_6":r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191225\近光灯熄灭\Bus Traffic 12-25-2019 15-20-09 pm.asc",
    "RL_7":r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191225\静态正常\Bus Traffic 12-25-2019 13-29-41 pm.asc",

    # 荣乐提供 漠河 升级V0.24_DEBUG后
    "RL_Debug_1": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191228\升级后\Bus Traffic 12-28-2019 6-54-42 pm.asc",
    "RL_Debug_2": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191228\升级后\Bus Traffic 12-28-2019 7-00-48 pm.asc",

    # 杭州replay - 删除280 380
    "HZ_RE_1": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191221\行驶正常\Bus Traffic201912211630 12-21-2019 4-30-52 pm(filtered) CANoe 记录280、380报文.asc",
    "HZ_RE_2": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191221\行驶正常\Bus Traffic201912211656 12-21-2019 4-56-12 pm(filtered) CANoe 记录280、380报文.asc",
    "HZ_RE_3": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191221\静态近光熄灭\Bus Traffic201912211916 12-21-2019 7-16-38 pm(filtered) CANoe 记录280、380.asc",
    "HZ_RE_4": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191221\静态正常\Bus Traffic201912211547 12-21-2019 3-47-58 pm(filtered) CANoe 记录280、380报文.asc",
    "HZ_RE_5": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191221\静态近光熄灭\Bus Traffic201912211916 12-21-2019 7-16-38 pm(filtered)CANoe 记录280、380 -1.asc",
    "HZ_RE_6": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\杭州常温试验\20191230\V0.24_DEBUG_611-1.asc",

    # 692
    "RL_8": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191226\692\off界面开启远近光灯\Bus Traffic 12-26-2019 15-45-41 pm.asc",
    "RL_9": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191226\692\近光熄灭\Bus Traffic 12-26-2019 14-17-21 pm.asc",
    "RL_10": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191226\692\正常静态\Bus Traffic 12-26-2019 15-09-46 pm.asc",
    "RL_11": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191226\692\正常静态，不过15点08下了on电，接着又上on电\Bus Traffic 12-26-2019 14-31-58 pm.asc",

    # 低温箱
    "DG_1":r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\东莞低温试验\20191223\20191223.txt",
    
    # 常温实验台架
    "HZ_1":r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\常温试验台架\20191225\Frame 1(0-9999).asc",
    "HZ_2":r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\常温试验台架\20191225\Frame 2(0-9999).asc",
    "HZ_3":r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\常温试验台架\20191225\frame_all.asc",
    "HZ_4":r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\杭州常温试验\20191226\试验报文记录.asc",
    "HZ_5":r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\杭州常温试验\20191231\V0.26_测报文丢失.asc",

    # 杭州实车
    "HZ_V_1": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\杭州常温试验\2019.12.27 实车报文\整车报文 2019.12.27.asc",

    "HZ_V_2": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\can2020-1-15\14-52.asc",
    "HZ_V_3": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\can2020-1-15\14-53.asc",
    "HZ_V_4": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\can2020-1-15\14-54.asc",
    "HZ_V_5": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\can2020-1-15\14-55.asc",
    "HZ_V_6": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\can2020-1-15\14-56.asc",

    "HZ_V_7": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\can2020-4-7\14-17.asc",
    "HZ_V_8": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\can2020-4-7\14-18.asc",
    "HZ_V_9": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\can2020-4-7\14-19.asc",
    "HZ_V_10": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\can2020-4-7\14-20.asc",
    "HZ_V_11": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\can2020-4-7\14-21.asc",
    "HZ_V_12": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\can2020-4-7\14-22.asc",
    "HZ_V_13": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\can2020-4-7\14-23.asc",
    "HZ_V_14": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\can2020-4-7\14-24.asc",
    "HZ_V_15": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\can2020-4-7\14-25.asc",

    "HZ_V_16": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\canoe20200413\ON档电左转向灯报文.asc",
    "HZ_V_17": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\canoe20200413\ON档电右转向灯报文.asc",
    "HZ_V_18": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\canoe20200413\ON档电，左、右转向灯报文.asc",
    "HZ_V_19": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\实车测试\转向灯声音\canoe20200414\ON左、右转向灯单亮2020.04.14.asc", # 转向灯声音频率跳变
}

log_file_path = log_file_path_dict["HZ_V_19"]

IP_280_50ms = "280"
IP_380_500ms = "380"
IP_611_50ms = "611"
EPB_26B_20ms = "26B"
SRS_50_500ms = "50"
BCM_288_40ms = "288"

id_dict = {
IP_280_50ms: 0.06, #, 0.0001
IP_380_500ms: 0.6, #0.6,
IP_611_50ms: 0.06,
EPB_26B_20ms: 0.025, #filter time =30ms
SRS_50_500ms: 0.01, #filter time =50ms
BCM_288_40ms: 0.05,
}

filter_canid =  str(BCM_288_40ms)
filter_time = id_dict[filter_canid] # 0.06#0.06 # unit: s
print("filter_canid = %s"%filter_canid)

output_file_name = ""
if filter_canid == IP_280_50ms:
    output_file_name = "out_280.txt"
elif filter_canid == IP_380_500ms:
    output_file_name = "out_380.txt"
else:
    output_file_name = "out.txt"


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

    if not output_file_name:
        print("output files name cant be null")
        return

    f = open(output_file_name, "w") # open file for writing
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
            f.write("duration = %.2f ms "%(data.duration * 1000))

            j = 0
            f.write("\tdata[] = ")
            while j < data.can_length:
                f.write("%x "%data.can_data[j])
                j = j + 1

            f.write("\n")

        i += 1

    f.close()

    print("can_data_filter_duration end.")


can_frame_list = []
can_data_parse_beam(can_frame_list)
can_data_filter_duration(can_frame_list, filter_time)
bcm = BCM(can_frame_list)
bcm.ParaseTurnIndcr()
print("length of can_frame_list = %d"%len(can_frame_list))