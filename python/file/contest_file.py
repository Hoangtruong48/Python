f1 = open("Input2.txt", "r")
f2 = open("Output2.txt", "w")
a = []
temp = ''
data = f1.read()
data += ','
for i in range(len(data)):
    if data[i] != ',':
        temp += data[i]
    else:
        a.append(temp)
        temp = ''
for x in a:
    s1 = x.title().split()
    temp = ' '.join(s1)
    f2.write(temp + ', ')
f1.close()
f2.close()