# Textual 提供了预定义的容器 Widget（来自 `textual.containers`）
# from textual.containers import (
#     Container,        # 通用容器
#     Horizontal,       # 水平布局容器
#     Vertical,         # 垂直布局容器
#     VerticalScroll,   # 带垂直滚动的容器
#     HorizontalScroll, # 带水平滚动的容器
#     Grid,             # 网格布局容器
# )

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static

class ContainerApp(App):
    CSS = """
    Horizontal{ 
        height: 100%;
        border: #ff0000; /* 红色边框 */
    }
    Vertical{
        width: 50%;
        border: #FFFFFF; /* 白色边框 */
    }
    Static{
        height: 1fr; /* 单位fr 表示等比例分配 */
        background: #00FFFF; /* 蓝绿色背景 */
        content-align: center middle;
        # 外边距 上下 左右
        margin: 0 1;
        color: #000000; /* 黑色文字 */
    }
    """

    def compose(self):

        with Horizontal():

            with Vertical():
                yield Static("左侧 - 上")
                yield Static("左侧 - 下")

            with Vertical():
                yield Static("右侧 - 上")
                yield Static("右侧 - 下")


if __name__ == "__main__":
    app = ContainerApp()
    app.run()       
