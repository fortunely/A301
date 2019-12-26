import os.path

log_file_path_dict = {
    # 荣乐提供
    "RL_1": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191221\静态近光熄灭\Bus Traffic201912211916 12-21-2019 7-16-38 pm.asc",
    "RL_2": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191221\静态正常\Bus Traffic201912211547 12-21-2019 3-47-58 pm.asc",
    "RL_3": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191221\行驶正常\Bus Traffic201912211630 12-21-2019 4-30-52 pm.asc",
    "RL_4": r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191221\行驶正常\Bus Traffic201912211656 12-21-2019 4-56-12 pm.asc"
}

current_file_path = log_file_path_dict["RL_4"]
can_ids = ["280", "380","401"]


class CANLogParse(object):
    def __init__(self):
        self._file_path = ""


    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def set_file_path(self, value):
        self._file_path = value


    def is_file_exist(self):
        if self.file_path:
            return os.path.isfile(self.file_path)

        print("%s is not a file."%self.file_path)
        return False

    def get_filter_canid_list(self, list):
        filter_can_id_string = []
        for s in list:
            s = " " + s + "  "
            filter_can_id_string.append(s)
        print(filter_can_id_string)
        return filter_can_id_string


    # @param list remove Can id list
    def removeCanIds(self, filter_list):
        if not filter_list:
            print("remove Can id list is null")
            return

        path = os.path.splitext(self.file_path)[0]
        suffix = os.path.splitext(self.file_path)[1]

        destination_file_path = path + "(filtered)" + suffix

        with open(self.file_path, 'r') as source_file, open(destination_file_path, 'w') as destination_file:
            for line_str in source_file:
                line_str_keep = True

                # if only one filter string of list is in current line string, then ingore the line string(dont copy to new file)
                for filter_string in filter_list:
                    if filter_string in line_str:
                        line_str_keep = False
                        break

                if line_str_keep:
                    destination_file.write(line_str)


can_log_parse = CANLogParse()
can_log_parse.set_file_path = current_file_path
filter_can_id_string = can_log_parse.get_filter_canid_list(can_ids)
can_log_parse.removeCanIds(filter_can_id_string)
