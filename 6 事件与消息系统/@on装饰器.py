from textual.app import App, ComposeResult
from textual.widgets import Button, Input
from textual import on

class OnDecoratorApp(App):
    CSS = """
    Input, Button {
        margin: 1 2;
    }
    /* 危险按钮的特殊样式 */
    .danger {
        background: red;
        color: white;
    }
    """

    def compose(self) -> ComposeResult:
        # 1. 搜索框，带 ID
        yield Input(placeholder="输入关键词并按回车搜索...", id="search")
        # 2. 普通操作按钮，带 ID
        yield Button("点击发送数据", id="send")
        # 3. 危险操作按钮，带 Class 类名
        yield Button("清空历史记录", classes="danger")

    # 用法一：精准绑定 ID (#send)
    @on(Button.Pressed, "#send")
    def handle_send(self) -> None:
        self.notify("发送按钮被点击：数据已成功上报！")

    # 用法二：精准绑定类名 (.danger)
    # 提示：不管是哪个按钮，只要身上带着 .danger 这个类名，点击时都会触发这里
    @on(Button.Pressed, ".danger")
    def handle_danger(self) -> None:
        self.notify("危险按钮被点击：历史记录已被强制抹除！", severity="error")

    # 用法三：捕捉输入框的“回车提交”事件 (Input.Submitted)
    # 提示：在输入框打完字直接敲回车，就会触发此事件，并可以通过 event 拿到里面的内容
    @on(Input.Submitted, "#search")
    def handle_search(self, event: Input.Submitted) -> None:
        # event.value 完美拿到了输入框里的字符串
        self.notify(f"触发搜索，关键字为: {event.value}")

if __name__ == "__main__":
    OnDecoratorApp().run()