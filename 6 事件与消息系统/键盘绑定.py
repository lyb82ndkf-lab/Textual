from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Static

# Widget 级别绑定（完全对齐主图）
class MyWidget(Static, can_focus=True):
    BINDINGS = [
        Binding("enter", "select", "选择"),
        Binding("space", "toggle", "切换"),
    ]
    
    def action_select(self) -> None:
        self.notify("选中")

    # 补充主图缺失的 toggle 行为，使其闭环
    def action_toggle(self) -> None:
        self.notify("切换状态")

    def render(self) -> str:
        return "【子组件】\n先按 Tab 键聚焦我，再按 Enter 或 Space 键"


# App 级别绑定（完全对齐主图）
class MyApp(App):
    BINDINGS = [
        Binding("ctrl+s", "save", "保存", show=True),
        Binding("ctrl+q", "quit", "退出"),
        Binding("up,k", "scroll_up", "上移"),
        Binding("down,j", "scroll_down", "下移"),
        Binding("escape", "cancel", "取消", show=False),
    ]
    
    CSS = """
    MyWidget {
        border: solid green;
        margin: 2;
        height: 5;
        text-align: center;
        content-align: center middle;
    }
    MyWidget:focus {
        border: double yellow;
    }
    """

    def compose(self) -> ComposeResult:
        # 装载图片中的自定义 Widget 级别组件
        yield MyWidget()
    
    def action_save(self) -> None:
        self.notify("已保存！")
    
    def action_quit(self) -> None:
        self.exit()
    
    def action_scroll_up(self) -> None:
        self.scroll_up(animate=True)

    # 补充主图缺失的 scroll_down 行为
    def action_scroll_down(self) -> None:
        self.scroll_down(animate=True)

    # 补充主图缺失的 cancel 行为
    def action_cancel(self) -> None:
        self.notify("已取消操作")

if __name__ == "__main__":
    MyApp().run()