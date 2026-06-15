from textual.app import App, ComposeResult
from textual.widgets import Static, Button
from textual.containers import Vertical

class CombinatorApp(App):
    CSS = """
    /* ============ 基础样式 ============ */
    Button {
        margin: 1;
    }

    Static {
        margin: 1;
        padding: 1;
        border: solid green;  /* 给所有组件加绿色边框 */
    }

    /* ============ 后代组合器 (空格) ============ */
    /* 匹配 #container 内部所有层级的 Button */
    /* 无论嵌套多深都会被选中 */
    #container Button {
        background: blue;  /* 蓝色背景 */
        color: white;     /* 白色文本 */
    }

    /* ============ 子组合器 (>) ============ */
    /* 只匹配 #sidebar 的直接子 Button */
    /* 更深层嵌套的 Button 不会被选中 */
    #sidebar > Button {
        background: red;  /* 红色背景 */
        color: yellow;   /* 黄色文本 */
    }

    /* ============ 容器样式 ============ */
    #container {
        border: solid orange;
        padding: 2;
        margin: 2;
    }

    #sidebar {
        border: solid purple;
        padding: 2;
        margin: 1;
    }

    #inner-box {
        border: dashed cyan;
        padding: 1;
        margin: 1;
    }
    """

    def compose(self) -> ComposeResult:
        # 根容器
        yield Vertical(
            Static("【外层容器】橙色边框 - 所有内部按钮都是蓝色（后代组合器）"),
            Button("蓝色按钮 - 被后代组合器选中"),
            
            # 侧边栏容器
            Vertical(
                Static("【侧边栏】紫色边框 - 直接子按钮是红色（子组合器）"),
                Button("红色按钮 - 被后代+子组合器选中"),
                
                # 内层盒子
                Vertical(
                    Static("【内层盒子】青色虚线边框"),
                    Button("蓝色按钮 - 只被后代组合器选中"),
                    id="inner-box"
                ),
                id="sidebar"
            ),
            id="container"
        )

if __name__ == "__main__":
    app = CombinatorApp()
    app.run()   