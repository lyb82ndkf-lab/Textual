# 层级与偏移示例
from textual.app import App, ComposeResult
from textual.widgets import Static

class LayerOffsetApp(App):
    CSS = """
    /* 
    layers层级
    在 Screen 上定义两个绘制层级
    below 层在下方，above 层在上方
    */
    Screen {
        layers: below above;  /* 左低右高 */
    }

    /*
    layer: 指定组件在哪一层绘制
    将组件放到指定层级，上层组件会覆盖下层组件
    */
    #popup {
        layer: above;  /* 在上层绘制 */
        width: 20;     /* 设置宽度 */
        height: 3;     /* 设置高度 */
        background: red;  /* 红色背景，方便观察覆盖效果 */
        offset: 5 2;   /* 偏移到内容区域上方，产生重叠 */
    }

    /*
    offset: 相对于正常布局位置的偏移量
    第一个值：水平偏移（正数向右，负数向左）
    第二个值：垂直偏移（正数向下，负数向上）
    */
    #floating-box {
        offset: 5 3;  /* 右移5, 下移3 */
        background: yellow;  /* 黄色背景，方便观察 */
        # padding: 1;  /* 增加内边距 */
    }

    #content {
        layer: below;  /* 在下层绘制 */
        background: blue;  /* 蓝色背景，方便观察 */
    }
    """

    def compose(self):
        # 下层组件（蓝色背景）
        yield Static("下层蓝色内容 " * 20, id="content")
        # 浮动组件（带有偏移）
        yield Static("浮动框", id="floating-box")
        # 弹窗组件（上层，红色背景）
        yield Static("上层红色弹窗", id="popup")

if __name__ == "__main__":
    app = LayerOffsetApp()
    app.run()