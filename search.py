import re

def searchByOneName(name, relationType):
    f = open('./data/sanguo_edge.txt', encoding='utf-8')
    for line in f.readlines():
        temp = []
        temp = re.split(r' ', line)
        if name == temp[0] and relationType in line:
            print(line)

    print("finsih!!")

def searchByTwoName(name1, name2):
    f = open('./data/sanguo_edge.txt', encoding='utf-8')
    for line in f.readlines():
        temp = []
        temp = re.split(r' ', line)
        if name1 == temp[0] and name2 == temp[1]:
            print(line)

    print("finsih!!")


def searchByrelationType(relationType):
    f = open('./data/sanguo_edge.txt', encoding='utf-8')
    for line in f.readlines():
        temp = []
        temp = re.split(r' ', line)
        if relationType in line:
            print(line)

    print("finsih!!")
    
searchByrelationType('密切相关')
##searchByOneName('刘备', '密切相关')
## searchByTwoName('刘备', '张飞')
