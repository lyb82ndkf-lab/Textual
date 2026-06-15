from textual.app import App,ComposeResult
from textual.widgets import TabbedContent, TabPane, Label

class TabbedContentApp(App):

    CSS = """
    TabbedContent {
        # 可加可不加感觉没区别
        height: 1fr;
        # width: 1fr;
    }
    """

    def compose(self) -> ComposeResult:

        # 标签页
        with TabbedContent():
            # 标签页标签1
            with TabPane("聊天",id="chat"):
                yield Label("聊天内容")
            # 标签页标签2
            with TabPane("设置",id="settings"):
                yield Label("设置内容")
            # 标签页标签3
            with TabPane("日志",id="logs"):
                yield Label("日志内容")


if __name__ == "__main__":
    TabbedContentApp().run()
