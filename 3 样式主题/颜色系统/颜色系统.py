from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Vertical

class ColorSystemApp(App):

    CSS = """
    /* ============ 颜色系统演示 ============ */
    
    /* 1. 命名颜色 */
    .named-color {
        background: crimson;
        color: white;
        padding: 1;
        margin: 1;
    }
    
    /* 2. 十六进制颜色 */
    .hex-color {
        background: #9932CC;
        color: white;
        padding: 1;
        margin: 1;
    }
    
    .hex-short {
        background: #f00;
        color: white;
        padding: 1;
        margin: 1;
    }
    
    /* 3. RGB 颜色 */
    .rgb-color {
        background: rgb(255, 0, 0);
        color: white;
        padding: 1;
        margin: 1;
    }
    
    /* 4. HSL 颜色 */
    .hsl-color {
        background: hsl(120, 100%, 50%);
        color: black;
        padding: 1;
        margin: 1;
    }
    
    /* 5. RGBA 颜色（含透明度）*/
    .rgba-color {
        background: rgba(153, 50, 204, 0.5);
        color: black;
        padding: 1;
        margin: 1;
    }
    
    .hex-alpha {
        background: #9932CC7F;
        color: black;
        padding: 1;
        margin: 1;
    }
    """

    def compose(self):
        yield Vertical(
            Static("1. 命名颜色: crimson", classes="named-color"),
            Static("2. 十六进制: #9932CC", classes="hex-color"),
            Static("3. 十六进制简写: #f00", classes="hex-short"),
            Static("4. RGB: rgb(255, 0, 0)", classes="rgb-color"),
            Static("5. HSL: hsl(120, 100%, 50%)", classes="hsl-color"),
            Static("6. RGBA: rgba(153, 50, 204, 0.5)", classes="rgba-color"),
            Static("7. 十六进制含透明度: #9932CC7F", classes="hex-alpha"),
        )

if __name__ == "__main__":
    app = ColorSystemApp()
    app.run()