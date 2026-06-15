from textual.app import App, ComposeResult
from textual.widgets import Static

class GridApp(App):
    CSS = """
    Screen{
        layout: grid;
        # ### Grid 属性

        # | 属性           | 说明        | 示例                                 |
        # | -------------- | ----------- | ------------------------------------ |
        # | `grid-size`    | 列数 [行数] | `grid-size: 3;` 或 `grid-size: 3 2;` |
        # | `grid-columns` | 列宽        | `grid-columns: 2fr 1fr 1fr;`         |
        # | `grid-rows`    | 行高        | `grid-rows: 25% 75%;`                |
        # | `grid-gutter`  | 单元格间距  | `grid-gutter: 1 2;`                  |
        # | `column-span`  | 跨列        | `column-span: 2;`                    |
        # | `row-span`     | 跨行        | `row-span: 2;`                       |
        grid-size: 3 2; /* 3列2行 */
        grid-gutter: 1 2; /* 单元格间距,行间距1,列间距2 */
        grid-columns: 2fr 1fr 1fr; /* 列宽比 */
    }
    .box{
        border: solid red;
        content-align: center middle;
        # 100% 表示示父容器的高度，所有子元素都占满父容器高度
        height: 100%;
    }
    """

    def compose(self):
        yield Static("1",classes="box")
        yield Static("2",classes="box")
        yield Static("3",classes="box")
        yield Static("4",classes="box")
        yield Static("5",classes="box")
        yield Static("6",classes="box")

if __name__ == "__main__":
    app = GridApp()
    app.run()  
