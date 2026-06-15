from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Vertical

class CSSVariableApp(App):

    CSS = """
    /* ============ CSS变量演示 ============ */
    
    /* 定义 CSS 变量 */
    $my-color: #004578; /* 蓝色背景 */
    $my-border: wide $my-color; 
    $text-color: #ff0000; /* 红色文本 */

    /* 使用 CSS 变量 */
    Widget {
        background: $my-color;
        border: $my-border;
        color: $text-color;
    }
    
    Static {
        margin: 2;
        padding: 1;
    }
    """

    def compose(self):
        yield Vertical(
            Static("使用 CSS 变量 , 文本颜色来自 $text-color"),
            Static("背景色来自 $my-color"),
            Static("边框来自 $my-border"),
        )

if __name__ == "__main__":
    app = CSSVariableApp()
    app.run()