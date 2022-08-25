import os

file_path = r"U:\D\123"
def get_dir_size(file_path):
    size = 0
    for root, dirs, file in os.walk(file_path):
        # print("正在遍历的地址是 %s" % root)
        # print("文件夹中的目录 %s" % dirs)
        # print("文件夹中的文件 %s" % file)
        for name in file:
            file = os.path.join(root, name)  # 获取文件名
            size += os.path.getsize(file)    # 返回文件大小，字节
    print("目录大小: %.2f G" % (size / 1073741824))

if __name__ == "__main__":
    get_dir_size(file_path)