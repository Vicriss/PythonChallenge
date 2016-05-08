__author__ = 'vicriss'
__date__ = '2016/02/12'

# import re
#
stopword = ''
str = ''
for line in iter(raw_input, stopword):
  str += line + '\n'
# result = re.findall(r'.*?([a-z]).*?', str)
# print ''.join(result)


########################################################
#Very Easy Method
string = str
count_list = []
char_list = []
def count_char(char):
    return string.count(char)

for char in string:
    if char not in char_list:
        char_list.append(char)
        count_list.append(count_char(char))


print char_list
print count_list