from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Input
from textual.containers import Container, Vertical, Horizontal, VerticalScroll

class myApp(App):
    CSS = """
    /* ============ 特异性规则演示 ============ */
    
    /* 1. ID选择器特异性最高 */
    /* 2. 类选择器次之 */
    /* 3. 类型选择器最低 */
    /* 4. !important 优先级最高 */

    /* ============ 基础样式 ============ */
    Static {
        padding: 1;
        border: solid green;
        margin: 1;
    }

    /* ============ 1. ID 选择器的特异性 ============ */
    #a {
        background: red;
        color: white;
    }
    
    .a {
        background: blue;
        color: white;
    }
    
    /* 类型选择器 - 默认样式 */
    Static {
        background: gray;
        color: black;
    }

    /* ============ 2. 多个类名的特异性 ============ */
    .b {
        background: yellow;
        color: black;
    }
    
    .b.c {
        background: orange;
    }

    /* ============ 3. 组合选择器的特异性 ============ */
    #container {
        border: solid purple;
        padding: 2;
    }
    
    #container Static {
        background: green;
        color: white;
    }
    
    #container .special {
        background: magenta;
        color: white;
    }

    /* ============ 4. !important 覆盖所有规则 ============ */
    .important {
        background: cyan !important;
        color: black !important;
    }
    """

    def compose(self):
        yield VerticalScroll(
            Static("ID选择器(#a) - 红色背景", id="a"),
            Static("类选择器(.a) - 蓝色背景", classes="a"),
            Static("类型选择器(Static) - 灰色背景"),
            
            Static("一个类名(.b) - 黄色背景", classes="b"),
            Static("两个类名(.b.c) - 橙色背景", classes="b c"),
            
            Container(
                Static("ID+类型 - 绿色背景", id="inner1"),
                Static("ID+类 - 品红色背景", classes="special", id="inner2"),
                id="container"
            ),
            
            Static("!important - 青色背景（最高优先级）", id="high-priority", classes="important"),
        )

if __name__ == "__main__":
    app = myApp()
    app.run()