from textual.widgets import Button, Header, Footer
from textual.app import App, ComposeResult
from textual import on

class ButtonApp(App):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        # 创建按钮
        yield Button("普通按钮", id="normal")
        yield Button("主要按钮", variant="primary", id="primary")
        yield Button("成功按钮", variant="success", id="success")
        yield Button("警告按钮", variant="warning", id="warning")
        yield Button("错误按钮", variant="error", id="error")

        # 禁用按钮
        yield Button("禁用", disabled=True)

    # 处理按钮事件
    # 格式为: @on(事件类型, 选择器)
    # 选择器: #id, .class, tag, * (所有元素)
    @on(Button.Pressed, "#success") 
    def handle_success(self) -> None:
        self.notify("成功按钮被点击了")

    # 传统命名方式
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "normal":
            self.notify("普通按钮被点击了")

if __name__ == "__main__":
    ButtonApp().run()
