import xlrd
import os
import shutil

num = 0
# 表格复制到同目录，表格名字修改到table_name,目标地址修改dist_file
table_name = "2021082401.xls"
dist_file = r"E:\OCT\\"

data = xlrd.open_workbook(table_name)  # 打开表
table = data.sheets()[0]  # 获取第一个表的sheet
cols_value = table.col_values(1)  # 第一个sheet的第2列数据
for file_name in cols_value:
    # 创建二级子目录
    new_file = dist_file + file_name.split(r"/")[2] + "\\" + file_name.split(r"/")[3]
    try:
        os.makedirs(new_file)
        print("创建 %s 成功" % new_file)
    except:
        pass
    # 复制到对应文件夹
    for file_name1 in cols_value:
        t1_file = "\\".join(file_name1.split(r"/")[4:])
        if t1_file == file_name.split("/")[-1]:
            src_dir = file_name
            dist_dir = dist_file + "Asset\\" +file_name.split("/")[-2] + "\\" + file_name.split("/")[-1]
            num += 1
            print("开始拷贝第%d个目录" % num)
            shutil.copytree(src_dir, dist_dir)
            print("由 %s 拷贝到 %s ,拷贝完成！" % (src_dir, dist_dir))
            print("-----------------------------------------------")
os.system("pause")