# ============================================
# Textual 常用样式属性速查
# ============================================

# 一、布局属性
# --------------------------------------------
# display: 控制组件是否显示
#   block  - 显示组件（默认）
#   none   - 隐藏组件（不占用空间）
# 
# visibility: 控制组件可见性
#   visible - 可见（默认）
#   hidden  - 隐藏但仍占用空间
# 
# layout: 设置容器的布局方向
#   vertical   - 垂直排列子组件
#   horizontal - 水平排列子组件
#   grid       - 网格布局
# 
# dock: 将组件固定到父容器边缘
#   top    - 固定到顶部
#   right  - 固定到右侧
#   bottom - 固定到底部
#   left   - 固定到左侧

# 二、对齐属性
# --------------------------------------------
# content-align: 子组件在容器中的对齐方式
#   格式: 水平对齐 垂直对齐
#   示例: content-align: center middle;
#   水平值: left | center | right
#   垂直值: top | middle | bottom
# 
# text-align: 文本水平对齐
#   left   - 左对齐（默认）
#   center - 居中对齐
#   right  - 右对齐
# 
# align: 组件自身在可用空间中的对齐方式
#   格式: 水平对齐 垂直对齐
#   示例: align: right bottom;

# 三、文本属性
# --------------------------------------------
# color: 文本颜色
#   支持: 命名颜色、十六进制、RGB、HSL
#   示例: color: white;
#         color: #ff0000;
#         color: rgb(255, 0, 0);
# 
# text-style: 文本样式（可组合使用）
#   bold      - 粗体
#   italic    - 斜体
#   underline - 下划线
#   strike    - 删除线
#   reverse   - 反色显示
#   示例: text-style: bold italic;
# 
# text-wrap: 文本换行方式
#   wrap    - 自动换行（默认）
#   nowrap  - 不换行
# 
# text-overflow: 溢出文本处理
#   ellipsis - 显示省略号
#   fold     - 折叠显示

# 四、背景属性
# --------------------------------------------
# background: 背景颜色
#   示例: background: darkblue;
# 
# background-tint: 在背景上叠加颜色滤镜
#   格式: background-tint: 颜色 透明度%;
#   示例: background-tint: blue 50%;
# 
# tint: 为整个组件添加颜色滤镜
#   格式: tint: 颜色 透明度%;
#   示例: tint: red 30%;

# 五、滚动属性
# --------------------------------------------
# overflow: 内容溢出时的处理方式
#   auto   - 自动显示滚动条（需要时）
#   hidden - 隐藏溢出内容
#   scroll - 始终显示滚动条
# 
# overflow-x: 水平方向溢出处理
# overflow-y: 垂直方向溢出处理

# 六、动画属性
# --------------------------------------------
# animation: 应用预设动画效果
#   格式: animation: 动画名 时长 缓动函数;
#   示例: animation: fade-in 0.3s in_out;
#   常用动画: fade-in, slide-in-left, slide-in-right
#   缓动函数: linear, in_out, bounce

# 七、透明度属性
# --------------------------------------------
# opacity: 组件透明度
#   值范围: 0.0 ~ 1.0
#   0.0 = 完全透明
#   1.0 = 完全不透明（默认）
#   示例: opacity: 0.8;

# ============================================
# 使用示例
# ============================================
# Widget {
#     /* 布局 */
#     display: block;
#     layout: vertical;
#     dock: top;
#     
#     /* 对齐 */
#     content-align: center middle;
#     text-align: center;
#     
#     /* 文本 */
#     color: white;
#     text-style: bold italic;
#     text-wrap: wrap;
#     
#     /* 背景 */
#     background: darkblue;
#     opacity: 0.8;
#     
#     /* 滚动 */
#     overflow: auto;
#     
#     /* 动画 */
#     animation: fade-in 0.3s in_out;
# }