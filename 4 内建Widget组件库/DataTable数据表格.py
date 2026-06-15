from textual.app import App, ComposeResult
from textual.widgets import DataTable

class DataTableApp(App):
    def compose(self) -> ComposeResult:
        # 数据表格创建
        yield DataTable(id="table")

    # on_mount是 Textual 框架自带的一个生命周期钩子
    # 当应用启动时，会自动调用这个方法
    def on_mount(self) -> None:
        # 寻找表格
        self.table = self.query_one("#table", DataTable)
        # 定义表头
        self.table.add_columns("姓名", "年龄", "城市", "职业")
        # 填充数据
        self.table.add_rows([
            ("张三", 25, "北京", "前端开发"),
            ("李四", 30, "上海", "后端开发"),
            ("王五", 28, "广州", "数据分析师"),
            ("赵六", 32, "深圳", "数据工程师"),
        ])
        # 行选择模式
        self.table.cursor_type = "row" 


if __name__ == "__main__":
    DataTableApp().run()
