f = open("news.txt", 'r')

d = []

for line in f.readlines():
    data = []
    p = line.split('[')
    data.append(p[0])
    data.append(p[1].split(']')[0])
    print(data)
    d.append(data)

f1 = open("news_informat.txt", 'w')
for item in d:
    f1.write('- date: ' + item[1] + '\n')
    f1.write('  headline: ' + item[0] + '\n')
f1.close()
    
    
f.close()