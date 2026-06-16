from textual.app import App, ComposeResult
from textual.widgets import Static, Input
from textual.widget import Widget
from textual.reactive import reactive
from textual import on

class Greeting(Widget):

    who = reactive("World") # 默认值是 World
    # 自动推断类型，这里 age 是 int 类型，所以这里需要写 int
    age = reactive(0) # 默认值是 0

    # 渲染组件
    def render(self) -> str:
        # 渲染组件时，会自动调用 render 方法
        return f"Hello, {self.who}，你今年 {self.age} 岁" 
    
class reactiveApp(App):
    def compose(self) -> ComposeResult:
        
        yield Input("请输入姓名", id="name-input")
        yield Input(placeholder="请输入年龄", id="age-input")
        yield Greeting()

    # on_组件名小写_事件名小写 是Textual的标准事件命名规范 
    @on(Input.Changed, "#name-input")
    def on_name_changed(self, event: Input.Changed) -> None:
        self.query_one(Greeting).who = event.value

    @on(Input.Changed, "#age-input")
    def on_age_changed(self, event: Input.Changed) -> None:
        self.query_one(Greeting).age = int(event.value)

if __name__ == "__main__":
    reactiveApp().run()
