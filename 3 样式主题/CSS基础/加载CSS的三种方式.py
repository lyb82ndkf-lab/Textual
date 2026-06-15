from textual.app import App
from textual.widgets import Static

# Textual 使用自己的 CSS 变体（文件扩展名 `.tcss`）
# 语法与 Web CSS 类似但不完全相同。

## 方法1： 外部文件（推荐）
class MyApp(App):
    CSS_PATH = "../TCSS/my_style.tcss"

## 方法2： 多个CSS文件
class MyApp2(App):
    CSS_PATHS = ["../TCSS/my_style1.tcss", "../TCSS/my_style2.tcss"]

## 方法3： 内联CSS
class MyApp3(App):
    CSS = """
    Screen {
        background: #f0f0f0;
    }
    """

##方法4： Widget 内嵌默认CSS
class MyApp4(Static):
    DEFAULT_CSS = """
    Screen {
        background: #f0f0f0;
    }
    """

# 开发时使用 `--dev` 标志可以实时预览 CSS 修改：

# bash
# textual run my_app.py --dev
# 

# 修改 `.tcss` 文件后会**即时生效**，无需重启。