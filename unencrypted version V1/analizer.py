# -*- coding: utf-8 -*- #

__author__ = 'cyankw'
import xlwt
# import chardet
from multiprocessing import Pool

txtfile = open("d:\\install.txt", "r")
lines = txtfile.readlines()  #<type 'list'>

#打开表格
xlsfile = xlwt.Workbook()
table = xlsfile.add_sheet('sheet', cell_overwrite_ok = True)
first_col = table.col(0)
second_col = table.col(1)
first_col.width = 256 * 115
second_col.width = 256 * 25

#若第一行不是"---------\n"，则进行删除，防止逻辑出错
L0 = lines[0]
if L0 == "---------\n":
	pass
else:
	while lines[0] != "---------\n":
		del(lines[0])

#WindowsName函数
def WindowsName():
    rawlist = []
    for line in lines:
        if line[0:11] == 'WindowName:':
            line = unicode(line, errors='ignore')
            rawlist.append(line)
    return rawlist

#Time函数
def Time():
    rawlist = []
    for line in lines:
        if line[0:5] == 'Time:':
            rawlist.append(line[5:])
    return rawlist

#Key函数
def Key():
    rawlist = []
    i=0
    while i <= len(lines):
        rawlist2 = []
        if lines[i] == '---------\n':
            if i+3 < len(lines):
                i=i+3
            else:
                break
            while lines[i][0:9] == '     Key:':
                temp = ' '+lines[i][9:17]

                temp = temp.replace('Lcontrol', 'Ctrl')
                temp = temp.replace('Lmenu', 'Alt')
                temp = temp.replace('Lshift', 'Shift')
                temp = temp.replace('Lwin', 'Win')
                temp = temp.replace('Return', 'Enter')
                temp = temp.replace('Rcontrol', 'Ctrl')
                temp = temp.replace('Rshift', 'Shift')
                temp = temp.replace('Rmenu', 'Alt')
                temp = temp.replace('Escape', 'Esc')
                
                rawlist2.append(temp)
                if i<len(lines)-1:
                    i=i+1
                else:
                    break
            rawlist.append(rawlist2)
        else:
            break
    return rawlist

if __name__ == '__main__':
    p = Pool(processes=8)
    WindowsName = WindowsName()
    Time = Time()
    Key =Key()
    if len(WindowsName) == len(Time):
        print 'Numberic =:'+str(len(WindowsName))
        #print(WindowsName)
        #print(Time)

        i=1
        while i<=len(WindowsName):
            table.write(i, 0, WindowsName[i-1])
            i=i+1

        u=1
        while u<=len(Time):
            table.write(u, 1, Time[u-1])
            u=u+1

        v=1
        while v<=len(Key):
            if len(Key[v-1]) >= 1500:
                Key[v-1] = Key[v-1][0:1500]
            table.write(v, 2, Key[v - 1])
            v=v+1
        xlsfile.save('test.xls')

    else:
        print 'Numberic WRONG'
        print(len(WindowsName))
        print(len(Time))
        print(WindowsName)
        print(Time)
    print 'Program Finished'
    p.close()
    p.join()



