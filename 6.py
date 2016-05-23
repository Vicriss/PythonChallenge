import re, zipfile

zippath = '/home/wybe/Templates/pychallenge/channel.zip'
z = zipfile.ZipFile(zippath, mode="r")
nothing = '90052'
comments = []
while (True):
    text = z.read(nothing + '.txt')
    nothing = re.findall('(\d+)', text)
    # f = nothing + ".txt"
    try:
        nothing = nothing[0]
        comments.append(z.getinfo(nothing + '.txt').comment)
    except Exception as e:
        break
    print nothing

print ''.join(comments)
    # count += 1
    # break
