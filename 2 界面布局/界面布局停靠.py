# 将组件固定在容器边缘，不参与流动布局：

from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer, Input, Button

class DockApp(App):
    CSS = """
    #sidebar{
        # 固定在左侧
        dock: left;
        width: 20%;
        background: #000000;
        # 内边距
        padding: 1;
        height: 100%;
    }
    #content{
        # 内容区域左侧外边距
        margin-left: 1;
    }
    """

    def compose(self):
        yield Header()
        yield Static("侧边栏\n菜单项1\n菜单项2\n菜单项3",id="sidebar")
        yield Static("内容区域",id="content")
        yield Footer()

if __name__ == "__main__":
    app = DockApp()
    app.run()   

