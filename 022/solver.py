#coding: utf-8

def name_value(name):
    ret = 0
    for c in name:
        ret += ord(c) - ord('A') + 1
    return ret

with open('p022_names.txt') as fin:
    name_list = [item[1:-1] for item in fin.readline().rstrip('\r\n').split(',')]
name_list = sorted(name_list)
total = 0
for i in range(len(name_list)):
    total += name_value(name_list[i]) * (i + 1)
print(total)
