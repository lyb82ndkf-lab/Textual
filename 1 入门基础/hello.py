from textual.app import App , ComposeResult

# 导入 Textual 应用的核心组件
# Label	轻量级文本标签
# Static	静态文本组件
# Header	标题栏组件
# Footer	状态栏组件
# Button	可交互按钮
from textual.widgets import Label, Button, Static, Header, Footer, Input


class HelloApp(App):

    TITLE = "ICHIGO-TUI"
    SUB_TITLE = "v0.1.0"
    CSS = """
    Header {
        background: #f1bcf0;
        text-align: center;
        color: #ed6f58;
    }
    SCREEN {
        background: #e0e0e0;
    }
    """

    # compose 函数是 Textual 应用的核心布局方法，用于定义界面的组件结构。
    # 定义一个返回 ComposeResult 的生成器方法
    # 工作原理：
    # 生成器模式：使用 yield 而不是 return，允许逐个创建组件
    # 组件树构建：Textual 会收集所有 yield 出的组件，构建成完整的界面树
    # 自动渲染：框架自动处理组件的布局和渲染
    def compose(self) -> ComposeResult:
        # 创建并返回顶部标题栏组件，会自动显示 TITLE 和 SUB_TITLE
        yield Header()
        # 创建并返回静态文本组件，显示 "Hello, World!"
        yield Static("Hello, World!")
        # 创建并返回底部状态栏组件
        yield Footer()

        yield Input("请输入内容")
        yield Button("提交", id="submit_button")
        yield Label("等待操作...", id="status_label")

if __name__ == "__main__":
    HelloApp().run()
