import pystray
from PIL import Image


class trayicon:

    def create_tray_icon(self):
        # 从图片文件中加载图标
        image = Image.open("icon/tray_icon_disconnect.png")
        print(image.size)

        # 创建系统托盘菜单
        menu = (
            pystray.MenuItem("打开应用", action=self.open_app, default=True),
            pystray.MenuItem("退出", action= self.exit_app)
        )



        # 创建系统托盘图标
        self.tray_icon = pystray.Icon("app_name", image, "N2N-GUI", menu)

        # 设置图标的提示文本
        self.tray_icon.tooltip = "N2N-GUI"

        # 显示系统托盘图标
        self.tray_icon.run()

    # 点击“打开应用”菜单项的事件处理函数
    def open_app(self):
        # TODO: 打开应用的具体逻辑
        print("open")
        pass

    # 点击“退出”菜单项的事件处理函数
    def exit_app(self):
        # TODO: 退出应用的具体逻辑
        print("exit")
        self.tray_icon.stop()
        pass