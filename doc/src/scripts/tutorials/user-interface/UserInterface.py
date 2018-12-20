import time
import krpc

conn = krpc.connect(name='用户界面演示')
canvas = conn.ui.stock_canvas

# 获取游戏窗口的像素尺寸
screen_size = canvas.rect_transform.size

# 添加一个面板用来容纳UI元素
panel = canvas.add_panel()

# 将面板定位在屏幕左侧
rect = panel.rect_transform
rect.size = (200, 100)
rect.position = (110-(screen_size[0]/2), 0)

# 添加按钮把节流阀设置为最大
button = panel.add_button("反向节流阀")
button.rect_transform.position = (0, 20)

# 添加一些显示总发动机推力的文本
text = panel.add_text("推力: 0 kN")
text.rect_transform.position = (0, -20)
text.color = (1, 1, 1)
text.size = 18

# 设置流以监视节流阀按钮
button_clicked = conn.add_stream(getattr, button, 'clicked')

vessel = conn.space_center.active_vessel
while True:
    # 处理被点击的节流阀按钮
    if button_clicked():
        if (vessel.control.throttle == 0) :
            vessel.control.throttle = 1
        else:
            vessel.control.throttle = 0
        button.clicked = False

    # 更新推力文本
    text.content = '推力: %.1f kN' % (vessel.thrust/1000)

    time.sleep(0.1)
