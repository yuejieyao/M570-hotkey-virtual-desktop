#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description: 绑定M570的两个编程键给ctrl+win+right/left
@Date     :2021/06/29 15:47:13
@Author      :yuejieyao
@version      :1.0
'''


from pynput import mouse


if __name__ == "__main__":

    # 监听鼠标并执行相应的键盘热键
    from pynput.mouse import Listener, Button
    from pynput.keyboard import Key, Controller

    def ctrl_win_x(x):
        # 执行ctrl+win组合键
        keyboard = Controller()
        with keyboard.pressed(Key.cmd):
            with keyboard.pressed(Key.ctrl):
                keyboard.press(x)
                keyboard.release(x)

    def on_click(x, y, button, pressed):
        # 监听
        print(button)
        if pressed:
            if button == Button.x2:
              # 位置靠上,驱动默认是前进的按钮,这里绑定了上一个桌面
                ctrl_win_x(Key.left)
            if button == Button.x1:
              # 后退按钮,这里绑定了下一个桌面
                ctrl_win_x(Key.right)

    listener = Listener(on_click=on_click)
    listener.start()

  # 生成系统托盘方便关闭
    import webbrowser
    from SysTrayIcon import SysTrayIcon

    def about(sysTrayIcon): webbrowser.open(
        'https://github.com/yuejieyao/M570-hotkey-virtual-desktop')
    menu_options = (('about', None, about),)
    hover_text = 'M750-HOTKEY-VIRTUAL-DESKTOP'
    SysTrayIcon(icon='233.ico', hover_text=hover_text,
                menu_options=menu_options, default_menu_index=1)
