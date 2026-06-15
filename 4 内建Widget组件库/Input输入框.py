from textual.widgets import Input, Header, Footer
from textual import on
from textual.app import App, ComposeResult
# 导入验证器
from textual.validation import Integer

class InputApp(App):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()

        # 基础输入
        # placeholder: 占位符
        yield Input(placeholder="请输入内容...")
        yield Input(placeholder="搜索...", type="text")
        yield Input(placeholder="请输入密码", password=True)

        # 带验证器的输入框
        # 你不需要写任何代码去判断“是不是数字”
        # Textual 靠这个验证器自己就把错误样式画出来了
        yield Input(validators=[Integer()])

        # 带默认值
        yield Input(value="默认文本", id="name-input")

        # 主输入框
        yield Input(placeholder="输入点什么，按回车提交", id="main-input")

    # Input.Changed: 输入框内容变化事件
    @on(Input.Changed,"#main-input")
    def handle_main_input_changed(self, event: Input.Changed) -> None:
        # event.value: 输入框当前内容 , event.old_value: 输入框上一次内容
        self.notify(f"主输入框内容变化: {event.value}")

    # Input.Submitted: 输入框内容提交事件
    @on(Input.Submitted,"#main-input")
    def handle_main_input_submitted(self, event: Input.Submitted) -> None:
        self.notify(f"主输入框内容提交: {event.value}")

if __name__ == "__main__":
    InputApp().run()