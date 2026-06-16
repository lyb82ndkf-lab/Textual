from textual.app import App, ComposeResult
from textual.messages import Message
from textual.widget import Widget

class ChatMessage(Widget):
    
    # 1. 声明自定义消息（仅作为数据的载体，不要在里面写业务逻辑）
    class Sent(Message):
        def __init__(self, content: str) -> None:
            self.content = content
            # 只要你继承了别人的类，并且自己写了 __init__ 构造函数
            # 那就闭着眼睛把 super().__init__() 写上去
            super().__init__()

    # 为了让组件有内容可点，我们给它一个初始文字
    def __init__(self, text: str) -> None:
        self.text = text
        super().__init__()

    def render(self) -> str:
        # 渲染到终端屏幕上
        return f"聊天框: {self.text} (用鼠标点击我试试)"

    # 2. 修正：组件被点击的事件，必须属于 Widget！
    def on_click(self) -> None:
        # 此时 self 是 ChatMessage 组件对象，它完美拥有 post_message 方法
        # 我们在这里把自定义的 Sent 消息大声地广播出去！
        self.post_message(self.Sent(f"【{self.text}】成功触发了自定义消息！"))


class ChatApp(App):
    CSS = """
    ChatMessage {
        border: solid pink;
        background: #222;
        margin: 2;
        height: 3;
        # width: auto;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield ChatMessage("这是一条可以点击的聊天消息")

    # 3. 接收端：App 通过暗号规则自动监听
    # 名字铁律：on_ + 组件名小写(chat_message) + _ + 消息名小写(sent)
    def on_chat_message_sent(self, message: ChatMessage.Sent) -> None:
        # 拆开信封，拿出里面我们自定义的 content 数据，弹出全局通知
        self.notify(message.content)


if __name__ == "__main__":
    ChatApp().run()