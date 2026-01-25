#%%
import rich
rich.print("[red]hello[/] world")
rich.get_console().log("hello")


#%%
print("s")
import rich
rich.get_console().log("hello===")
{"1":1}


##. justify对齐
#%%
from rich.console import Console

console = Console(width=20)

style = "bold white on blue"
console.print("Rich", style=style)
console.print("Rich", style=style, justify="left")
console.print("Rich", style=style, justify="center")
console.print("Rich", style=style, justify="right")


## style
#%%
from rich.console import Console
blue_console = Console(style="white on blue",force_jupyter=True)
blue_console.print("I'm blue. Da ba dee da ba di.")
%env
