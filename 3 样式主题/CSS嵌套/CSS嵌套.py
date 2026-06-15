# 从 v0.47.0 开始，Textual 支持 CSS 嵌套语法：

from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Vertical, Horizontal, VerticalScroll


class CSSNestingApp(App):
    # 传统写法
    # #dialog {
    #     background: $panel;
    # }
    # #dialog Button {
    #     width: 1fr;
    # }
    # #dialog Button.primary {
    #     background: $success;
    # }

    # 嵌套写法（等效）
    CSS = """
    #dialog {
        background: $panel;
        Button {
            width: 1fr;
            &.primary {    /* & 代表父选择器 */
                background: $success;
            }
        }
    }
    """

    def compose(self) -> ComposeResult:
        from textual.widgets import Button
        
        yield Vertical(
            Static("这是一个对话框"),
            Button("普通按钮"),
            Button("主要按钮", classes="primary"),
            id="dialog"
        )

if __name__ == "__main__":
    CSSNestingApp().run()