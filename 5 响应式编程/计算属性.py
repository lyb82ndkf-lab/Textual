from textual.app import App, ComposeResult
from textual.widgets import Button
from textual.widget import Widget
from textual.reactive import reactive
from textual import on
from rich.text import Text

class RGBDisplay(Widget):
    # 1. 声明三个独立的响应式基础变量，默认值都是 0（即黑色）
    red = reactive(0)
    green = reactive(0)
    blue = reactive(0)

    # 🟢 2. 核心计算属性魔法（名字必须叫 compute_ + 虚拟变量名）
    # Textual 看到这个名字后，会自动在后台偷偷创造一个 self.color 变量！
    def compute_color(self) -> str:
        """【计算属性】只要 red、green 或 blue 任何一个发生改变，这里就会自动重新计算"""
        # Textual 会像星探一样盯着这行代码，发现它依赖了 self.red, self.green, self.blue
        return f"rgb({self.red},{self.green},{self.blue})"
    
    # 3. 监听计算出来的虚拟变量
    # 铁律暗号：watch_ + 虚拟变量名 (即 watch_color)
    # 虽然类里没有声明 color = reactive()，但因为有了上面的 compute_color，这里就能完美监听！
    def watch_color(self, color: str) -> None:
        """【监听器】只要上面 compute_color 算出的新颜色变了，这里立刻自动执行"""
        # 动态修改组件自身的背景色
        self.styles.background = color
        self.refresh()

    # 4. 渲染函数：返回当前的 RGB 状态和合成的 CSS 值
    def render(self) -> Text:
        displayText = f"🔴红:{self.red}  🟢绿:{self.green}  🔵蓝:{self.blue}\n合成的 CSS 值为: {self.compute_color()}"
        rich_text = Text(displayText)
        rich_text.stylize(f"on {self.compute_color()}")
        return rich_text

class RGBApp(App):
    CSS = """
    RGBDisplay {
        height: 8;
        margin: 1;
        border: solid white;
        text-align: center;
        content-align: center middle;
    }
    Button {
        margin: 0 1;
    }
    """

    def compose(self) -> ComposeResult:
        # 放置三个控制按钮
        yield Button("红色 +50", id="add-red", variant="error")
        yield Button("绿色 +50", id="add-green", variant="success")
        yield Button("蓝色 +50", id="add-blue", variant="primary")
        
        # 放置我们的颜色展示组件
        yield RGBDisplay(id="color-box")

    # 4. 按钮事件：我们在这里只纯粹地做数学加法，根本不提“改背景色”这回事
    @on(Button.Pressed)
    def handle_buttons(self, event: Button.Pressed) -> None:
        box = self.query_one("#color-box", RGBDisplay)
        
        if event.button.id == "add-red":
            # 限制最大值为 255，超过了就归零重来
            box.red = 0 if box.red >= 250 else box.red + 50
        elif event.button.id == "add-green":
            box.green = 0 if box.green >= 250 else box.green + 50
        elif event.button.id == "add-blue":
            box.blue = 0 if box.blue >= 250 else box.blue + 50

if __name__ == "__main__":
    RGBApp().run()