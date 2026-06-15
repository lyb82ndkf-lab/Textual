from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import Static, Header, Footer, Input, Button

class ContextManagerApp(App):

    CSS = """
    #main{
        height: 100%;
        border: #ff0000; /* 红色边框 */
    }
    #sidebar{
        width: 20%;
        border: #FFFFFF; /* 白色边框 */
    }
    #content{
        height: 100%;
        border: #00FFFF; /* 蓝绿色边框 */
    }
    .menu-item{
        height: 20;
    }
    """

    # 使用 `with` 语句可以更清晰地定义嵌套结构：
    def compose(self):

        with Horizontal(id="main"):
            with VerticalScroll(id="sidebar"):
                yield Static("菜单1",classes="menu-item")
                yield Static("菜单2",classes="menu-item")
                yield Static("菜单3",classes="menu-item")
                yield Static("菜单4",classes="menu-item")
                yield Static("菜单5",classes="menu-item")
                yield Static("菜单6",classes="menu-item")
                yield Static("菜单7",classes="menu-item")
                yield Static("菜单8",classes="menu-item")
                yield Static("菜单9",classes="menu-item")
                yield Static("菜单10",classes="menu-item")
            with VerticalScroll(id="content"):
                yield Static("大量内容...")

    # 等价于
    # def compose(self) -> ComposeResult:
    #     yield Horizontal(
    #         Vertical(
    #             Static("菜单1"),
    #             Static("菜单2"),
    #             id="sidebar",
    #         ),
    #         VerticalScroll(
    #             Static("大量内容..."),
    #             id="content",
    #         ),
    #         id="main",
    #     )

if __name__ == "__main__":
    app = ContextManagerApp()
    app.run()   