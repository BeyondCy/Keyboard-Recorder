# -*- coding: utf-8 -*- #
import re
import chardet
from multiprocessing import Pool

f = open("d:\\install.txt","r")
lines = f.readlines() #读取全部内容

def WindowsName():
    rawlist = []
    for line in lines:
        if line[0:11] == 'WindowName:':
            #print chardet.detect(line)['encoding']
            #print type(line)
            #print chardet.detect(stri)['encoding']
            rawlist.append(line)
    return rawlist

def Time():
    rawlist = []
    for line in lines:
        r1 = r'\bTime:\b.*'
        r2 = re.findall(r1,line)
        if r2 != []:
            strr = str(r2[0])
            rawlist.append(strr)
    return rawlist

if __name__=='__main__':
    p = Pool(processes=8)
    WindowsName = WindowsName()
    Time = Time()
    if len(WindowsName) == len(Time):
        print 'Numberic correct:'+str(len(WindowsName))
        #print(WindowsName)
        #print(Time)
        x = 0
        diction = []
        while x < len(WindowsName):
            i = WindowsName[x]
            diction.append(i)
            o = Time[x]
            diction.append(o)
            x = x + 1

        if len(diction) == len(WindowsName)*2:
            print 'Numberic correct:'+str(len(diction))
            print diction
        else:
            print 'Numberic WRONG'
            print len(diction)
            print diction

    else:
        print 'Numberic WRONG'
        print(len(WindowsName))
        print(len(Time))
        print(WindowsName)
        print(Time)
    print 'Program Finished'
    p.close()
    p.join()



