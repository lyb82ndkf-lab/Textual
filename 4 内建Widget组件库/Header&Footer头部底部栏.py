from textual.widgets import Header, Footer
from textual.app import App, ComposeResult

class HeaderFooterApp(App):

    def compose(self) -> ComposeResult:
        # 头部 显示时间 
        yield Header(show_clock=True)
        # 底部
        yield Footer()

if __name__ == "__main__":
    HeaderFooterApp().run()