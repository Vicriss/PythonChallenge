import re, zipfile

zippath = 'channel.zip'
z = zipfile.ZipFile(zippath, mode="r")
nothing = '90052'
comments = []
while (True):
    text = z.read(nothing + '.txt')
    text = text.decode('utf-8')
    nothing = re.findall('(\d+)', text)
    # f = nothing + ".txt"
    try:
        nothing = nothing[0]
        comments.append(z.getinfo(nothing + '.txt').comment.decode('utf-8'))
    except Exception as e:
        break
#    print(nothing)

print(''.join(comments))
    # count += 1
    # break
