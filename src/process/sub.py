import datetime
import sys
import threading
import os
import time


def watch_parent():
    # 阻塞式读取。因为父进程没发数据，所以这里会一直停着。
    # 一旦父进程崩溃或退出，管道会自动断开，read() 会立即返回空字符串。
    sys.stdin.read()
    print("检测到父进程连接断开，正在清理云资源并退出...")
    os._exit(0)

# 开启守护线程监控管道状态
t = threading.Thread(target=watch_parent, daemon=True)
t.start()

# 子进程主逻辑
while True:
    time.sleep(1)
    print("child process running...{}",datetime.now())
