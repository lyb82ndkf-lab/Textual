from textual.app import App
from textual.widgets import Static, Button, Input

class SelectorApp(App):
    CSS_PATH = "选择器.tcss"

    def compose(self):

        yield Static("类型选择器示例")
        yield Button("点击我")
        yield Static("ID选择器示例",id="id-selector")
        yield Static("类名选择器示例",classes="class-selector")
        yield Input("通用选择器示例")

        yield Button("伪类选择器示例1")
        yield Input("通用选择器示例2")
        yield Static("伪类选择器示例3",disabled=True)  # 禁用状态下的文本颜色

if __name__ == "__main__":
    app = SelectorApp()
    app.run()
