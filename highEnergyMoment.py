import re


with open('danmus.csv', encoding='utf-8') as f:
    danmus = []
    for line in f.readlines()[1:]:
        time = int(float(line.split(',')[0]))
        text = line.split(',')[-1].replace('\n', '')
        danmus.append([time, text])


danmus.sort(key=lambda x: x[0])
dict1 = {}
dict2 = {}
control = True
for item in danmus:
    if re.search('名场面(:|：)', item[1]):
        print(f'{int(item[0]/60)}m{item[0]%60}s {item[1]}')
        control = False
        break
    if '名场面' in item[1]:
        minute = int(item[0]/60)
        second = item[0] % 60
        dict1[minute] = dict1.get(minute, 0)+1
        dict2[minute] = dict2.get(minute, 0)+second
    else:
        pass
if control:
    minute= max(dict1, key=dict1.get)
    second = round(dict2[minute]/dict1[minute])
    print(f'{minute}m{second}s 名场面')
