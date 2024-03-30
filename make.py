import os
try:
    import _pyinstaller_hooks_contrib
except ModuleNotFoundError:
    print("环境中未安装pyinstaller,使用pip install pyinstaller安装后执行脚本")
    exit()

os.system("pyinstaller -F -w -i icon/icon256x.ico main.py")
os.system(r"copy dist\main.exe n2n-gui.exe")

f = open("start.bat","w")
f.write('@echo off\n'
        '%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit\n'
        'cd /d "%~dp0"\n'
        '\n'
        'start n2n-gui.exe')
f.close()
