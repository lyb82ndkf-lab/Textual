from textual.app import App, ComposeResult
from textual.widgets import Label, Button, Static, Header, Footer, Input

class EventApp(App):

    CSS = """
    #input_field {
        width: 100%;
    }
    """

    # | 事件                 | 触发条件              |
    # | -------------------- | --------------------- |
    # | `on_mount`           | Widget/App 挂载到 DOM |
    # | `on_key`             | 任意键按下            |
    # | `on_click`           | 鼠标点击              |
    # | `on_button_pressed`  | Button 被按下         |
    # | `on_input_changed`   | Input 内容变化        |
    # | `on_input_submitted` | Input 回车提交        |
    # | `on_focus`           | 获得焦点              |
    # | `on_blur`            | 失去焦点              |
    # | `on_resize`          | 终端窗口大小变化      |

    def compose(self):
        yield Input("请输入内容", id="input_field")
        yield Button("提交", id="submit_button")
        yield Label("等待操作...", id="status_label")   

    def on_mount(self) -> None:
        """应用挂载完成后触发"""
        self.title = "事件示例"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """按钮点击事件"""
        self.query_one("#status_label", Label).update(f"你点击了: {event.button.id}")

    def on_input_changed(self, event: Input.Changed) -> None:
        """输入框内容变化"""
        self.query_one("#status_label", Label).update(f"输入: {event.value}")

    def on_key(self, event) -> None:
        """按键事件"""
        self.query_one("#status_label", Label).update(f"你按下了: {event.key}")

if __name__ == "__main__":
    app = EventApp()
    app.run()