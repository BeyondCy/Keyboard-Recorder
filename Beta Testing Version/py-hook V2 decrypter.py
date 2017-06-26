# -*- coding: utf-8 -*- #

__author__ = 'cyankw'
import urllib, base64
from multiprocessing import Pool

if __name__ == "__main__":
    rtfile = open(r'd://install22.txt', 'r')
    p = Pool(processes=8)
    lines = rtfile.readlines()

    Lst=[]
    lst2=[]

    for x in lines:
        x = x.replace("%7qw(","CU")
        x = x.replace("%128)","=\\n")
        x = x.replace("%$6rd)",",")
        m = x.split('\\n')
        for mm in m:
            b = base64.decodestring(mm)
            a = urllib.unquote(b)
            lst2.append(a)

    wrfile2 = open('d://rmm.txt', 'a')

    for n in lst2:
        wrfile2.write(n)

    p.close()
    p.join()
