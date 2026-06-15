from textual.app import App, ComposeResult
from textual.widgets import Static

class BoxModelApp(App):

    CSS = """
    /* 演示 margin 的实际效果 */
    
    /* 根容器 - 移除默认 padding */
    Screen {
        padding: 0;
    }
    
    /* 盒子样式 */
    .box {
        width: 30;
        height: 5;
        border: solid deepskyblue;
        padding: 1;
        background: darkorange;
        margin: 5;        /* 四周都是 5 个字符的边距 */
    }
    
    /* 参考线 */
    .reference {
        width: 100%;
        height: 1;
        background: red;
    }
    """

    def compose(self):
        yield Static("←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←", classes="reference")
        yield Static("内容区域", classes="box")

if __name__ == "__main__":
    app = BoxModelApp()
    app.run()