from textual.app import App, ComposeResult
from textual.widgets import Button
from textual.widget import Widget
from textual.reactive import reactive
from textual import on

# 1. 干净的纯计数器组件
class Counter(Widget):
    count = reactive(0)

    def render(self) -> str:
        return f"计数器数据: {self.count}"

# 2. 调度全局的主应用
class WatchApp(App):
    def compose(self) -> ComposeResult:
        yield Button("点我加 1", id="add-btn")
        yield Counter(id="my-counter")

    # 动态监听的舞台：在应用挂载完成时启动
    def on_mount(self) -> None:
        # 第一步：把要盯着的那个目标组件抓过来
        # query_one: 查询第一个符合条件的组件
        target_counter = self.query_one("#my-counter", Counter)
        
        # 第二步：安装动态监控摄像头！
        # 意思：盯着 target_counter 的 "count" 变量，只要一变，
        # 立刻通知我自己的 handle_count_change 函数
        self.watch(target_counter, "count", self.handle_count_change)

    # 触发的回调函数
    def handle_count_change(self, new_value: int) -> None:
        """这个函数是主应用(App)里的，但它却能在 Counter 改变时自动执行！"""
        self.notify(f"检测到计数器变为了 {new_value}！")

    @on(Button.Pressed, "#add-btn")
    def on_click(self) -> None:
        # 点击按钮只是让计数器数字自增
        self.query_one("#my-counter", Counter).count += 1

if __name__ == "__main__":
    WatchApp().run()