# Vertical 垂直布局
from textual.app import App, ComposeResult
from textual.widgets import Static

class VerticalApp(App):
    CSS = """
    .box{
        #  `1fr` 表示占剩余空间的等比例。三个子组件各 `1fr`，就平均分配高度。
        height: 1fr;
        border: solid green;
        # content-align 用于控制控件内部内容的位置： 
        # center 水平居中
        # middle 垂直居中
        # content-align: center middle;
    }
    """

    def compose(self):
        yield Static("顶部",classes="box")
        yield Static("中间",classes="box")
        yield Static("底部",classes="box")

if __name__ == "__main__":
    app = VerticalApp()
    app.run()
