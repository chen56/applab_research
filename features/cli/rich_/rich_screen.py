

#%%
import rich
import rich.console
from time import sleep
console=rich.console.Console(force_jupyter=False)
with console.screen(style="white on red"):  # 红色背景，白色文字
    console.print("临时全屏内容，2秒后消失")
    sleep(2)  # 2秒后回到原来的终端界面


#%%
