from textual.app import App, ComposeResult
from textual.widgets import Input
from textual.widget import Widget
from textual.reactive import reactive
from textual import on

# 1. 定义子组件（儿子）
class TitleWidget(Widget):
    # 💡 核心前提：子组件里必须有一个和主应用（父亲）一模一样的变量名
    title_text: reactive[str] = reactive("")

    def render(self) -> str:
        # 如果没有绑定成功，这里会是空字符串；如果绑定成功，就会显示父亲的数据
        return f"🏆 动态同步的标题：{self.title_text}"

# 2. 定义主应用（父亲）
class ParentApp(App):
    # 父亲手里的核心数据源
    title_text: reactive[str] = reactive("默认标题")

    CSS = """
    TitleWidget {
        background: teal;
        color: white;
        height: 3;
        margin: 1;
        content-align: center middle; /* 🟢 严格使用正确的居中关键字 */
    }
    Input {
        margin: 1;
    }
    """

    def compose(self) -> ComposeResult:
        # 🟢 核心魔法行：在这里将儿子和父亲的数据强行绑定！
        # 注意语法：TitleWidget().data_bind(ParentApp.title_text)
        # 它会在后台建立自动同步通道
        yield TitleWidget().data_bind(ParentApp.title_text)
        
        yield Input(placeholder="在这里打字，观察上方标题的变化...")

    # 3. 当你在输入框打字时，我们只修改“父亲”体内的 title_text 变量
    @on(Input.Changed)
    def on_input_changed(self, event: Input.Changed) -> None:
        # 💥 奇迹发生的地方：
        # 注意看！整个函数里，我【完全没有】去 query 子组件，也【完全没有】写修改子组件的代码！
        # 我只是纯粹地修改了父亲自己的变量：
        self.title_text = event.value

if __name__ == "__main__":
    ParentApp().run()