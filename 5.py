#! /usr/bin/python2
# author: vicriss
# date: 2016.5.10

import pickle
import urllib

data = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
obj = pickle.loads(data)

# print obj

for line in obj:
    print ''.join(ch * count for ch, count in line)
