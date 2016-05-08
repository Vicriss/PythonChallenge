__author__ = 'vicriss'
__date__ = '2016/02/12'

import re, urllib2

f = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
result = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', f.read())   # ^[A-Z] 匹配以大写字母开头的文本串 [^A-Z] 表示与不包含大写字母的字符匹配
print ''.join(result)