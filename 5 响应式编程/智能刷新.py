from textual.app import App, ComposeResult
from textual.widgets import Static, Input, Button
from textual.widget import Widget
from textual.reactive import reactive, var
from textual import on

class Counter(Widget):

    # 关键：layout=True 表示 count 变化时，会触发组件的重新渲染
    count = reactive(0,layout=True) # 默认值是 0
    # 渲染组件
    def render(self) -> str:
        return f"当前计数: {self.count}"
    
    # 使用Textual自动生成的watch机制
    # 当 count 变化时，动态修改组件自身的TCSS样式宽度
    def watch_count(self, value: int) -> None:
        self.styles.width = 20 + value * 4

class NoRefreshCounter(Counter):

    count = var(0)  # 变化时 不 触发刷新
    def render(self) -> str:
        return f"当前计数: {self.count}"
    
    def watch_count(self, value: int) -> None:
        pass

class SmartRefresh(App):

    CSS = """
    #counter {
        color: black;   
        height: 3;
        background: red;
        width: 20;
    }
    #norefreshcounter {
        background: yellow;
        color: blue;
        height: 3;
        width: 20   ;
    }
    """

    def compose(self) -> ComposeResult:

        yield Button("点击我", id="refresh-button")
        yield Counter(id="counter")
        yield NoRefreshCounter(id="norefreshcounter")

    @on(Button.Pressed, "#refresh-button")
    def on_refresh(self) -> None:
        self.query_one(Counter).count += 1
        # 不会触发刷新
        self.query_one(NoRefreshCounter).count += 1


if __name__ == "__main__":
    SmartRefresh().run()