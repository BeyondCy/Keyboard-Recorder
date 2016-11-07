# -*- coding: utf-8 -*- #
import re
import xlwt
#import chardet
from multiprocessing import Pool
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

txtfile = open("d:\\install.txt","r")
lines = txtfile.readlines() #读取全部内容

xlsfile = xlwt.Workbook()
table = xlsfile.add_sheet('Windows+Time',cell_overwrite_ok=True)

def WindowsName():
    rawlist = []
    for line in lines:
        if line[0:11] == 'WindowName:':
            line = unicode(line, errors='ignore')
            rawlist.append(line)
    return rawlist

def Time():
    rawlist = []
    for line in lines:
        r1 = r'\bTime:\b.*'
        r2 = re.findall(r1,line)
        if r2 != []:
            str_r2 = str(r2[0])
            rawlist.append(str_r2)
    return rawlist

if __name__=='__main__':
    p = Pool(processes=8)
    WindowsName = WindowsName()
    Time = Time()
    if len(WindowsName) == len(Time):
        print 'Numberic correct:'+str(len(WindowsName))
        #print(WindowsName)
        #print(Time)
        i=1
        while i<=len(WindowsName):
            table.write(i, 1, WindowsName[i-1])
            i=i+1
        u=1
        while u<=len(Time):
            table.write(u, 2, Time[u-1])
            u=u+1

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



