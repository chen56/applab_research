import subprocess
import time

"""
## 如何保证父进程kill后，子进程不变成孤儿进程？

### 方案：“匿名管道重定向” 

当我们从父进程启动子进程时，我们不把父进程的控制台 stdin 给它，而是利用 subprocess.PIPE 在父子进程之间建立一根“专线”。
1. 父进程：持有管道的“写端”。
2. 子进程：持有管道的“读端”（作为它的 stdin）。
3. 父进程被kill后，操作系统内核也会检测到管道的一端关闭，从而向另一端发送 EOF。子进程会立即感知并自杀

优势：
跨平台：这种管道机制在 Windows、Linux 和 macOS 上的表现高度一致。

子问题：子进程kill后，父进程如何知道？

监听管道写错误：
1. 父进程：在写入管道时，应该监听写错误（`pipe.stdin.write()` 可能会抛出 `BrokenPipeError`）。
2. 子进程：在读取管道时，应该监听读错误（`pipe.stdout.readline()` 可能会抛出 `IOError`）。

"""



proc = subprocess.Popen(
    ['python', 'child_script.py'],
    stdin=subprocess.PIPE,  # 关键：创建专属管道
    text=True
)

# 父进程正常做自己的事，比如管理云资源
# 只要 proc 对象不关闭，管道就一直连着
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("父进程退出")