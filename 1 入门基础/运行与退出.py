from textual.app import App, ComposeResult
from textual.widgets import Button, Static, Header, Footer, Input

class myapp(App):

    def compose(self) -> ComposeResult:
        yield Button("退出", id="quit")
        yield Button("确认", id="yes")

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "quit":
            self.exit() # 正常退出应用
        elif event.button.id == "yes":
            self.exit("yes") # 返回值yes


if __name__ == "__main__":
    app = myapp()

    # run() 会阻塞直到应用退出
    result = app.run() # 可以接收 exit() 的返回值

    # app.run(inline=True)

    # 退出时可以返回值
    # 在应用内部调用 self.exit("result") 
    print(f"应用返回: {result}")