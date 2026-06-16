from textual.app import App, ComposeResult
from textual.widgets import Static, Button
from textual import on

class MyPanel(Static, can_focus=True):
    # 局部组件：它自己只有 toggle_dark 动作
    def action_toggle_dark(self) -> None:
        self.app.theme = "textual-light" if self.app.theme == "textual-dark" else "textual-dark"
        self.notify("【组件内部】触发了相对动作：切换明暗主题")

    def render(self) -> str:
        return "【子组件面板】\n按 Tab 聚焦我后，按 'd' 切换主题；按 'q' 强行退出"


class ActionApp(App):
    # 1. 完全对齐主图：键盘绑定中的 Action 字符串
    BINDINGS = [
        ("q", "app.quit", "退出"),           # 带 app. 前缀，绝对寻址到 App.action_quit
        ("d", "toggle_dark", "切换暗色"),    # 不带前缀，相对寻址，聚焦在谁身上就调谁的
    ]

    CSS = """
    MyPanel {
        border: solid green;
        margin: 1 2;
        height: 5;
        text-align: center;
        content-align: center middle;
    }
    MyPanel:focus { border: double yellow; }
    Button { margin: 1 2; }
    """

    def compose(self) -> ComposeResult:
        yield MyPanel()
        # 放置两个按钮，用来演示“代码中触发 Action”
        yield Button("点我：代码触发 save", id="btn-save")
        yield Button("点我：代码触发 app.quit", id="btn-quit")

    # 2. 定义对应的 action 函数（暗号：action_ + 动作名）
    def action_quit(self) -> None:
        self.exit()

    def action_save(self) -> None:
        self.notify("💾 【App全局】收到暗号：数据保存成功！")

    # 3. 完全对齐主图：在代码中触发 run_action
    @on(Button.Pressed)
    def handle_buttons(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-save":
            # 相当于你在后台用代码偷偷喊了一声 "save" 暗号，系统会自动找 action_save 执行
            self.run_action("save")
            
        elif event.button.id == "btn-quit":
            # 相当于你在代码里强行呼叫全局退出暗号
            self.run_action("app.quit")

if __name__ == "__main__":
    ActionApp().run()