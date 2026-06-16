from textual.app import App, ComposeResult
from textual.widgets import Button
from textual.widget import Widget
from textual.reactive import reactive
from textual import on

class ColorPreview(Widget):
    # 声明一个响应式变量，默认值为 "blue"
    color = reactive("blue")

    # 🟢 关键监听器代码：
    # 铁律暗号：watch_ + 变量名 (这里就是 watch_color)
    # 只要 color 的值发生改变，Textual 就会在后台百分之百自动调用这个方法！
    def watch_color(self, old_color: str, new_color: str) -> None:
        """当颜色变量发生变化时自动触发执行"""
        
        # 1. 打印后台日志（你可以同时拿到旧值和新值进行对比）
        self.notify(f"【监听器检测到变化】颜色从 {old_color} 变为了 {new_color}")
        
        # 2. 动态修改组件自身的 TCSS 样式背景色，让界面实时刷新变色
        self.styles.background = new_color

    def render(self) -> str:
        # 渲染组件内部文字，顺便告诉你当前的颜色状态
        return f"当前背景颜色变量值: {self.color}"

class WatchDemoApp(App):
    CSS = """
    ColorPreview {
        /* 给颜色方块设置一个初始的长宽和边框，方便肉眼观察 */
        height: 5;
        margin: 1;
        border: solid white;
        text-align: center;
        content-align: center middle;   
    }
    """

    def compose(self) -> ComposeResult:
        yield Button("点击切换颜色", id="toggle-btn")
        yield ColorPreview(id="preview-box")

    @on(Button.Pressed, "#toggle-btn")
    def handle_toggle(self) -> None:
        box = self.query_one("#preview-box", ColorPreview)
        
        # 💡 这里我们只管修改变量的值：如果是 blue 就改成 red，反之亦然
        if box.color == "blue":
            box.color = "red"
        else:
            box.color = "blue"

if __name__ == "__main__":
    WatchDemoApp().run()