# 在内网管理的时候，通常有些环境下是禁止员工上网的，但一些特殊需求需要防火墙放行部分地址，实现特殊地址的放行
# 若软件官网没有指出该放行的地址，这种情况下是比较痛苦的
# 我这里先打开软件，得到该软件的进程。然后通过进程查看端口号，通过netstat查看端口号的连接得到IP
# 最终防火墙放行这些IP

import os
import psutil
import time
port = "14232"
lis1 = []
pids = psutil.process_iter()
for pid in pids:
    if pid.name() == "Bridge.exe":
        print(pid.pid)


# res=os.popen("netstat -ano | findstr {port}".format(port=port))
# while True:
#     time.sleep(3)
#     for i in res:
#         lis1.append(i.split('    ')[2].split(":")[0])
#     print(set(lis1))