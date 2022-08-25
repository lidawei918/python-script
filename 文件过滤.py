import os
import shutil
import queue
import copy

BASE_DIR = os.getcwd()
file_path = os.path.join(BASE_DIR, "要搜索的文件")
query_path = os.path.join(BASE_DIR, "query.txt")
print(query_path)
with open(query_path,encoding='UTF-8')as f:
    query_list = f.read().split("\n")

file_list = os.listdir(file_path)

query_list2 = copy.copy(query_list)

for query in query_list:
    for file in file_list:
        if query != "":
            if query.strip() in file:
                print("搜索中...学员 {} 的资料已找到".format(query,))
                shutil.move(os.path.join(BASE_DIR, "要搜索的文件", file), os.path.join(BASE_DIR, "搜索出来的数据", file))
                file_list.remove(file)
                try:
                    query_list2.remove(query)
                except ValueError:
                    pass
print("\n")
print("找到的学员的资料已经剪切到\n{}".format(os.path.join(BASE_DIR, "搜索出来的数据")))
print("\n")
print("还有{}个人的资料没有找到".format(len(query_list2)))
print("\n")
print(query_list2)
print("\n")

ss = input(">>>:")