from textual.widgets import (
    Checkbox,       # 复选框
    Switch,         # 开关
    RadioButton,    # 单选按钮
    RadioSet,       # 单选按钮组
    Select,         # 下拉选择
    SelectionList,  # 可选择列表
    Static,         # 静态文本
    Placeholder,    # 占位符
    Rule,           # 分隔线
    Sparkline,      # 迷你折线图
    Digits,         # 大号数字显示
    Pretty,         # Python 对象美观打印
    Markdown,       # Markdown 渲染
    MarkdownViewer, # Markdown 查看器（可滚动）
    Collapsible,    # 可折叠面板
    LoadingIndicator,# 加载指示器
    ContentSwitcher, # 内容切换器
    ListItem,       # 列表项
    ListView,       # 列表视图
    MaskedInput,    # 格式化输入
    Log,            # 简单日志
)
from textual.app import App, ComposeResult

class OtherWidgetApp(App):
    def compose(self) -> ComposeResult:
        yield Checkbox()       # 复选框
        yield Switch()         # 开关
        yield RadioButton()       # 单选按钮
        yield RadioSet()       # 单选按钮组
        # yield Select()         # 下拉选择
        yield SelectionList()  # 可选择列表
        yield Static()         # 静态文本
        yield Placeholder()    # 占位符
        yield Rule()           # 分隔线
        yield Sparkline()      # 迷你折线图
        yield Digits()         # 大号数字显示
        # yield Pretty()         # Python 对象美观打印
        yield Markdown()       # Markdown 渲染
        yield MarkdownViewer() # Markdown 查看器（可滚动）
        yield Collapsible()    # 可折叠面板
        yield LoadingIndicator() # 加载指示器
        yield ContentSwitcher() # 内容切换器
        yield ListItem()       # 列表项
        yield ListView()       # 列表视图
        # yield MaskedInput()    # 格式化输入
        yield Log()            # 简单日志

if __name__ == "__main__":
    OtherWidgetApp().run()
