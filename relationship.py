import jieba
names = {}
relationships = {}
linenames = []
all_names = []

f1 = open('./data/name.txt',encoding='utf-8')
for line in f1.readlines():
    all_names.append(line.strip().strip('\ufeff'))
for name in all_names:
    jieba.add_word(name)

f2 = open('./data/sanguo-utf8.txt',encoding='utf-8')
for line in f2.readlines():
    seg_list = jieba.cut(line)
    linenames.append([])
    for i in seg_list:
        if i in all_names:
            linenames[-1].append(i)
            if names.get(i) is None:
                names[i] = 0
                relationships[i] = {}
            names[i] +=1

for line in linenames:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2]=1
            else:
                relationships[name1][name2] += 1

import codecs
with codecs.open('./data/sanguo_node.txt','w','utf-8') as f:
    f.write("Id Label Weight\r\n")
    for name, times in names.items():
        f.write(name + ' ' + name + ' ' + str(times) + '\r\n')
        
with codecs.open('./data/sanguo_edge.txt', 'w', "utf-8") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w < 50:
                f.write(name + ' ' + v + " " + str(w) + " 较少相关"+ "\r\n")
            elif w < 100:
                f.write(name + ' ' + v + " " + str(w) + " 一般相关"+ "\r\n")
            elif w < 250:
                f.write(name + ' ' + v + " " + str(w) + " 相关"+ "\r\n")
            elif w < 350:
                f.write(name + ' ' + v + " " + str(w) + " 很相关"+ "\r\n")
            else:
                f.write(name + ' ' + v + " " + str(w) + " 密切相关"+ "\r\n")

