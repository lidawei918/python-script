import os
import time
def wan():
    os.system("netsh interface set interface wan enabled")
    os.system("netsh interface ip set address lan static 192.168.1.1 255.255.255.0")

def lan():
    os.system("netsh interface set interface wan disabled")
    os.system("netsh interface ip set address lan static 192.168.1.1 255.255.255.0 192.168.20.1")
    os.system("netsh interface ip set dns lan static 192.168.1.1 primary")

while True:
    print("          网络切换工具 输入选项1或2切换网络")
    print("\t")
    print('          （1）专线模式:适用于和外包会议，外部视频会议，无法访问内部资源')
    print("\t")
    print('          （2）内网模式：适用于公司内部会议，能访问shotgun和1984')
    print("\t")

    a = int(input("          输入选择项然后按回车 : "))

    if a == 1:
        wan()
        print("配置生效中...")
        time.sleep(5)
        break

    if a == 2:
        lan()
        print("配置生效中...")
        time.sleep(5)
        break