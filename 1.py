__author__ = 'vicriss'

old = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr
amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
lmu ynnjw ml rfc spj."""


def enascll(ch):
    oldascll = map(ord, ch)
    n = 0
    for i in oldascll:
        if(i>=97 and i<=122):
            if( i + 2 > 122):
                oldascll[n] = i - 24
            else:
                oldascll[n] = i + 2
        else:
            oldascll[n] = i
        n += 1
    return oldascll


def deascll(num):
    return ''.join(map(chr, num))


ch = enascll(old)
print deascll(ch)

############################################################
# solution
import string
text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr
amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
lmu ynnjw ml rfc spj."""
table = string.maketrans(
    string.ascii_lowercase,
    string.ascii_lowercase[2:]+string.ascii_lowercase[:2])

print string.translate(text,table)