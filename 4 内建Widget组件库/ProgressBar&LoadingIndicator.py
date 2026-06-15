from textual.app import App,ComposeResult
from textual.widgets import ProgressBar, LoadingIndicator, Button, Static
from textual import on
# asyncio 导入异步模块
import asyncio

class myApp(App):

    def compose(self) -> ComposeResult:
        
        # 进度条
        # total: 总进度
        # show_eta: 是否显示ETA(预计完成时间)
        yield ProgressBar(total=100, show_eta=True) 

        # 加载指示器(自动旋转动画)
        # yield LoadingIndicator()
        
        yield Button("点击我", id="load-button")
        yield Static("这是原本内容", id="static-content")

        # 点击按钮事件
    @on(Button.Pressed,"#load-button")
    async def handle_load(self) -> None:
        # 抓取要控制的组件
        #query_one: 查询第一个符合条件的组件
        content = self.query_one("#static-content", Static)

        # 开启加载状态
        content.loading = True
        self.notify("加载中...")

        # 模拟网络延迟
        await asyncio.sleep(0.05)
        await asyncio.sleep(3)

        # 更新组件里的文本
        content.update("加载完成")

        # 关闭加载状态
        content.loading = False
        self.notify("加载完成")


    def on_callback(self) -> None:
        
        # 这时候组件已经上屏了，可以百分百精准抓取
        progress = self.query_one(ProgressBar)
        # Textual 中更新进度条进度的参数叫 advance 或 progress
        # advance: 增加进度
        # progress: 更新进度
        progress.progress = 50
        # progress.advance(50)
    
if __name__ == "__main__":
    myApp().run()

