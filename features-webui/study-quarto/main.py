# ---
# title: "Apphub: 云资源编排原型"
# format: html
# server: shiny
# ---

import json
from shiny import App, render, ui, reactive
from pydantic import BaseModel, Field
from deepdiff import DeepDiff


# --- 1. 定义 Apphub 核心模型 ---
class CloudAccount(BaseModel):
    vendor: str
    name: str
    region: str = "ap-guangzhou"


class TencentAccount(CloudAccount):
    secret_id: str
    app_id: int


# --- 2. 定义 UI 布局 ---
app_ui = ui.page_fluid(
    ui.panel_title("Apphub 研究终端 (Quarto + Shiny)"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select("vendor", "选择厂商", ["tencentcloud", "aws"]),
            ui.input_text("name", "账户名称", "test_account"),
            ui.input_text("secret_id", "SecretID", "AKID_SAMPLE"),
            ui.input_numeric("app_id", "AppID", 1234567),
            ui.hr(),
            ui.input_action_button("compare", "执行 DeepDiff 校验", class_="btn-primary"),
        ),
        ui.navset_tab(
            ui.nav_panel("模型校验",
                         ui.output_code("model_output"),
                         ui.markdown("---"),
                         ui.output_text_verbatim("diff_output")
                         ),
            ui.nav_panel("项目文档",
                         ui.markdown("""
                ### 关于 Apphub
                这是 **apphub** 项目的 Layer 1 脚本层原型。
                - **核心目标**: 验证多态模型序列化。
                - **技术栈**: Pydantic v2 + DeepDiff + Shiny。
                """)
                         ),
        ),
    ),
)


# --- 3. 定义服务端逻辑 ---
def server(input, output, session):
    @reactive.calc
    def current_model():
        # 实时根据输入构造 Pydantic 模型
        try:
            if input.vendor() == "tencentcloud":
                return TencentAccount(
                    vendor=input.vendor(),
                    name=input.name(),
                    secret_id=input.secret_id(),
                    app_id=input.app_id()
                )
            return CloudAccount(vendor=input.vendor(), name=input.name())
        except Exception as e:
            return f"校验失败: {str(e)}"

    @output
    @render.code
    def model_output():
        model = current_model()
        if isinstance(model, str): return model
        return json.dumps(model.model_dump(), indent=2, ensure_ascii=False)

    @output
    @render.text
    def diff_output():
        # 只有点击按钮时才执行 DeepDiff
        input.compare()  # 依赖追踪

        # 模拟一个预期的 Target 配置
        expected = {"vendor": "tencentcloud", "region": "ap-guangzhou"}
        actual = current_model().model_dump()

        # 使用我们之前讨论的 ignore_extra_fields 逻辑（DeepDiff 的包含关系检查）
        diff = DeepDiff(expected, actual, ignore_order=True, ignore_extra_fields=True)

        if not diff:
            return "✅ 包含关系检查：当前账户完全符合预期 Target 最小子集"
        return f"❌ 差异检测：\n{diff.pretty()}"


app = App(app_ui, server)