import os

log_file_path = r"F:\工作\A301\测试文档\漠河\黑屏F:\工作\A301\测试文档\漠河\黑屏"

log_file_path3 = r"F:\\工作\\A301\\测试文档\\漠河 远近光灯丢失\\20191214170000_20191214180000.asc"  # 远近光灯报文丢失

out_file_path = log_file_path.replace("\\", "\\\\")
print(out_file_path)

def convert_filepath_style_from_win_to_python(filepath):
    if "\\" in filepath:
        print("yes")
    else:
        print("no")


convert_filepath_style_from_win_to_python(log_file_path)


file = os.listdir(r"F:\工作\SVN\Department\RD\Project\A301_IP\03_测试\PP4\漠河\20191217\黑屏\20191216093000_20191216100000.asc")
print(file)
print("file name : ", os.path.splitext(file)[0])
print("file name : ", os.path.splitext(file)[1])

dict =