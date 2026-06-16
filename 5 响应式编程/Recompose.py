from textual.app import App, ComposeResult
from textual.widgets import Label, Button
from textual.widget import Widget
from textual.reactive import reactive
from textual import on

class DynamicList(Widget):
    # 🟢 核心声明：recompose=True 告诉系统，
    # 只要 items 变了，立马重新执行下方的 compose
    items: reactive[list[str]] = reactive(list, recompose=True)
    
    def compose(self) -> ComposeResult:
        # 每次 items 改变，这里都会被重新调用，根据最新的数据动态 yield 组件
        for item in self.items:
            yield Label(item)

class TodoApp(App):
    CSS = """
    DynamicList {
        border: solid green;
        margin: 1;
        padding: 1;
    }
    Label {
        background: #222;
        margin: 1 0;
        padding: 0 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Button("添加新任务", id="add-btn")
        # 初始列表是空的
        yield DynamicList(id="my-list")

    @on(Button.Pressed, "#add-btn")
    def handle_add(self) -> None:
        todo_list = self.query_one("#my-list", DynamicList)
        
        # 💡 注意：在 Python 中，直接对列表使用 .append() 
        # 有时候无法触发 Textual 的响应式拦截（因为列表的内存地址没变）。
        # 最稳妥、最标准的写法是“解包赋值”或者重新生成列表：
        new_index = len(todo_list.items) + 1
        todo_list.items = [*todo_list.items, f"任务明细数据 #{new_index}"]

if __name__ == "__main__":
    TodoApp().run()