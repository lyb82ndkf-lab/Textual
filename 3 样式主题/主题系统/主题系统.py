# Textual 内置了多个主题，也可以自定义：

from textual.theme import Theme
from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Vertical

# 自定义主题
my_theme = Theme(
    name="my-theme",
    primary="#88C0D0",
    secondary="#81A1C1",
    accent="#B48EAD",
    foreground="#D8DEE9",
    background="#2E3440",
    surface="#3B4252",
    panel="#434C5E",
    success="#A3BE8C",
    warning="#EBCB8B",
    error="#BF616A",
    dark=True,
)

### 主题颜色变量

# 在 CSS 中使用这些变量：

# | 变量          | 用途                       |
# | ------------- | -------------------------- |
# | `$primary`    | 主色调                     |
# | `$secondary`  | 次要色                     |
# | `$accent`     | 强调色                     |
# | `$foreground` | 默认文字颜色               |
# | `$background` | 背景色                     |
# | `$surface`    | 组件背景色                 |
# | `$panel`      | 面板背景色                 |
# | `$boost`      | 半透明叠加色               |
# | `$success`    | 成功色                     |
# | `$warning`    | 警告色                     |
# | `$error`      | 错误色                     |
# | `$text`       | 自适应文字色（保证可读性） |
# | `$text-muted` | 柔和文字色                 |


# ### 颜色明暗变体

# ```css
# /* 每种颜色都有 3 级加深和 3 级变浅 */
# background: $primary-lighten-1;   /* 变浅一级 */
# background: $primary-darken-2;    /* 加深两级 */
# ```

# ### 颜色预览

# ```bash
# textual colors
# ```


class MyApp(App):
    def on_mount(self) -> None:
        self.register_theme(my_theme)
        self.theme = "my-theme"

if __name__ == "__main__":
    app = MyApp()
    app.run()   