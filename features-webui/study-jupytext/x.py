# %% [markdown]
# # 🚀 Apphub 编排实验室 (Voila 模式)
# 这是一个纯 `.py` 脚本，通过 Jupytext 与 Voila 实现交互。

# %%
import ipywidgets as widgets
from IPython.display import display, clear_output
from pydantic import BaseModel, ValidationError

# --- 1. 定义 Apphub 数据模型 ---
class ServiceConfig(BaseModel):
    name: str
    port: int
    version: str = "v1.0"

# --- 2. 模拟业务逻辑 ---
def deploy_service(name, port):
    try:
        # Pydantic 校验
        cfg = ServiceConfig(name=name, port=port)
        return f"✅ 校验通过: {cfg.name} 将部署在端口 {cfg.port}"
    except ValidationError as e:
        return f"❌ 校验失败: {e.json()}"

# --- 3. 构建 UI 组件 ---
name_input = widgets.Text(value='FTP-Service', description='服务名:')
port_input = widgets.IntText(value=21, description='端口:')
deploy_btn = widgets.Button(
    description='开始部署',
    button_style='success', # 'success', 'info', 'warning', 'danger' or ''
    icon='cloud-upload'
)
output_area = widgets.Output(layout={'border': '1px solid #ddd', 'padding': '10px'})

# --- 4. 绑定事件逻辑 ---
def on_button_clicked(b):
    with output_area:
        clear_output()
        result = deploy_service(name_input.value, port_input.value)
        print(result)

deploy_btn.on_click(on_button_clicked)

# --- 5. 页面布局 ---
# 就像在 Jupyter 里一样，最后一步 display 它们
ui_box = widgets.VBox([
    widgets.HTML("<h3>配置参数</h3>"),
    name_input,
    port_input,
    deploy_btn,
    widgets.HTML("<br>"),
    output_area
])

display(ui_box)