#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 18:08:13 2018

@author: Vyri
"""

#poem = "hello word!"
#
#for i in range(1,10):
#    poem = "hello word " + str(i)
#    print poem

#with open("poem.md","w") as f:
#    f.write(poem)
    
#    
#with open("poem.md","w") as f:
#    for i in range(1,10):
#        poem = "hello word " + str(i)
#        print poem
#        f.write(poem)
#        f.write("\n")

mylist = []
for i in range(0,7):
    mylist.append( "hello world" + str(i))
#    print mylist
#    print mylist[i]
with open("poem.md","w") as f:
    for item in mylist:
        f.write(item)
        f.write("\n")
        
    
    
    
#print mylist
    