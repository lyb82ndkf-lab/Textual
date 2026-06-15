from textual.app import App
from textual.widgets import Label, Static, Header, Footer, Button
from textual.containers import Vertical

# 1. 你的自定义 Static 组件
# MyStatic 继承自 Static
# Static 组件的核心功能就是在屏幕上显示文本
# self.update() 就是用来改变这个文本内容的方法
class MyStatic(Static):
    # on_mount是 Textual 框架自带的一个生命周期钩子
    def on_mount(self) -> None:
        # 当组件挂载到 App 上时，初始化它的内容
        self.update("这是一段[b]加粗[/b]文本")

    # 2. 自定义方法：刷新内容
    def refresh_content(self, text: str) -> None:
        # 接收一个参数 text ， 调用了 self.update(text)
        # 把组件在屏幕上显示的内容刷新成你刚刚传进来的新文本
        self.update(text)

# 2. 主应用类
class TextualStyleApp(App):
    """一个展示 Static、Label 和富文本标记的应用"""

    # BINDINGS 是用来定义键盘快捷键
    BINDINGS = [
        # 格式：(按键, 方法名, 提示信息)
        ("q", "quit", "退出应用"),
    ]

    def compose(self):
        # show_clock=True 会在 Header 中显示一个时钟，方便我们查看时间变化
        yield Header(show_clock=True)

        # 使用 Vertical 容器让组件从上到下排列
        with Vertical(id="container"):
            # 示范 1：直接 yield 一个更轻量的 Label
            yield Label("1. 简单的标签文本 (Label)")
            
            # 示范 2：Label 同样支持样式标记
            yield Label("[green]2. 带有颜色的 Label[/green] -> [u]下划线[/u]")

            # 示范 3：实例化你上面写的自定义 MyStatic 组件
            # 我们给它一个 id，方便后面通过 self.query_one 找到它
            # 相当于赋值
            self.my_custom_static = MyStatic(id="custom_static")
            yield self.my_custom_static
            
            # 示范 4：放一个按钮，点击后改变 MyStatic 的内容，展示各种样式
            # variant="primary" 是按钮的样式，这里用的是高亮样式
            yield Button("点击测试各种内容标记 (Markup)", variant="primary", id="change_btn")

        yield Footer()

    # 3. 按钮点击事件处理
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """当界面上的按钮被点击时触发"""
        if event.button.id == "change_btn":
            # 组合各种复杂的富文本标记
            test_markup = (
                "这是一段 [b]加粗[/b] 文本\n"
                "[i]斜体[/i] 和 [u]下划线[/u]\n"
                "[red]红色[/red] 和 [green]绿色[/green] 文字\n"
                "[bold red on white]加粗红字白底[/bold red on white]\n"
                "普通文本链接: http://example.com"
            )
            # 调用你自定义的方法更新内容
            self.my_custom_static.refresh_content(test_markup)

if __name__ == "__main__":
    TextualStyleApp().run()