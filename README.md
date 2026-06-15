# Textual TUI 开发完全教程 —— 从零开始构建 Agent 终端界面

> 📖 本教程基于 Textual 官方文档（ https://textual.textualize.io/ ）整理，覆盖从入门到高级的全部知识点。  
> 🎯 最终目标：用 Python + Textual 构建一个功能完整、界面美观的 **AI Agent TUI 界面**。

---

## 目录

- [第一部分：入门基础](#第一部分入门基础)
  - [1.1 什么是 Textual](#11-什么是-textual)
  - [1.2 安装与环境](#12-安装与环境)
  - [1.3 第一个应用：Hello World](#13-第一个应用hello-world)
  - [1.4 App 类基础](#14-app-类基础)
  - [1.5 compose 方法与 Widget](#15-compose-方法与-widget)
  - [1.6 事件处理](#16-事件处理)
  - [1.7 运行与退出](#17-运行与退出)
- [第二部分：界面布局](#第二部分界面布局)
  - [2.1 布局系统概览](#21-布局系统概览)
  - [2.2 Vertical 垂直布局](#22-vertical-垂直布局)
  - [2.3 Horizontal 水平布局](#23-horizontal-水平布局)
  - [2.4 Grid 网格布局](#24-grid-网格布局)
  - [2.5 Dock 停靠布局](#25-dock-停靠布局)
  - [2.6 容器组件](#26-容器组件)
  - [2.7 上下文管理器语法](#27-上下文管理器语法)
  - [2.8 层级与偏移](#28-层级与偏移)
- [第三部分：样式与主题](#第三部分样式与主题)
  - [3.1 Textual CSS 基础](#31-textual-css-基础)
  - [3.2 选择器](#32-选择器)
  - [3.3 组合器](#33-组合器)
  - [3.4 特异性规则](#34-特异性规则)
  - [3.5 CSS 变量与主题系统](#35-css-变量与主题系统)
  - [3.6 颜色系统](#36-颜色系统)
  - [3.7 盒模型：宽高、内外边距、边框](#37-盒模型宽高内外边距边框)
  - [3.8 单位系统](#38-单位系统)
  - [3.9 CSS 嵌套](#39-css-嵌套)
  - [3.10 常用样式属性速查](#310-常用样式属性速查)
- [第四部分：内建 Widget 组件库](#第四部分内建-widget-组件库)
  - [4.1 Static / Label 静态文本](#41-static--label-静态文本)
  - [4.2 Button 按钮](#42-button-按钮)
  - [4.3 Input 输入框](#43-input-输入框)
  - [4.4 TextArea 文本区域](#44-textarea-文本区域)
  - [4.5 DataTable 数据表格](#45-datatable-数据表格)
  - [4.6 Tree / DirectoryTree 树形结构](#46-tree--directorytree-树形结构)
  - [4.7 TabbedContent 标签页](#47-tabbedcontent-标签页)
  - [4.8 Select / OptionList 下拉选择](#48-select--optionlist-下拉选择)
  - [4.9 RichLog / Log 日志](#49-richlog--log-日志)
  - [4.10 ProgressBar / LoadingIndicator](#410-progressbar--loadingindicator)
  - [4.11 Header / Footer 头部底部栏](#411-header--footer-头部底部栏)
  - [4.12 其他常用 Widget](#412-其他常用-widget)
- [第五部分：响应式编程 (Reactive)](#第五部分响应式编程-reactive)
  - [5.1 创建 Reactive 属性](#51-创建-reactive-属性)
  - [5.2 智能刷新](#52-智能刷新)
  - [5.3 验证 (Validation)](#53-验证-validation)
  - [5.4 监听器 (Watch Methods)](#54-监听器-watch-methods)
  - [5.5 计算属性 (Compute Methods)](#55-计算属性-compute-methods)
  - [5.6 数据绑定 (Data Binding)](#56-数据绑定-data-binding)
- [第六部分：事件与消息系统](#第六部分事件与消息系统)
  - [6.1 消息队列机制](#61-消息队列机制)
  - [6.2 消息冒泡](#62-消息冒泡)
  - [6.3 自定义消息](#63-自定义消息)
  - [6.4 @on 装饰器](#64-on-装饰器)
  - [6.5 键盘绑定 (Key Bindings)](#65-键盘绑定-key-bindings)
  - [6.6 Actions 系统](#66-actions-系统)
- [第七部分：自定义 Widget](#第七部分自定义-widget)
  - [7.1 从 Widget 继承](#71-从-widget-继承)
  - [7.2 从 Static 继承](#72-从-static-继承)
  - [7.3 默认 CSS (DEFAULT_CSS)](#73-默认-css-default_css)
  - [7.4 复合组件 (Compound Widgets)](#74-复合组件-compound-widgets)
  - [7.5 渲染 Rich 对象](#75-渲染-rich-对象)
  - [7.6 Line API 高级渲染](#76-line-api-高级渲染)
  - [7.7 Tooltips 与 Loading 状态](#77-tooltips-与-loading-状态)
- [第八部分：Screen 屏幕管理](#第八部分screen-屏幕管理)
  - [8.1 什么是 Screen](#81-什么是-screen)
  - [8.2 创建与切换 Screen](#82-创建与切换-screen)
  - [8.3 ModalScreen 模态对话框](#83-modalscreen-模态对话框)
  - [8.4 从 Screen 返回数据](#84-从-screen-返回数据)
  - [8.5 多模式 (Modes)](#85-多模式-modes)
- [第九部分：Workers 并发任务](#第九部分workers-并发任务)
  - [9.1 为什么需要 Workers](#91-为什么需要-workers)
  - [9.2 @work 装饰器](#92-work-装饰器)
  - [9.3 run_worker 方法](#93-run_worker-方法)
  - [9.4 线程 Workers](#94-线程-workers)
  - [9.5 Worker 生命周期与事件](#95-worker-生命周期与事件)
- [第十部分：调试与测试](#第十部分调试与测试)
  - [10.1 DevTools 开发者工具](#101-devtools-开发者工具)
  - [10.2 自动化测试](#102-自动化测试)
- [第十一部分：实战 —— 构建 Agent TUI 界面](#第十一部分实战构建-agent-tui-界面)
  - [11.1 需求分析与架构设计](#111-需求分析与架构设计)
  - [11.2 Step 1: 项目结构](#112-step-1-项目结构)
  - [11.3 Step 2: 基础骨架](#113-step-2-基础骨架)
  - [11.4 Step 3: 聊天消息区域](#114-step-3-聊天消息区域)
  - [11.5 Step 4: 输入区域与发送](#115-step-4-输入区域与发送)
  - [11.6 Step 5: 流式输出与打字效果](#116-step-5-流式输出与打字效果)
  - [11.7 Step 6: 侧边栏 —— 会话管理](#117-step-6-侧边栏会话管理)
  - [11.8 Step 7: 主题美化](#118-step-7-主题美化)
  - [11.9 Step 8: 工具面板与 Function Calling](#119-step-8-工具面板与-function-calling)
  - [11.10 Step 9: Markdown 渲染](#1110-step-9-markdown-渲染)
  - [11.11 Step 10: 快捷键与命令面板](#1111-step-10-快捷键与命令面板)
  - [11.12 完整代码参考](#1112-完整代码参考)
- [附录：常用 API 速查表](#附录常用-api-速查表)

---

# 第一部分：入门基础

## 1.1 什么是 Textual

Textual 是一个 Python 框架，用于构建**终端用户界面 (TUI)**。它由 [Textualize](https://textualize.io/) 开发，底层基于 Rich 库进行终端渲染。Textual 的核心特点：

- **CSS 样式系统**：类似 Web 开发的 CSS 样式分离，让界面与逻辑分离
- **组件化**：所有界面元素都是 Widget，可以组合嵌套
- **响应式编程**：内置 `reactive` 属性，自动刷新 UI
- **异步支持**：基于 asyncio，支持高并发网络操作
- **丰富的内建组件**：按钮、输入框、表格、树形视图等 30+ 内建 Widget
- **跨平台**：支持 Linux、macOS、Windows

## 1.2 安装与环境

### 系统要求

- Python 3.9 或更高版本（建议使用最新版）
- Windows 推荐使用 [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701)
- macOS 推荐安装 [iTerm2](https://iterm2.com/) 或 [Ghostty](https://ghostty.org/)

### 安装

```bash
# 核心库
pip install textual

# 开发工具（强烈推荐，包含 live reload、调试控制台等）
pip install textual-dev

# 如果需要 TextArea 的语法高亮功能
pip install "textual[syntax]"
```

### 验证安装

```bash
# 运行官方 Demo
python -m textual

# 查看开发工具命令
textual --help
```

## 1.3 第一个应用：Hello World

创建文件 `hello.py`：

```python
from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer


class HelloApp(App):
    """我的第一个 Textual 应用"""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Hello, [b]World[/b]! 🎉", id="greeting")
        yield Footer()


if __name__ == "__main__":
    app = HelloApp()
    app.run()
```

运行：

```bash
python hello.py
```

你将看到一个带有 Header（标题栏）和 Footer（底部快捷键栏）的终端界面，中间显示 "Hello, World!" 的加粗文字。

> 💡 **退出应用**：按 `Ctrl+Q` 即可退出 Textual 应用。

## 1.4 App 类基础

每个 Textual 应用都需要继承 `App` 类：

```python
from textual.app import App


class MyApp(App):
    # 应用标题
    TITLE = "我的应用"
    
    # 应用副标题
    SUB_TITLE = "v1.0"
    
    # 外部 CSS 文件路径
    CSS_PATH = "styles.tcss"
    
    # 或者使用内联 CSS
    CSS = """
    Screen {
        background: $surface;
    }
    """


if __name__ == "__main__":
    app = MyApp()
    app.run()
```

### 关键属性

| 属性        | 说明                                            |
| ----------- | ----------------------------------------------- |
| `TITLE`     | 应用标题，显示在 Header 中                      |
| `SUB_TITLE` | 副标题                                          |
| `CSS_PATH`  | 外部 CSS 文件路径（相对路径相对于 Python 文件） |
| `CSS`       | 内联 CSS 字符串                                 |
| `BINDINGS`  | 键盘绑定列表                                    |
| `SCREENS`   | 命名屏幕字典                                    |
| `MODES`     | 多模式屏幕栈                                    |

## 1.5 compose 方法与 Widget

`compose()` 方法是 Textual 的核心——它定义了界面的组件结构：

```python
from textual.app import App, ComposeResult
from textual.widgets import Label, Button, Static, Header, Footer


class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("这是标签组件")
        yield Button("点击我", id="my-button", variant="primary")
        yield Static("这是静态文本组件")
        yield Footer()


if __name__ == "__main__":
    app = MyApp()
    app.run()
```

### Widget 基础

Widget 是界面的基本单元，每个 Widget 管理终端屏幕上的一块矩形区域。

**关键 Widget 一览**：

| Widget             | 用途                         |
| ------------------ | ---------------------------- |
| `Static`           | 显示静态文本/内容            |
| `Label`            | 标签（类似 Static 但更轻量） |
| `Button`           | 可点击按钮                   |
| `Input`            | 单行文本输入                 |
| `TextArea`         | 多行文本编辑器               |
| `DataTable`        | 数据表格                     |
| `Tree`             | 树形视图                     |
| `RichLog`          | 日志输出                     |
| `Header`           | 顶部标题栏                   |
| `Footer`           | 底部快捷键栏                 |
| `TabbedContent`    | 标签页容器                   |
| `Select`           | 下拉选择框                   |
| `ProgressBar`      | 进度条                       |
| `LoadingIndicator` | 加载指示器                   |
| `Markdown`         | Markdown 渲染                |
| `DirectoryTree`    | 文件目录树                   |

### Widget 的 id 和 classes

```python
yield Button("确定", id="ok-btn", classes="primary large")
yield Static("内容", id="content", classes="text-muted")
```

- `id`：唯一标识符（在同级中唯一），用于 CSS 选择器 `#ok-btn`
- `classes`：CSS 类名（空格分隔），用于 CSS 选择器 `.primary`

## 1.6 事件处理

Textual 使用 `on_` 前缀的方法来处理事件：

```python
from textual.app import App, ComposeResult
from textual.widgets import Button, Input, Label


class EventApp(App):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="输入点什么...")
        yield Button("提交", id="submit", variant="success")
        yield Label("等待操作...", id="status")

    def on_mount(self) -> None:
        """应用挂载完成后触发"""
        self.title = "事件示例"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """按钮点击事件"""
        self.query_one("#status", Label).update(f"你点击了: {event.button.id}")

    def on_input_changed(self, event: Input.Changed) -> None:
        """输入框内容变化"""
        self.query_one("#status", Label).update(f"输入: {event.value}")

    def on_key(self, event) -> None:
        """按键事件"""
        pass  # 处理键盘输入


if __name__ == "__main__":
    app = EventApp()
    app.run()
```

### 常用事件

| 事件                 | 触发条件              |
| -------------------- | --------------------- |
| `on_mount`           | Widget/App 挂载到 DOM |
| `on_key`             | 任意键按下            |
| `on_click`           | 鼠标点击              |
| `on_button_pressed`  | Button 被按下         |
| `on_input_changed`   | Input 内容变化        |
| `on_input_submitted` | Input 回车提交        |
| `on_focus`           | 获得焦点              |
| `on_blur`            | 失去焦点              |
| `on_resize`          | 终端窗口大小变化      |

## 1.7 运行与退出

```python
from textual.app import App

class MyApp(App):
    pass

if __name__ == "__main__":
    app = MyApp()
    
    # run() 会阻塞直到应用退出
    result = app.run()  # 可以接收 exit() 的返回值
    
    # 退出时可以返回值
    # 在应用内部调用 self.exit("result") 
    print(f"应用返回: {result}")
```

### 退出应用

```python
# 在应用内部
def on_button_pressed(self, event: Button.Pressed) -> None:
    if event.button.id == "quit":
        self.exit()  # 正常退出
    elif event.button.id == "yes":
        self.exit("yes")  # 返回值 "yes"
```

### Inline 模式

```python
app.run(inline=True)  # 在命令行提示符下方运行，不进入全屏模式
```

---

# 第二部分：界面布局

## 2.1 布局系统概览

Textual 支持四种核心布局模式：

| 布局       | 说明             | CSS 值                        |
| ---------- | ---------------- | ----------------------------- |
| Vertical   | 垂直排列（默认） | `layout: vertical`            |
| Horizontal | 水平排列         | `layout: horizontal`          |
| Grid       | 网格排列         | `layout: grid`                |
| Dock       | 停靠到边缘       | `dock: top/bottom/left/right` |

## 2.2 Vertical 垂直布局

Vertical 是默认布局，子组件从上到下排列：

```python
from textual.app import App, ComposeResult
from textual.widgets import Static


class VerticalApp(App):
    CSS = """
    .box {
        height: 1fr;
        border: solid green;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("顶部", classes="box")
        yield Static("中部", classes="box")
        yield Static("底部", classes="box")


if __name__ == "__main__":
    app = VerticalApp()
    app.run()
```

> 💡 `1fr` 表示占剩余空间的等比例。三个子组件各 `1fr`，就平均分配高度。

## 2.3 Horizontal 水平布局

```python
from textual.app import App, ComposeResult
from textual.widgets import Static


class HorizontalApp(App):
    CSS = """
    Screen {
        layout: horizontal;
    }
    .box {
        width: 1fr;
        height: 100%;
        border: solid green;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("左", classes="box")
        yield Static("中", classes="box")
        yield Static("右", classes="box")


if __name__ == "__main__":
    app = HorizontalApp()
    app.run()
```

> ⚠️ Horizontal 布局不会自动设置高度，需要手动设置 `height: 100%`。

## 2.4 Grid 网格布局

```python
from textual.app import App, ComposeResult
from textual.widgets import Static


class GridApp(App):
    CSS = """
    Screen {
        layout: grid;
        grid-size: 3 2;       /* 3列 x 2行 */
        grid-gutter: 1 2;     /* 行间距1, 列间距2 */
        grid-columns: 2fr 1fr 1fr;  /* 列宽比 */
    }
    .box {
        height: 100%;
        border: solid green;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("1", classes="box")
        yield Static("2", classes="box")
        yield Static("3", classes="box")
        yield Static("4", classes="box")
        yield Static("5", classes="box")
        yield Static("6", classes="box")


if __name__ == "__main__":
    app = GridApp()
    app.run()
```

### Grid 属性

| 属性           | 说明        | 示例                                 |
| -------------- | ----------- | ------------------------------------ |
| `grid-size`    | 列数 [行数] | `grid-size: 3;` 或 `grid-size: 3 2;` |
| `grid-columns` | 列宽        | `grid-columns: 2fr 1fr 1fr;`         |
| `grid-rows`    | 行高        | `grid-rows: 25% 75%;`                |
| `grid-gutter`  | 单元格间距  | `grid-gutter: 1 2;`                  |
| `column-span`  | 跨列        | `column-span: 2;`                    |
| `row-span`     | 跨行        | `row-span: 2;`                       |

## 2.5 Dock 停靠布局

将组件固定在容器边缘，不参与流动布局：

```python
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static


class DockApp(App):
    CSS = """
    #sidebar {
        dock: left;
        width: 20;
        background: $panel;
        padding: 1;
    }
    #content {
        margin-left: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("侧边栏\n\n菜单项1\n菜单项2\n菜单项3", id="sidebar")
        yield Static("主内容区域", id="content")
        yield Footer()


if __name__ == "__main__":
    app = DockApp()
    app.run()
```

## 2.6 容器组件

Textual 提供了预定义的容器 Widget（来自 `textual.containers`）：

```python
from textual.containers import (
    Container,        # 通用容器
    Horizontal,       # 水平布局容器
    Vertical,         # 垂直布局容器
    VerticalScroll,   # 带垂直滚动的容器
    HorizontalScroll, # 带水平滚动的容器
    Grid,             # 网格布局容器
)
```

```python
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static


class ContainerApp(App):
    CSS = """
    Horizontal {
        height: 100%;
    }
    Vertical {
        width: 1fr;
        border: solid green;
    }
    Static {
        height: 1fr;
        content-align: center middle;
        background: $boost;
        margin: 0 1;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical():
                yield Static("左列 - 上")
                yield Static("左列 - 下")
            with Vertical():
                yield Static("右列 - 上")
                yield Static("右列 - 下")


if __name__ == "__main__":
    app = ContainerApp()
    app.run()
```

## 2.7 上下文管理器语法

使用 `with` 语句可以更清晰地定义嵌套结构：

```python
def compose(self) -> ComposeResult:
    with Horizontal(id="main"):
        with Vertical(id="sidebar"):
            yield Static("菜单1")
            yield Static("菜单2")
        with VerticalScroll(id="content"):
            yield Static("大量内容...")


# 等价于
def compose(self) -> ComposeResult:
    yield Horizontal(
        Vertical(
            Static("菜单1"),
            Static("菜单2"),
            id="sidebar",
        ),
        VerticalScroll(
            Static("大量内容..."),
            id="content",
        ),
        id="main",
    )
```

## 2.8 层级与偏移

### Layers 层级

```css
Screen {
    layers: below above;  /* 左低右高 */
}

#popup {
    layer: above;  /* 在上层绘制 */
}
```

### Offset 偏移

```css
#floating-box {
    offset: 5 3;  /* 右移5, 下移3 */
}
```

---

# 第三部分：样式与主题

## 3.1 Textual CSS 基础

Textual 使用自己的 CSS 变体（文件扩展名 `.tcss`），语法与 Web CSS 类似但不完全相同。

### CSS 文件结构

```css
/* 这是注释 */

Selector {
    property: value;
    another-property: value;
}
```

### 加载 CSS 的三种方式

```python
# 方式1：外部文件（推荐）
class MyApp(App):
    CSS_PATH = "styles.tcss"

# 方式2：多个 CSS 文件
class MyApp(App):
    CSS_PATH = ["base.tcss", "theme.tcss"]

# 方式3：内联 CSS
class MyApp(App):
    CSS = """
    Screen {
        background: $surface;
    }
    """

# 方式4：Widget 内嵌默认 CSS
class MyWidget(Static):
    DEFAULT_CSS = """
    MyWidget {
        background: blue;
    }
    """
```

### Live Reload

开发时使用 `--dev` 标志可以实时预览 CSS 修改：

```bash
textual run my_app.py --dev
```

修改 `.tcss` 文件后会**即时生效**，无需重启。

## 3.2 选择器

### 类型选择器

匹配 Python 类名：

```css
Button {
    background: green;
}

Static {
    color: white;
}
```

### ID 选择器

```python
yield Button("确定", id="ok")
```

```css
#ok {
    background: blue;
}
```

### 类名选择器

```python
yield Button("确认", classes="primary large")
```

```css
.primary {
    background: blue;
}

.primary.large {
    padding: 2 4;
}
```

### 通用选择器

```css
* {
    outline: solid red;  /* 给所有组件加红色边框 */
}

Container > * {
    margin: 1;
}
```

### 伪类选择器

```css
Button:hover {
    background: green;
}

Input:focus {
    border: heavy $primary;
}

Static:disabled {
    color: $text-disabled;
}
```

**常用伪类**：

| 伪类           | 说明           |
| -------------- | -------------- |
| `:hover`       | 鼠标悬停       |
| `:focus`       | 获得焦点       |
| `:blur`        | 未获焦点       |
| `:disabled`    | 禁用状态       |
| `:enabled`     | 启用状态       |
| `:first-child` | 第一个子元素   |
| `:last-child`  | 最后一个子元素 |
| `:dark`        | 暗色主题       |
| `:light`       | 亮色主题       |

## 3.3 组合器

### 后代组合器

```css
#dialog Button {
    background: green;  /* #dialog 内部所有 Button */
}
```

### 子组合器

```css
#sidebar > Button {
    background: green;  /* 仅 #sidebar 的直接子 Button */
}
```

## 3.4 特异性规则

当多个选择器匹配同一个组件时：

1. **ID 数量**多的选择器优先（`#a #b` > `#a`）
2. **类名数量**多的选择器优先（`.a.b` > `.a`）
3. **类型数量**多的选择器优先（`Container Button` > `Button`）
4. `!important` 可以覆盖所有规则

```css
Button:hover {
    background: blue !important;
}
```

## 3.5 CSS 变量与主题系统

### CSS 变量

```css
$my-color: #004578;
$my-border: wide $my-color;

Widget {
    background: $my-color;
    border: $my-border;
}
```

### 主题系统

Textual 内置了多个主题，也可以自定义：

```python
from textual.theme import Theme

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

class MyApp(App):
    def on_mount(self) -> None:
        self.register_theme(my_theme)
        self.theme = "my-theme"
```

### 主题颜色变量

在 CSS 中使用这些变量：

| 变量          | 用途                       |
| ------------- | -------------------------- |
| `$primary`    | 主色调                     |
| `$secondary`  | 次要色                     |
| `$accent`     | 强调色                     |
| `$foreground` | 默认文字颜色               |
| `$background` | 背景色                     |
| `$surface`    | 组件背景色                 |
| `$panel`      | 面板背景色                 |
| `$boost`      | 半透明叠加色               |
| `$success`    | 成功色                     |
| `$warning`    | 警告色                     |
| `$error`      | 错误色                     |
| `$text`       | 自适应文字色（保证可读性） |
| `$text-muted` | 柔和文字色                 |

### 颜色明暗变体

```css
/* 每种颜色都有 3 级加深和 3 级变浅 */
background: $primary-lighten-1;   /* 变浅一级 */
background: $primary-darken-2;    /* 加深两级 */
```

### 颜色预览

```bash
textual colors
```

## 3.6 颜色系统

支持的颜色格式：

```css
/* 命名颜色 */
color: crimson;
color: lime;

/* 十六进制 */
color: #9932CC;
color: #f00;

/* RGB */
color: rgb(255, 0, 0);

/* HSL */
color: hsl(0, 100%, 50%);

/* RGBA (含透明度) */
color: rgba(255, 0, 0, 0.5);
color: #9932CC7f;
```

## 3.7 盒模型：宽高、内外边距、边框

```
┌────────── margin ──────────┐
│ ┌──────── border ────────┐ │
│ │ ┌────── padding ─────┐ │ │
│ │ │                      │ │ │
│ │ │      content         │ │ │
│ │ │                      │ │ │
│ │ └──────────────────────┘ │ │
│ └──────────────────────────┘ │
└──────────────────────────────┘
```

### 常用尺寸属性

```css
Widget {
    width: 50;          /* 固定宽度 50 字符 */
    height: 10;         /* 固定高度 10 行 */
    width: 50%;         /* 父容器的 50% */
    width: 1fr;         /* 占剩余空间 1 等份 */
    width: auto;        /* 根据内容自动调整 */
    min-width: 20;
    max-width: 80;
    min-height: 5;
    max-height: 30;
}
```

### Padding 内边距

```css
Widget {
    padding: 2;                /* 四周 2 格 */
    padding: 1 3;              /* 上下1, 左右3 */
    padding: 1 2 3 4;          /* 上 右 下 左 */
}
```

### Margin 外边距

```css
Widget {
    margin: 2;
    margin: 1 2;
    margin: 1 2 3 4;
}
```

### Border 边框

```css
Widget {
    border: solid white;
    border: heavy $primary;
    border: round green;
    border: tall red;
    border: blank;         /* 占位但不显示 */
    border: none;          /* 无边框 */
}

/* 边框标题 */
Widget {
    border-title: "标题";
    border-title-align: center;
    border-subtitle: "副标题";
}
```

查看所有边框样式：

```bash
textual borders
```

### Outline 轮廓

与 border 类似，但**不占用内容空间**：

```css
Widget {
    outline: heavy yellow;
}
```

## 3.8 单位系统

| 单位   | 说明           | 示例             |
| ------ | -------------- | ---------------- |
| 无单位 | 字符数/行数    | `width: 50;`     |
| `%`    | 父容器百分比   | `width: 50%;`    |
| `fr`   | 弹性比例       | `height: 1fr;`   |
| `auto` | 自动计算       | `width: auto;`   |
| `vw`   | 终端宽度百分比 | `width: 80vw;`   |
| `vh`   | 终端高度百分比 | `height: 100vh;` |
| `w`    | 可用宽度百分比 | `width: 50w;`    |
| `h`    | 可用高度百分比 | `height: 80h;`   |

## 3.9 CSS 嵌套

从 v0.47.0 开始，Textual 支持 CSS 嵌套语法：

```css
/* 传统写法 */
#dialog {
    background: $panel;
}
#dialog Button {
    width: 1fr;
}
#dialog Button.primary {
    background: $success;
}

/* 嵌套写法（等效） */
#dialog {
    background: $panel;

    Button {
        width: 1fr;
        
        &.primary {    /* & 代表父选择器 */
            background: $success;
        }
    }
}
```

## 3.10 常用样式属性速查

```css
Widget {
    /* 布局 */
    display: block | none;
    visibility: visible | hidden;
    layout: vertical | horizontal | grid;
    dock: top | right | bottom | left;
    
    /* 对齐 */
    content-align: center middle;  /* 水平 垂直 */
    text-align: center;
    align: center middle;
    
    /* 文本 */
    color: white;
    text-style: bold | italic | underline | strike | reverse;
    text-wrap: wrap | nowrap;
    text-overflow: ellipsis | fold;
    
    /* 背景 */
    background: darkblue;
    background-tint: blue 50%;
    tint: red 30%;
    
    /* 滚动 */
    overflow: auto | hidden | scroll;
    overflow-x: auto;
    overflow-y: auto;
    
    /* 动画 */
    animation: fade-in 0.3s in_out;
    
    /* 透明度 */
    opacity: 0.8;
}
```

---

# 第四部分：内建 Widget 组件库

## 4.1 Static / Label 静态文本

```python
from textual.widgets import Static, Label

# Static: 可以更新内容的静态组件
class MyStatic(Static):
    def on_mount(self) -> None:
        self.update("[b]初始内容[/b]")
    
    def refresh_content(self, text: str) -> None:
        self.update(text)

# Label: 更轻量的标签
yield Label("简单的标签文本")
```

**内容标记 (Content Markup)**：

使用方括号标签嵌入样式：

```python
widget.update("这是一段 [b]加粗[/b] 文本")
widget.update("[i]斜体[/i] 和 [u]下划线[/u]")
widget.update("[red]红色[/red] 和 [green]绿色[/green] 文字")
widget.update("[bold red on white]加粗红字白底[/bold red on white]")
widget.update("[link=http://example.com]可点击链接[/link]")
```

## 4.2 Button 按钮

```python
from textual.widgets import Button
from textual import on

# 创建按钮
yield Button("普通按钮", id="normal")
yield Button("主要按钮", variant="primary", id="primary")
yield Button("成功按钮", variant="success", id="success")
yield Button("警告按钮", variant="warning", id="warning")
yield Button("错误按钮", variant="error", id="error")

# 禁用按钮
yield Button("禁用", disabled=True)

# 处理按钮事件
@on(Button.Pressed, "#success")
def handle_success(self) -> None:
    self.notify("操作成功！")

# 传统命名方式
def on_button_pressed(self, event: Button.Pressed) -> None:
    if event.button.id == "normal":
        self.notify("普通按钮被点击")
```

## 4.3 Input 输入框

```python
from textual.widgets import Input

# 基础输入
yield Input(placeholder="请输入内容...")
yield Input(placeholder="搜索...", type="text")
yield Input(placeholder="请输入密码", password=True)

# 带验证
yield Input(validator=Integer())

# 带默认值
yield Input(value="默认文本", id="name-input")
```

```python
from textual import on
from textual.widgets import Input

class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="输入点什么，按回车提交", id="main-input")

    @on(Input.Changed, "#main-input")
    def on_changed(self, event: Input.Changed) -> None:
        """实时响应输入变化"""
        self.log(f"当前输入: {event.value}")

    @on(Input.Submitted, "#main-input")
    def on_submitted(self, event: Input.Submitted) -> None:
        """按回车时触发"""
        self.notify(f"你输入了: {event.value}")
```

## 4.4 TextArea 文本区域

```python
from textual.widgets import TextArea

# 多行文本编辑器
yield TextArea(id="editor")

# 带初始内容
yield TextArea("# Hello\n\n这是一个多行编辑器", id="editor")

# 获取内容
editor = self.query_one("#editor", TextArea)
content = editor.text  # 获取全部文本
line_count = editor.line_count  # 行数
```

## 4.5 DataTable 数据表格

```python
from textual.widgets import DataTable

class MyApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable(id="table")

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
        self.table.cursor_type = "row"  # 行选择模式
```

## 4.6 Tree / DirectoryTree 树形结构

```python
from textual.widgets import Tree

class MyApp(App):
    def compose(self) -> ComposeResult:
        tree = Tree("根节点")
        tree.root.add_leaf("叶节点 1")
        branch = tree.root.add_branch("分支 1")
        branch.add_leaf("子叶节点 1")
        branch.add_leaf("子叶节点 2")
        yield tree
```

## 4.7 TabbedContent 标签页

```python
from textual.widgets import TabbedContent, TabPane, Label

class MyApp(App):
    CSS = """
    TabbedContent {
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("聊天", id="chat"):
                yield Label("聊天内容在这里")
            with TabPane("设置", id="settings"):
                yield Label("设置面板")
            with TabPane("日志", id="logs"):
                yield Label("日志输出")
```

## 4.8 Select / OptionList 下拉选择

```python
from textual.widgets import Select

# 下拉选择
yield Select(
    [(label, value) for label, value in [
        ("GPT-4", "gpt-4"),
        ("Claude 3", "claude-3"),
        ("Gemini Pro", "gemini-pro"),
    ]],
    prompt="选择模型",
    id="model-select",
)

# 处理选择变化
@on(Select.Changed, "#model-select")
def on_model_changed(self, event: Select.Changed) -> None:
    self.notify(f"选择了: {event.value}")
```

## 4.9 RichLog / Log 日志

```python
from textual.widgets import RichLog
from rich.text import Text

class MyApp(App):
    def compose(self) -> ComposeResult:
        yield RichLog(id="log", highlight=True, markup=True)

    def on_mount(self) -> None:
        log = self.query_one("#log", RichLog)
        log.write("这是一条日志消息")
        log.write(Text("这是 Rich 格式的", style="bold red"))
        log.write({"key": "value", "nested": [1, 2, 3]})  # 自动 pretty print
```

## 4.10 ProgressBar / LoadingIndicator

```python
from textual.widgets import ProgressBar, LoadingIndicator

# 进度条
yield ProgressBar(total=100, show_eta=True)

# 在代码中更新进度
progress = self.query_one(ProgressBar)
progress.update(progress=50)  # 更新到 50%

# 加载指示器（自动旋转动画）
yield LoadingIndicator()
```

### Widget 的 loading 状态

```python
# 任何 Widget 都可以设置 loading 状态
widget.loading = True   # 显示加载指示器，替换原内容
widget.loading = False  # 恢复原内容
```

## 4.11 Header / Footer 头部底部栏

```python
from textual.widgets import Header, Footer

# Header 显示应用标题和副标题
yield Header()

# Footer 显示当前可用的键盘绑定
yield Footer()

# 自定义 Header
yield Header(show_clock=True)  # 显示时钟
```

## 4.12 其他常用 Widget

```python
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
```

---

# 第五部分：响应式编程 (Reactive)

## 5.1 创建 Reactive 属性

`reactive` 属性是 Textual 最强大的特性之一——赋值时自动触发 UI 刷新：

```python
from textual.reactive import reactive
from textual.widget import Widget
from textual.app import App, ComposeResult
from textual.widgets import Input, Static


class Greeting(Widget):
    who = reactive("World")  # 类型自动推断为 str
    
    def render(self) -> str:
        return f"Hello, {self.who}!"


class ReactiveApp(App):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="输入你的名字")
        yield Greeting()

    def on_input_changed(self, event: Input.Changed) -> None:
        self.query_one(Greeting).who = event.value  # 自动刷新！
```

### 类型注解

```python
# 自动推断
count = reactive(0)  # int

# 显式类型
name: reactive[str | None] = reactive("Paul")

# 动态默认值（每次创建时调用）
start_time = reactive(time)  # 传入 callable
```

## 5.2 智能刷新

Reactive 属性变化时 Textual 自动调用 `render()` 刷新内容：

```python
class Counter(Widget):
    count = reactive(0)
    
    def render(self) -> str:
        return f"计数: {self.count}"
    
    # 自增/自减时只需：
    # self.count += 1  → UI 自动更新！
```

### 关闭刷新

```python
from textual.reactive import var

class MyWidget(Widget):
    internal_state = var(0)  # 变化时 不 触发刷新
```

### 布局刷新

```python
class DynamicSize(Widget):
    size = reactive(10, layout=True)  # 变化时触发 CSS 布局更新
    
    def render(self) -> str:
        return "X" * self.size
```

### Recompose

```python
class DynamicList(Widget):
    items: reactive[list[str]] = reactive(list, recompose=True)
    
    def compose(self) -> ComposeResult:
        for item in self.items:
            yield Label(item)
```

## 5.3 验证 (Validation)

```python
class ScoreWidget(Widget):
    score = reactive(0)
    
    def validate_score(self, score: int) -> int:
        """确保分数在 0-100 之间"""
        return max(0, min(100, score))
    
    def render(self) -> str:
        return f"分数: {self.score}"
```

## 5.4 监听器 (Watch Methods)

```python
class ColorPreview(Widget):
    color = reactive("blue")
    
    def watch_color(self, old_color: str, new_color: str) -> None:
        """颜色变化时执行"""
        self.log(f"颜色从 {old_color} 变为 {new_color}")
        self.styles.background = new_color
```

### 动态监听

```python
def on_mount(self) -> None:
    counter = self.query_one(Counter)
    self.watch(counter, "count", self.update_progress_bar)
```

## 5.5 计算属性 (Compute Methods)

```python
class RGBDisplay(Widget):
    red = reactive(0)
    green = reactive(0)
    blue = reactive(0)
    
    def compute_color(self) -> str:
        """自动根据 red/green/blue 计算"""
        return f"rgb({self.red},{self.green},{self.blue})"
    
    def watch_color(self, color: str) -> None:
        self.styles.background = color
```

## 5.6 数据绑定 (Data Binding)

```python
class ParentApp(App):
    title_text: reactive[str] = reactive("默认标题")
    
    def compose(self) -> ComposeResult:
        yield TitleWidget().data_bind(ParentApp.title_text)
        yield Input()

class TitleWidget(Widget):
    title_text: reactive[str] = reactive("")
    
    def render(self) -> str:
        return self.title_text
```

---

# 第六部分：事件与消息系统

## 6.1 消息队列机制

每个 Widget/App 都有一个消息队列，消息按顺序被处理。这保证了线程安全和事件的有序处理。

## 6.2 消息冒泡

消息默认会向上冒泡到父组件：

```
App
  └── Container
        └── Button  ← 按键事件先到这里
              ↓ 冒泡
        └── Container  ← 然后到这里
              ↓ 冒泡
        App  ← 最后到这里
```

阻止冒泡：

```python
def on_key(self, event) -> None:
    event.stop()  # 停止冒泡
```

## 6.3 自定义消息

```python
from textual.message import Message
from textual.widget import Widget


class ChatMessage(Widget):
    """聊天消息组件"""
    
    class Sent(Message):
        """消息发送事件"""
        def __init__(self, content: str) -> None:
            self.content = content
            super().__init__()
    
    def on_click(self) -> None:
        self.post_message(self.Sent("用户点击了消息"))
```

在 App 中处理：

```python
class ChatApp(App):
    def on_chat_message_sent(self, message: ChatMessage.Sent) -> None:
        self.notify(f"消息发送: {message.content}")
```

## 6.4 @on 装饰器

```python
from textual import on
from textual.widgets import Button, Input


class MyApp(App):
    @on(Button.Pressed, "#send")
    def handle_send(self) -> None:
        self.notify("发送按钮被点击")
    
    @on(Button.Pressed, ".danger")
    def handle_danger(self) -> None:
        self.notify("危险按钮被点击")
    
    @on(Input.Submitted, "#search")
    def handle_search(self, event: Input.Submitted) -> None:
        self.notify(f"搜索: {event.value}")
```

## 6.5 键盘绑定 (Key Bindings)

```python
from textual.app import App
from textual.binding import Binding


class MyApp(App):
    BINDINGS = [
        Binding("ctrl+s", "save", "保存", show=True),
        Binding("ctrl+q", "quit", "退出"),
        Binding("up,k", "scroll_up", "上移"),
        Binding("down,j", "scroll_down", "下移"),
        Binding("escape", "cancel", "取消", show=False),
    ]
    
    def action_save(self) -> None:
        self.notify("已保存！")
    
    def action_quit(self) -> None:
        self.exit()
    
    def action_scroll_up(self) -> None:
        self.scroll_up(animate=True)
```

### Widget 级别绑定

```python
class MyWidget(Static, can_focus=True):
    BINDINGS = [
        Binding("enter", "select", "选择"),
        Binding("space", "toggle", "切换"),
    ]
    
    def action_select(self) -> None:
        self.notify("选中")
```

## 6.6 Actions 系统

Actions 是绑定到按键或程序触发的命名操作：

```python
# 在 CSS/TCSS 中使用 action
# 键盘绑定中的 action 字符串
BINDINGS = [
    ("q", "app.quit", "退出"),        # 调用 app.action_quit
    ("d", "toggle_dark", "切换暗色"),  # 调用 self.action_toggle_dark
]

# 在代码中触发
self.run_action("save")
self.run_action("app.quit")
```

---

# 第七部分：自定义 Widget

## 7.1 从 Widget 继承

```python
from textual.widget import Widget
from textual.app import App, ComposeResult, RenderResult


class GreetingWidget(Widget):
    """自定义问候组件"""
    
    def __init__(self, name: str = "World") -> None:
        self.name = name
        super().__init__()
    
    def render(self) -> RenderResult:
        return f"Hello, [b]{self.name}[/b]!"


class MyApp(App):
    def compose(self) -> ComposeResult:
        yield GreetingWidget("Textual")
```

## 7.2 从 Static 继承

Static 缓存渲染结果并提供 `update()` 方法，通常是更好的起点：

```python
from textual.widgets import Static
from textual.reactive import reactive


class StatusWidget(Static):
    """状态显示组件"""
    
    status = reactive("待机中")
    
    def render(self) -> str:
        return f"状态: [b]{self.status}[/b]"
    
    def set_status(self, new_status: str) -> None:
        self.status = new_status  # 自动刷新
```

## 7.3 默认 CSS (DEFAULT_CSS)

将组件的 CSS 与代码打包在一起：

```python
class Card(Static):
    DEFAULT_CSS = """
    Card {
        width: 100%;
        height: auto;
        min-height: 5;
        padding: 1 2;
        margin: 1 0;
        background: $surface;
        border: solid $primary;
        border-title-style: bold;
    }
    """
    
    BORDER_TITLE = "Card"
    
    def __init__(self, title: str, content: str) -> None:
        self.content_text = content
        self.BORDER_TITLE = title
        super().__init__(content)
```

> 💡 DEFAULT_CSS 默认作用域限定在本组件内（Scoped CSS），不会影响外部。

## 7.4 复合组件 (Compound Widgets)

将多个 Widget 组合成新的复合组件：

```python
from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.containers import Horizontal, Vertical
from textual.widgets import Input, Label, Button


class FormField(Widget):
    """带标签的输入字段"""
    
    DEFAULT_CSS = """
    FormField {
        layout: horizontal;
        height: auto;
        margin: 1 0;
    }
    FormField Label {
        width: 15;
        content-align: right middle;
        padding-right: 1;
    }
    FormField Input {
        width: 1fr;
    }
    """
    
    def __init__(self, label_text: str, placeholder: str = "") -> None:
        self.label_text = label_text
        self.placeholder = placeholder
        super().__init__()
    
    def compose(self) -> ComposeResult:
        yield Label(self.label_text)
        yield Input(placeholder=self.placeholder)


class MyApp(App):
    def compose(self) -> ComposeResult:
        yield FormField("用户名:", "请输入用户名")
        yield FormField("密码:", "请输入密码")
        yield Button("登录", id="login", variant="primary")
```

## 7.5 渲染 Rich 对象

使用 Rich 库的高级渲染能力：

```python
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax
from rich.markdown import Markdown as RichMarkdown
from textual.widgets import Static


class CodeViewer(Static):
    def on_mount(self) -> None:
        # 渲染语法高亮代码
        code = Syntax(
            'def hello():\n    print("Hello, World!")',
            "python",
            theme="monokai",
        )
        self.update(Panel(code, title="Python 代码"))
```

## 7.6 Line API 高级渲染

对于高性能的自定义渲染，可以使用 Line API：

```python
from textual.widget import Widget
from textual.strip import Strip
from rich.segment import Segment
from rich.style import Style


class ColorBar(Widget):
    """颜色条组件"""
    
    def render_line(self, y: int) -> Strip:
        """逐行渲染"""
        width = self.size.width
        # 每行不同颜色
        hue = int(y / self.size.height * 360)
        style = Style.parse(f"hsl({hue}, 70%, 50%)")
        segment = Segment("█" * width, style)
        return Strip([segment], width)
```

## 7.7 Tooltips 与 Loading 状态

```python
class MyButton(Button):
    def on_mount(self) -> None:
        self.tooltip = "这是一个提示信息"
    
    def show_loading(self) -> None:
        self.loading = True  # 显示旋转加载指示器
    
    def hide_loading(self) -> None:
        self.loading = False  # 恢复显示
```

---

# 第八部分：Screen 屏幕管理

## 8.1 什么是 Screen

Screen 是占满整个终端的容器，类似网页中的"页面"。App 始终至少有一个 Screen（默认 Screen）。

## 8.2 创建与切换 Screen

```python
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Label, Footer


class HomeScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("主页内容")
        yield Footer()

    BINDINGS = [("s", "app.push_screen('settings')", "设置")]


class SettingsScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("设置页面")
        yield Footer()

    BINDINGS = [("escape", "app.pop_screen", "返回")]


class MyApp(App):
    SCREENS = {
        "home": HomeScreen,
        "settings": SettingsScreen,
    }

    def on_mount(self) -> None:
        self.push_screen("home")
```

## 8.3 ModalScreen 模态对话框

```python
from textual.screen import ModalScreen
from textual.widgets import Button, Label, Static
from textual.containers import Grid


class ConfirmDialog(ModalScreen[bool]):
    """确认对话框"""
    
    CSS = """
    ConfirmDialog {
        align: center middle;
    }
    #dialog {
        grid-size: 2;
        grid-gutter: 1 2;
        grid-rows: 1fr 3;
        width: 60;
        height: auto;
        border: thick $background 80%;
        background: $surface;
        padding: 1;
    }
    #question {
        column-span: 2;
        content-align: center middle;
    }
    """
    
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__()
    
    def compose(self) -> ComposeResult:
        yield Grid(
            Label(self.message, id="question"),
            Button("确定", variant="error", id="confirm"),
            Button("取消", variant="primary", id="cancel"),
            id="dialog",
        )
    
    @on(Button.Pressed, "#confirm")
    def confirm(self) -> None:
        self.dismiss(True)
    
    @on(Button.Pressed, "#cancel")
    def cancel(self) -> None:
        self.dismiss(False)


# 使用
class MyApp(App):
    BINDINGS = [("q", "confirm_quit", "退出")]
    
    def action_confirm_quit(self) -> None:
        def on_result(result: bool | None) -> None:
            if result:
                self.exit()
        
        self.push_screen(ConfirmDialog("确定要退出吗？"), on_result)
```

## 8.4 从 Screen 返回数据

```python
from textual import work
from textual.widgets import Button


class InputDialog(ModalScreen[str]):
    """输入对话框，返回用户输入"""
    
    def compose(self) -> ComposeResult:
        yield Input(placeholder="请输入...", id="user-input")
        yield Button("确定", id="ok")
    
    @on(Button.Pressed, "#ok")
    def submit(self) -> None:
        value = self.query_one(Input).value
        self.dismiss(value)


class MyApp(App):
    @work
    async def on_mount(self) -> None:
        result = await self.push_screen_wait(InputDialog())
        if result:
            self.notify(f"你输入了: {result}")
```

## 8.5 多模式 (Modes)

```python
class MyApp(App):
    MODES = {
        "dashboard": "main",
        "settings": "settings",
        "help": "help",
    }
    
    BINDINGS = [
        ("d", "switch_mode('dashboard')", "仪表板"),
        ("s", "switch_mode('settings')", "设置"),
        ("h", "switch_mode('help')", "帮助"),
    ]
```

---

# 第九部分：Workers 并发任务

## 9.1 为什么需要 Workers

直接在事件处理器中执行耗时操作会**阻塞 UI**：

```python
# ❌ 错误示例：阻塞 UI
async def on_input_changed(self, event: Input.Changed) -> None:
    # 这会导致 UI 卡顿！
    response = await httpx.AsyncClient().get(url)
    self.update_display(response)

# ✅ 正确示例：使用 Worker
async def on_input_changed(self, event: Input.Changed) -> None:
    self.run_worker(self.fetch_data(event.value), exclusive=True)
```

## 9.2 @work 装饰器

```python
from textual import work
from textual.app import App, ComposeResult
from textual.widgets import Input, Static
import httpx


class WeatherApp(App):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="输入城市名")
        yield Static(id="weather")

    @on(Input.Submitted)
    def on_search(self, event: Input.Submitted) -> None:
        self.get_weather(event.value)

    @work(exclusive=True)  # exclusive: 取消之前的同名任务
    async def get_weather(self, city: str) -> None:
        widget = self.query_one("#weather", Static)
        widget.loading = True  # 显示加载状态
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.get(f"https://wttr.in/{city}")
                widget.update(resp.text)
        except Exception as e:
            widget.update(f"错误: {e}")
        finally:
            widget.loading = False
```

## 9.3 run_worker 方法

```python
# 等效于 @work 装饰器
worker = self.run_worker(
    self.get_weather(city),
    exclusive=True,        # 取消之前的任务
    exit_on_error=False,   # 出错不退出应用
)
```

## 9.4 线程 Workers

对于不支持 async 的 API（如 `requests`、`urllib`）：

```python
from textual import work
from textual.worker import get_current_worker


class MyApp(App):
    @work(exclusive=True, thread=True)
    def heavy_computation(self) -> None:
        """在后台线程运行"""
        worker = get_current_worker()
        
        # 耗时计算...
        result = some_slow_function()
        
        if not worker.is_cancelled:
            # 必须通过 call_from_thread 更新 UI
            self.call_from_thread(self.update_result, result)
    
    def update_result(self, result) -> None:
        self.query_one(Static).update(str(result))
```

> ⚠️ 线程 Worker 中**不能直接操作 UI**，必须使用 `self.call_from_thread()`。

## 9.5 Worker 生命周期与事件

| 状态        | 说明                             |
| ----------- | -------------------------------- |
| `PENDING`   | 已创建但未启动                   |
| `RUNNING`   | 正在运行                         |
| `SUCCESS`   | 成功完成，结果在 `worker.result` |
| `ERROR`     | 发生错误，异常在 `worker.error`  |
| `CANCELLED` | 被取消                           |

```python
from textual.worker import Worker


class MyApp(App):
    def on_worker_state_changed(self, event: Worker.StateChanged) -> None:
        self.log(f"Worker {event.worker} 状态: {event.state}")
```

---

# 第十部分：调试与测试

## 10.1 DevTools 开发者工具

```bash
# 开发模式运行（支持 CSS 热更新）
textual run my_app.py --dev

# 打开 Textual 控制台（查看日志、消息）
textual console
```

在代码中使用日志：

```python
self.log("调试信息", variable=some_value)
self.log.debug("详细调试")
self.log.warning("警告信息")
self.log.error("错误信息")
```

快捷键（在 `--dev` 模式下）：

| 快捷键   | 功能              |
| -------- | ----------------- |
| `Ctrl+T` | 打开开发者工具    |
| `Ctrl+P` | 打开命令面板      |
| `F12`    | 切换 CSS 网格视图 |

## 10.2 自动化测试

```python
from textual.app import App, ComposeResult
from textual.widgets import Button, Label


class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Button("点击", id="click-me")
        yield Label("等待...", id="status")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query_one("#status", Label).update("已点击！")


# 测试代码
async def test_button_click():
    async with MyApp().run_test() as pilot:
        # pilot 是测试助手
        await pilot.click("#click-me")
        assert app.query_one("#status", Label).renderable == "已点击！"


async def test_key_binding():
    async with MyApp().run_test() as pilot:
        await pilot.press("escape")
        # 验证状态...
```

```python
# 带初始状态的测试
async def test_with_initial_state():
    app = MyApp()
    async with app.run_test() as pilot:
        # 应用已启动，可以操作
        await pilot.press("ctrl+s")
        await pilot.pause()  # 等待消息处理完成
```

---

# 第十一部分：实战 —— 构建 Agent TUI 界面

## 11.1 需求分析与架构设计

### 功能需求

一个完整的 AI Agent TUI 界面需要：

1. **聊天区域**：显示用户消息和 AI 回复（支持 Markdown 渲染）
2. **输入区域**：用户输入消息的文本框
3. **侧边栏**：会话历史管理
4. **模型选择**：选择不同的 LLM 模型
5. **流式输出**：AI 回复时的打字效果
6. **工具面板**：显示 Function Calling / Tool Use 过程
7. **状态栏**：显示 Token 数、响应时间等信息
8. **主题美化**：专业的视觉设计

### 项目结构

```
agent-tui/
├── agent_tui.py        # 主应用入口
├── styles.tcss         # 外部 CSS 样式
├── screens/            # Screen 屏幕
│   ├── __init__.py
│   ├── chat.py         # 聊天主屏幕
│   └── settings.py     # 设置屏幕
├── widgets/            # 自定义 Widget
│   ├── __init__.py
│   ├── chat_message.py # 聊天消息气泡
│   ├── chat_input.py   # 输入区域
│   ├── sidebar.py      # 会话侧边栏
│   └── tool_panel.py   # 工具调用面板
├── models/             # 数据模型
│   ├── __init__.py
│   └── message.py      # 消息数据结构
└── services/           # 业务逻辑
    ├── __init__.py
    └── agent.py        # Agent 逻辑
```

## 11.2 Step 1: 项目结构

创建项目目录：

```bash
mkdir agent-tui
cd agent-tui
mkdir -p screens widgets models services
touch __init__.py screens/__init__.py widgets/__init__.py models/__init__.py services/__init__.py
```

## 11.3 Step 2: 基础骨架

创建 `agent_tui.py`：

```python
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Header, Footer, Static, Label


class AgentTuiApp(App):
    """AI Agent TUI 应用"""
    
    TITLE = "🤖 Agent TUI"
    SUB_TITLE = "与 AI 对话"
    
    CSS_PATH = "styles.tcss"
    
    BINDINGS = [
        Binding("ctrl+q", "quit", "退出"),
        Binding("ctrl+n", "new_chat", "新对话"),
        Binding("ctrl+l", "clear", "清空"),
        Binding("ctrl+p", "command_palette", "命令面板", show=False),
    ]
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static("欢迎使用 Agent TUI！按 Ctrl+N 开始新对话", id="main-content")
        yield Footer()
    
    def action_new_chat(self) -> None:
        self.notify("新对话已创建")
    
    def action_clear(self) -> None:
        self.notify("已清空聊天记录")


if __name__ == "__main__":
    app = AgentTuiApp()
    app.run()
```

创建 `styles.tcss`：

```css
/* 全局样式 */
Screen {
    background: $surface;
}

/* Header 样式优化 */
Header {
    dock: top;
    background: $primary;
}

/* Footer */
Footer {
    dock: bottom;
}

/* 主内容区域 */
#main-content {
    width: 100%;
    height: 1fr;
    content-align: center middle;
    color: $text-muted;
}
```

## 11.4 Step 3: 聊天消息区域

创建 `widgets/chat_message.py`：

```python
from textual.widget import Widget
from textual.widgets import Static, Label
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from datetime import datetime


class ChatMessage(Widget):
    """聊天气泡组件"""
    
    DEFAULT_CSS = """
    ChatMessage {
        width: 100%;
        height: auto;
        margin: 0 0 1 0;
        padding: 0 1;
    }
    
    ChatMessage.user {
        align: right middle;
    }
    
    ChatMessage.assistant {
        align: left middle;
    }
    
    .message-container {
        width: 85%;
        height: auto;
        padding: 1 2;
        margin: 0 1;
    }
    
    .message-container.user {
        background: $primary;
        color: $text;
        border: solid $primary;
        margin-left: 15%;
    }
    
    .message-container.assistant {
        background: $panel;
        color: $text;
        border: solid $secondary;
        margin-right: 15%;
    }
    
    .message-role {
        text-style: bold;
        text-opacity: 80%;
        margin-bottom: 0;
    }
    
    .message-content {
        width: 100%;
        height: auto;
    }
    
    .message-time {
        text-style: italic;
        text-opacity: 50%;
        margin-top: 0;
    }
    """
    
    role: reactive[str] = reactive("user")
    
    def __init__(self, role: str, content: str, timestamp: datetime | None = None) -> None:
        self.msg_role = role
        self.msg_content = content
        self.msg_time = timestamp or datetime.now()
        super().__init__()
        self.add_class(role)
    
    def compose(self):
        with Vertical(classes=f"message-container {self.msg_role}"):
            yield Label(
                f"{'🧑 你' if self.msg_role == 'user' else '🤖 AI'}",
                classes="message-role"
            )
            yield Static(self.msg_content, classes="message-content")
            yield Label(
                self.msg_time.strftime("%H:%M:%S"),
                classes="message-time"
            )
```

## 11.5 Step 4: 输入区域与发送

创建 `widgets/chat_input.py`：

```python
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Input, Button, Label, Select
from textual.widget import Widget
from textual import on


class ChatInput(Widget):
    """聊天输入区域"""
    
    DEFAULT_CSS = """
    ChatInput {
        dock: bottom;
        height: 5;
        background: $panel;
        padding: 1 2;
        border-top: solid $primary;
    }
    
    #input-row {
        height: 3;
        width: 100%;
    }
    
    #user-input {
        width: 1fr;
        height: 3;
    }
    
    #send-btn {
        width: 15;
        min-width: 15;
        margin-left: 1;
    }
    
    #model-select {
        width: 25;
        margin-left: 1;
    }
    
    #status-label {
        dock: top;
        height: 1;
        padding: 0 1;
        color: $text-muted;
    }
    """
    
    def compose(self) -> ComposeResult:
        yield Label("准备就绪", id="status-label")
        with Horizontal(id="input-row"):
            yield Input(
                placeholder="输入消息... (Enter 发送, Shift+Enter 换行)",
                id="user-input",
            )
            yield Select(
                [
                    ("GPT-4o", "gpt-4o"),
                    ("Claude 3.5", "claude-3.5-sonnet"),
                    ("Gemini Pro", "gemini-pro"),
                ],
                value="gpt-4o",
                id="model-select",
            )
            yield Button("发送 ➤", id="send-btn", variant="primary")
    
    def on_mount(self) -> None:
        self.query_one("#user-input", Input).focus()
    
    def get_input(self) -> str:
        return self.query_one("#user-input", Input).value
    
    def clear_input(self) -> None:
        self.query_one("#user-input", Input).value = ""
    
    def set_status(self, text: str) -> None:
        self.query_one("#status-label", Label).update(text)
```

## 11.6 Step 5: 流式输出与打字效果

在 `services/agent.py` 中模拟 AI 流式响应：

```python
import asyncio
from typing import AsyncGenerator


async def mock_stream_response(message: str) -> AsyncGenerator[str, None]:
    """模拟 AI 流式响应（实际项目替换为 API 调用）"""
    responses = [
        f"我收到你的消息了：「{message}」。\n\n",
        "让我来分析一下这个问题...\n\n",
        "## 分析结果\n\n",
        "根据我的理解，",
        "这个问题涉及到几个方面：\n\n",
        "1. **数据处理** - 需要对输入数据进行清洗\n",
        "2. **模型推理** - 使用适当的模型进行推理\n",
        "3. **结果展示** - 将结果格式化输出\n\n",
        "如果你需要更详细的信息，请告诉我！ 😊",
    ]
    
    for chunk in responses:
        yield chunk
        await asyncio.sleep(0.05)  # 模拟网络延迟
```

## 11.7 Step 6: 侧边栏 —— 会话管理

创建 `widgets/sidebar.py`：

```python
from textual.widget import Widget
from textual.widgets import Label, Button, ListView, ListItem, Static, Input
from textual.containers import Vertical, Horizontal
from textual.reactive import reactive
from textual import on
from datetime import datetime


class SidebarItem(ListItem):
    """侧边栏会话项"""
    
    def __init__(self, title: str, chat_id: str) -> None:
        self.chat_id = chat_id
        super().__init__(Label(title))


class Sidebar(Widget):
    """会话管理侧边栏"""
    
    DEFAULT_CSS = """
    Sidebar {
        dock: left;
        width: 30;
        background: $panel;
        border-right: solid $primary;
        padding: 1;
    }
    
    .sidebar-header {
        height: auto;
        padding: 1 0;
        text-style: bold;
        color: $primary;
    }
    
    #new-chat-btn {
        width: 100%;
        margin: 1 0;
    }
    
    #search-input {
        width: 100%;
        margin-bottom: 1;
    }
    
    #chat-list {
        height: 1fr;
        background: $panel;
    }
    
    #chat-list ListItem {
        padding: 1 1;
        margin: 0 0 0 0;
    }
    
    #chat-list ListItem:hover {
        background: $boost;
    }
    
    #chat-list ListItem.-active {
        background: $primary;
        color: $text;
    }
    """
    
    def compose(self):
        yield Label("📋 会话列表", classes="sidebar-header")
        yield Button("+ 新对话", id="new-chat-btn", variant="primary")
        yield Input(placeholder="🔍 搜索...", id="search-input")
        yield ListView(
            SidebarItem("新会话 1", "chat-1"),
            SidebarItem("Python 问题", "chat-2"),
            SidebarItem("代码审查", "chat-3"),
            SidebarItem("项目规划", "chat-4"),
            id="chat-list",
        )
    
    @on(Button.Pressed, "#new-chat-btn")
    def new_chat(self) -> None:
        self.notify("创建新对话", severity="information")
```

## 11.8 Step 7: 主题美化

创建自定义主题和完整样式。更新 `styles.tcss`：

```css
/* ========== 全局 ========== */
Screen {
    background: $surface;
}

Header {
    background: $primary;
    color: $text;
}

Footer {
    background: $panel;
}

/* ========== 主布局 ========== */
#app-container {
    width: 100%;
    height: 1fr;
}

#chat-area {
    width: 1fr;
    height: 1fr;
    overflow-y: auto;
    padding: 1 2;
}

/* ========== 聊天气泡 ========== */
.user-message {
    width: 80%;
    margin-left: 20%;
    margin-bottom: 1;
    padding: 1 2;
    background: $primary;
    color: $text;
    border: tall $primary-darken-1;
    border-radius: 0;
}

.assistant-message {
    width: 80%;
    margin-right: 20%;
    margin-bottom: 1;
    padding: 1 2;
    background: $panel;
    color: $text;
    border: tall $secondary;
}

.role-label {
    text-style: bold;
    text-opacity: 70%;
    margin-bottom: 0;
}

.content-text {
    width: 100%;
    height: auto;
}

.timestamp {
    text-style: italic;
    text-opacity: 40%;
    text-align: right;
    margin-top: 0;
}

/* ========== 工具调用面板 ========== */
.tool-panel {
    dock: right;
    width: 40;
    background: $panel;
    border-left: solid $accent;
    padding: 1;
    overflow-y: auto;
}

.tool-panel.hidden {
    display: none;
}

.tool-entry {
    padding: 1;
    margin-bottom: 1;
    background: $surface;
    border: solid $secondary-darken-1;
}

.tool-name {
    text-style: bold;
    color: $accent;
}

.tool-status {
    text-style: italic;
}

/* ========== 打字动画 ========== */
.typing-indicator {
    content-align: left middle;
    color: $text-muted;
}

/* ========== 滚动条美化 ========== */
$scrollbar: $panel;
$scrollbar-hover: $panel-lighten-1;
$scrollbar-active: $panel-lighten-2;
```

## 11.9 Step 8: 工具面板与 Function Calling

创建 `widgets/tool_panel.py`：

```python
from textual.widget import Widget
from textual.widgets import Static, Label
from textual.containers import Vertical, ScrollableContainer
from textual.reactive import reactive
from dataclasses import dataclass
from enum import Enum


class ToolStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class ToolCall:
    name: str
    args: dict
    status: ToolStatus = ToolStatus.PENDING
    result: str = ""


class ToolPanel(Widget):
    """工具调用面板"""
    
    DEFAULT_CSS = """
    ToolPanel {
        dock: right;
        width: 40;
        background: $panel;
        border-left: solid $accent;
        padding: 1;
        display: none;
    }
    
    ToolPanel.visible {
        display: block;
    }
    
    .panel-title {
        text-style: bold;
        color: $accent;
        padding: 1 0;
        border-bottom: solid $accent;
        margin-bottom: 1;
    }
    
    .tool-entry {
        padding: 1;
        margin: 0 0 1 0;
        background: $surface;
        border: solid $secondary-darken-1;
    }
    
    .tool-entry.running {
        border: solid $warning;
    }
    
    .tool-entry.completed {
        border: solid $success;
    }
    
    .tool-entry.failed {
        border: solid $error;
    }
    
    .tool-name {
        text-style: bold;
        color: $accent;
    }
    
    .tool-status {
        text-style: italic;
    }
    """
    
    is_visible: reactive[bool] = reactive(False)
    
    def watch_is_visible(self, visible: bool) -> None:
        if visible:
            self.add_class("visible")
        else:
            self.remove_class("visible")
    
    def compose(self):
        yield Label("🔧 工具面板", classes="panel-title")
        yield Static("暂无工具调用", id="tools-list")
    
    def add_tool_call(self, tool: ToolCall) -> None:
        """添加一个工具调用"""
        self.is_visible = True
        self.query_one("#tools-list").update(
            f"[b]{tool.name}[/b]\n{tool.args}\n[italic]运行中...[/italic]"
        )
    
    def update_tool_status(self, tool: ToolCall) -> None:
        """更新工具调用状态"""
        status_colors = {
            ToolStatus.COMPLETED: "[green]✓ 完成[/green]",
            ToolStatus.FAILED: "[red]✗ 失败[/red]",
            ToolStatus.RUNNING: "[yellow]● 运行中[/yellow]",
            ToolStatus.PENDING: "[dim]○ 等待中[/dim]",
        }
        status_text = status_colors.get(tool.status, "")
        self.query_one("#tools-list").update(
            f"[b]{tool.name}[/b]\n{tool.args}\n{status_text}"
        )
```

## 11.10 Step 9: Markdown 渲染

使用内建的 Markdown Widget 渲染 AI 回复：

```python
from textual.widgets import Markdown, MarkdownViewer


# 在 ChatMessage 中支持 Markdown
class ChatMessageMarkdown(Widget):
    """支持 Markdown 渲染的聊天消息"""
    
    def __init__(self, role: str, content: str) -> None:
        self.msg_role = role
        self.msg_content = content
        super().__init__()
    
    def compose(self):
        yield Label(
            f"{'🧑 你' if self.msg_role == 'user' else '🤖 AI'}",
            classes="role-label"
        )
        if self.msg_role == "assistant":
            yield Markdown(self.msg_content, classes="content-text")
        else:
            yield Static(self.msg_content, classes="content-text")
```

## 11.11 Step 10: 快捷键与命令面板

```python
class AgentTuiApp(App):
    BINDINGS = [
        Binding("ctrl+q", "quit", "退出应用"),
        Binding("ctrl+n", "new_chat", "新对话"),
        Binding("ctrl+l", "clear", "清空聊天"),
        Binding("ctrl+b", "toggle_sidebar", "切换侧边栏"),
        Binding("ctrl+t", "toggle_tools", "切换工具面板"),
        Binding("ctrl+shift+c", "copy_last", "复制最后回复"),
        Binding("f1", "show_help", "帮助"),
        Binding("ctrl+comma", "show_settings", "设置"),
    ]
    
    def action_toggle_sidebar(self) -> None:
        sidebar = self.query_one(Sidebar)
        sidebar.display = not sidebar.display
    
    def action_toggle_tools(self) -> None:
        panel = self.query_one(ToolPanel)
        panel.is_visible = not panel.is_visible
    
    def action_new_chat(self) -> None:
        chat_area = self.query_one("#chat-area")
        chat_area.remove_children()
        self.notify("新对话已开始")
```

## 11.12 完整代码参考

### 完整的 `agent_tui.py`

```python
"""
Agent TUI - AI Agent 终端界面
完整实现参考
"""
import asyncio
from datetime import datetime

from textual import on, work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import (
    Button,
    Footer,
    Header,
    Input,
    Label,
    ListView,
    ListItem,
    Select,
    Static,
)

from widgets.chat_message import ChatMessage
from widgets.sidebar import Sidebar
from widgets.tool_panel import ToolPanel, ToolCall, ToolStatus


class ChatScreen(Screen):
    """聊天主屏幕"""
    
    CSS = """
    Screen {
        layout: horizontal;
    }
    
    #sidebar {
        dock: left;
        width: 30;
    }
    
    #main-panel {
        width: 1fr;
        height: 100%;
        layout: vertical;
    }
    
    #chat-scroll {
        width: 1fr;
        height: 1fr;
        padding: 1 2;
    }
    
    #chat-scroll ChatMessage {
        margin-bottom: 0;
    }
    
    #input-area {
        dock: bottom;
        height: 5;
        background: $panel;
        padding: 1 2;
        border-top: solid $primary;
    }
    
    #input-row {
        height: 3;
        width: 100%;
    }
    
    #user-input {
        width: 1fr;
    }
    
    #send-btn {
        width: 12;
        margin-left: 1;
    }
    
    #model-select {
        width: 22;
        margin-left: 1;
    }
    
    #status-bar {
        dock: bottom;
        height: 1;
        background: $panel;
        padding: 0 2;
        color: $text-muted;
    }
    
    #tool-panel {
        dock: right;
        width: 35;
    }
    """
    
    BINDINGS = [
        Binding("ctrl+n", "new_chat", "新对话"),
        Binding("ctrl+b", "toggle_sidebar", "侧边栏"),
        Binding("ctrl+t", "toggle_tools", "工具面板"),
    ]
    
    sidebar_visible: reactive[bool] = reactive(True)
    tools_visible: reactive[bool] = reactive(False)
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Sidebar(id="sidebar")
        with Vertical(id="main-panel"):
            yield VerticalScroll(id="chat-scroll")
            with Horizontal(id="input-area"):
                yield Input(
                    placeholder="输入消息... (Enter 发送)",
                    id="user-input",
                )
                yield Select(
                    [
                        ("GPT-4o", "gpt-4o"),
                        ("Claude 3.5", "claude-3.5"),
                        ("Gemini Pro", "gemini"),
                    ],
                    value="gpt-4o",
                    id="model-select",
                )
                yield Button("发送 ➤", id="send-btn", variant="primary")
        yield ToolPanel(id="tool-panel")
        yield Label("就绪 | 模型: GPT-4o | Tokens: 0", id="status-bar")
        yield Footer()
    
    def on_mount(self) -> None:
        """挂载后显示欢迎消息"""
        self.add_system_message("欢迎使用 Agent TUI！输入消息开始对话。")
        self.query_one("#user-input", Input).focus()
    
    def add_user_message(self, text: str) -> None:
        """添加用户消息"""
        chat = self.query_one("#chat-scroll")
        chat.mount(
            ChatMessage("user", text),
            after=0,  # 在顶部添加（聊天反转显示）
        )
        chat.scroll_end(animate=True)
    
    def add_assistant_message(self, text: str) -> None:
        """添加 AI 回复"""
        chat = self.query_one("#chat-scroll")
        chat.mount(
            ChatMessage("assistant", text),
            after=0,
        )
        chat.scroll_end(animate=True)
    
    def add_system_message(self, text: str) -> None:
        """添加系统消息"""
        chat = self.query_one("#chat-scroll")
        chat.mount(
            Static(f"[dim][系统] {text}[/dim]", classes="system-message"),
            after=0,
        )
    
    @on(Input.Submitted, "#user-input")
    @on(Button.Pressed, "#send-btn")
    def handle_send(self) -> None:
        """发送消息"""
        input_widget = self.query_one("#user-input", Input)
        text = input_widget.value.strip()
        if not text:
            return
        
        self.add_user_message(text)
        input_widget.value = ""
        self.query_one("#status-bar", Label).update("思考中...")
        
        # 启动 Worker 获取 AI 回复
        self.get_ai_response(text)
    
    @work(exclusive=True)
    async def get_ai_response(self, message: str) -> None:
        """后台获取 AI 回复"""
        tool_panel = self.query_one("#tool-panel", ToolPanel)
        
        # 模拟工具调用
        tool = ToolCall(name="search_knowledge", args={"query": message})
        tool_panel.add_tool_call(tool)
        await asyncio.sleep(0.5)
        tool.status = ToolStatus.COMPLETED
        tool_panel.update_tool_status(tool)
        
        # 模拟流式输出
        full_response = ""
        chat = self.query_one("#chat-scroll")
        
        # 创建一个临时消息用于流式更新
        temp_msg = ChatMessage("assistant", "...")
        chat.mount(temp_msg, after=0)
        
        response_chunks = [
            f"关于「{message}」，",
            "我来为你分析一下：\n\n",
            "## 分析\n\n",
            "这是通过 **Agent TUI** 界面发送的消息。",
            "在实际项目中，这里会调用 LLM API 获取回复。\n\n",
            "### 功能特性\n\n",
            "- ✅ Markdown 渲染\n",
            "- ✅ 流式输出\n",
            "- ✅ 工具调用\n",
            "- ✅ 会话管理\n",
            "- ✅ 主题切换\n\n",
            "需要更多帮助吗？ 😊",
        ]
        
        for chunk in response_chunks:
            full_response += chunk
            temp_msg.update(full_response)
            chat.scroll_end(animate=False)
            await asyncio.sleep(0.03)
        
        # 更新状态栏
        tokens = len(full_response.split())
        self.query_one("#status-bar", Label).update(
            f"就绪 | 模型: GPT-4o | 回复: {tokens} tokens"
        )
    
    def action_new_chat(self) -> None:
        """清空并开始新对话"""
        chat = self.query_one("#chat-scroll")
        chat.remove_children()
        self.add_system_message("新对话已开始。")
        self.notify("🆕 新对话已创建")
    
    def action_toggle_sidebar(self) -> None:
        """切换侧边栏显示"""
        self.sidebar_visible = not self.sidebar_visible
        sidebar = self.query_one("#sidebar")
        sidebar.display = self.sidebar_visible
    
    def action_toggle_tools(self) -> None:
        """切换工具面板"""
        self.tools_visible = not self.tools_visible
        panel = self.query_one("#tool-panel", ToolPanel)
        panel.is_visible = self.tools_visible


class AgentTuiApp(App):
    """Agent TUI 主应用"""
    
    TITLE = "🤖 Agent TUI"
    SUB_TITLE = "AI Agent 终端界面"
    CSS_PATH = "styles.tcss"
    
    BINDINGS = [
        Binding("ctrl+q", "quit", "退出"),
        Binding("ctrl+p", "command_palette", show=False),
    ]
    
    def compose(self) -> ComposeResult:
        yield ChatScreen()


if __name__ == "__main__":
    app = AgentTuiApp()
    app.run()
```

---

# 附录：常用 API 速查表

## App 常用方法

| 方法                                    | 说明                  |
| --------------------------------------- | --------------------- |
| `self.exit(result)`                     | 退出应用              |
| `self.notify(message)`                  | 显示通知              |
| `self.bell()`                           | 响铃                  |
| `self.beep()`                           | 蜂鸣                  |
| `self.run_worker(coro)`                 | 启动 Worker           |
| `self.query(selector)`                  | 查询所有匹配的 Widget |
| `self.query_one(selector)`              | 查询单个 Widget       |
| `self.mount(*widgets)`                  | 挂载 Widget           |
| `self.push_screen(screen)`              | 压入屏幕              |
| `self.pop_screen()`                     | 弹出屏幕              |
| `self.switch_screen(screen)`            | 切换屏幕              |
| `self.set_interval(interval, callback)` | 定时器                |
| `self.set_timer(delay, callback)`       | 延时器                |
| `self.register_theme(theme)`            | 注册主题              |
| `self.theme = "name"`                   | 切换主题              |

## Widget 常用方法

| 方法                          | 说明               |
| ----------------------------- | ------------------ |
| `widget.update(content)`      | 更新内容（Static） |
| `widget.remove()`             | 从 DOM 移除        |
| `widget.add_class(name)`      | 添加 CSS 类        |
| `widget.remove_class(name)`   | 移除 CSS 类        |
| `widget.toggle_class(name)`   | 切换 CSS 类        |
| `widget.has_class(name)`      | 检查 CSS 类        |
| `widget.focus()`              | 获取焦点           |
| `widget.scroll_home()`        | 滚动到顶部         |
| `widget.scroll_end()`         | 滚动到底部         |
| `widget.refresh()`            | 刷新渲染           |
| `widget.loading = True`       | 显示加载状态       |
| `widget.display = False`      | 隐藏组件           |
| `widget.tooltip = "..."`      | 设置提示文字       |
| `widget.border_title = "..."` | 设置边框标题       |

## 鼠标和键盘事件

| 事件                   | 说明                       |
| ---------------------- | -------------------------- |
| `on_key(event)`        | 按键，`event.key` 获取键名 |
| `on_click(event)`      | 点击                       |
| `on_mouse_move(event)` | 鼠标移动                   |
| `on_paste(event)`      | 粘贴                       |

## 常用键名

```
字母: a-z
数字: 0-9
功能键: f1-f12
特殊键: enter, escape, space, tab, backspace, delete
方向键: up, down, left, right
组合键: ctrl+a 到 ctrl+z, shift+tab
```

## Textual CLI 命令

```bash
textual run app.py              # 运行应用
textual run app.py --dev        # 开发模式（CSS 热更新）
textual console                # 打开控制台
textual colors                 # 预览颜色主题
textual borders                # 预览边框样式
textual keys                   # 预览键名列表
textual css app.py             # CSS 调试模式
```

---

> 📚 **更多资源**：
>
> - 官方文档：https://textual.textualize.io/
> - GitHub 仓库：https://github.com/Textualize/textual
> - 官方示例：https://github.com/Textualize/textual/tree/main/examples
> - Discord 社区：https://discord.gg/Enf6Z3qhVr
> - PyPI：https://pypi.org/project/textual/
