from textual.app import App,ComposeResult
from textual.widgets import Select
from textual import on

class SelectApp(App):

    def compose(self) -> ComposeResult:

        # 下拉选择
        yield Select(
            # 下拉选择的选项 (label, value)
            # label: 下拉选择的选项文字
            # value: 下拉选择的选项值，用于提交表单
            [(label, value) for label, value in [
                ("gpt-5.5-pro label", "gpt-5.5-pro"),
                ("claude-3-pro label", "claude-3-pro"),
                ("deepseek-v4-flash label", "deepseek-v4-flash")
            ]],
            # 下拉框的提示文字
            prompt="请选择模型",
            id="model-select",
        )

    # 下拉选择变化事件
    # select.Changed: 下拉选择变化事件
    # event.value: 选择的模型值
    @on(Select.Changed,"#model-select")
    def on_model_changed(self, event: Select.Changed) -> None:
        self.notify(f"选择的模型: {event.value}")


if __name__ == "__main__":
    SelectApp().run()