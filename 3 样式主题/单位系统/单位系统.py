from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Vertical, Horizontal, VerticalScroll

class UnitSystemApp(App):

    CSS = """
    /* 单位系统演示 */
    
    /* 无单位：字符数/行数 */
    .unit-none {
        background: #ffeb3b;
        border: solid #ff9800;
        padding: 1; /* 内边距 */
        margin: 1; /* 外边距 */
    }
    
    /* %：父容器百分比 */
    .unit-percent {
        width: 50%; /* 宽度 */
        background: #81c784;
        border: solid #388e3c;
        padding: 1;
        margin: 1; /* 外边距 */
    }
    
    /* fr：弹性比例 */
    .flex-row {
        height: 4;
        border: solid #9c27b0;
        margin: 1;
    }
    .unit-fr-1 { height: 1fr; background: #ce93d8; }
    .unit-fr-2 { height: 2fr; background: #ba68c8; }
    
    /* auto：自动计算 */
    # width: auto 表示根据内容自动计算宽度
    # 它只关注组件内部的内容，不依赖于父容器或终端的大小。
    .unit-auto {
        width: auto; /* 自动计算宽度 */
        background: #64b5f6;
        border: solid #1e88e5;
        padding: 1;
        margin: 1;
    }
    
    /* vw/vh：终端视口百分比 */
    .unit-vw {
        width: 80vw;
        background: #ff8a65;
        border: solid #e64a19;
        padding: 1;
        margin: 1;
    }
    
    /* w/h：可用空间百分比 */
    .unit-w {
        width: 60w;
        background: #aed581;
        border: solid #689f38;
        padding: 1;
        margin: 1;
    }
    """

    def compose(self):
        yield VerticalScroll(
            Static("无单位 width:50 → 固定字符宽度", classes="unit-none"),
            Static("% width:50% → 父容器百分比", classes="unit-percent"),
            Static("fr 弹性比例:"),
            Horizontal(Static("1fr"), Static("2fr"), classes="flex-row"),
            Static("auto width:auto → 自动计算宽度", classes="unit-auto"),
            Static("vw width:80vw → 终端视口%", classes="unit-vw"),
            Static("w width:60w → 可用空间%", classes="unit-w"),
        )

if __name__ == "__main__":
    app = UnitSystemApp()
    app.run()