# Horizontal 水平布局
from textual.app import App, ComposeResult
from textual.widgets import Static

class HorizontalApp(App):
    CSS = """
    # Textual 默认使用垂直布局（子组件从上到下堆叠）
    # 就像之前的 界面布局垂直.py 那样。
    # 而 layout: horizontal 会让子组件从左到右并排排列
    Screen{
        layout: horizontal;
    }
    .box{
        width: 1fr;

        #  Horizontal 布局不会自动设置高度，需要手动设置 `height: 100%`。
        height: 100%;
        border: solid green;
        content-align: center middle;
    }
    """

    def compose(self):
        yield Static("顶部",classes="box")
        yield Static("中间",classes="box")
        yield Static("底部",classes="box")

if __name__ == "__main__":
    app = HorizontalApp()
    app.run()
