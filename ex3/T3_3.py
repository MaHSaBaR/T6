import re

text = input()
text = text.rstrip()
l = list(enumerate(text))
l1 = []
l2 = []
for i in range(len(l)):
    if l[i][1] == '#':
        l1.append(l[i][0])
    if l[i][1] == '@':
        l2.append(l[i][0])
for x in l2:
    for y in range(x):
        if y in l1:
            l1.remove(y)
    if l1 != []:
        z = min(l1)
        l1.remove((z))
        l.remove((z, '#'))
text = []
for x in l:
    text.append(x[1])
text = ''.join(text)


text = re.sub(r'\s{2,}',' ',text)
text = text.replace(r'\n','\n')

print('Formatted Text: '+ text)