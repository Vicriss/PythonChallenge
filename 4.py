__author__ = 'vicriss'
__date__ = '2016/02/12'

import urllib, re, urllib2, pickle

nothing = 8022
count = 0
while (count < 400):
    param = urllib.urlencode({'nothing':nothing})
    f = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?%s' %param)
    reg = re.compile('(\d+)', re.X)
    match = reg.search(f.read())
    nothing = match.group(1)
    count += 1
    print count, " : ", nothing
