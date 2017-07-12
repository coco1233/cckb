#!/usr/bin/env python
# coding=utf-8
strl = "asasadadsafsfsgdgdfhfhggfhjgjfgkflfkjdfhdgsf"
liststr = []
for eachstr in strl:
    countstr = strl.count(eachstr)
    numstr = eachstr + ":" + str(countstr)
    if numstr not in liststr :
        liststr.append(numstr)
for i in liststr:
    print i

