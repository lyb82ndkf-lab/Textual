from textual.app import App, ComposeResult
from textual.widgets import Tree

class TreeApp(App):

    def compose(self):
        
        tree = Tree("根节点")
        
        # 全部改用 .add() 方法
        tree.root.add("子叶节点1")
        tree.root.add("子叶节点4")
        
        # 拿到分支节点，它同样是用 add 创建的
        branch = tree.root.add("分支1")
        
        # 在分支下面继续 add 子节点
        branch.add("子叶节点2")
        branch.add("子叶节点3")
        yield tree

if __name__ == "__main__":
    TreeApp().run()
   