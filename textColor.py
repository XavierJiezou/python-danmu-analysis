with open('danmus.csv', encoding='utf-8') as f:
    danmus = []
    for line in f.readlines()[1:]:
        time = int(float(line.split(',')[0]))
        color = line.split(',')[3]
        text = line.split(',')[-1].replace('\n', '')
        danmus.append([time, color, text])

danmus.sort(key=lambda x: x[0])
dict1 = {}
dict2 = {}
for item in danmus:
    if item[1] == '16776960':
        minute = int(item[0]/60)
        second = item[0] % 60
        dict1[minute] = dict1.get(minute, 0)+1
        if dict2.get(minute) == None:
            dict2[minute] = f'{minute:0>2}m{second:0>2}s {item[2]}'
        else:
            pass
for key, value in dict1.items():
    if value >= 3:
        print(dict2[key])
