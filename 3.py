__author__ = 'vicriss'
__date__ = '2016/02/12'

import re, urllib2

f = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
result = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', f.read())   # ^[A-Z] ƥ���Դ�д��ĸ��ͷ���ı��� [^A-Z] ��ʾ�벻������д��ĸ���ַ�ƥ��
print ''.join(result)