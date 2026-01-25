import rich
from rich.console import Console
from rich.markdown import Markdown

console = Console()

# 定义 Markdown 内容
markdown_text = """
# 一级标题
## 二级标题

这是普通段落，支持 **粗体**、*斜体*、`行内代码`，还有[链接](https://github.com/Textualize/rich)。

- 无序列表项 1
- 无序列表项 2
  - 嵌套列表项

1. 有序列表项 1
2. 有序列表项 2

> 这是一段引用文本

```python

# 代码块示例
def hello():
    print("Hello, Rich!")
```

"""

rich.print(Markdown(markdown_text))
