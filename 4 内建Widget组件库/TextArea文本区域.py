from textual.app import App, ComposeResult
from textual.widgets import TextArea

class TextAreaApp(App):

    def compose(self) -> ComposeResult:
        
        # 多行文本编辑器
        yield TextArea(id="editor")

        # 带初始内容
        yield TextArea("这是初始内容", id="editor2")


if __name__ == "__main__":
    TextAreaApp().run()