import json, re

def load_json(source):
    '''
    Загрузить файл JSON в виде списка или словаря
    '''
    with open(source, 'r', encoding='utf-8') as handler:
        return json.load(handler)

distinct_territory = dict()
etr = list()
data = load_json('media_dump.json')
for d in data:
    #print(d)
    #print(d['territory'])
    if 'langs'not in d:
        if ('territory' in d) and ('зарубежные страны' in d['territory']):
            print (d['name'],d['territory']) #Health & Beauty Краснодар
        continue
    #for s in re.split(r',', d['territory']):
    #    if 'зарубежные страны' in s:
    #        distinct_territory[s] = distinct_territory.get(s,0) + 1
    #    if 'зарубежные страны' in s and 'Российская Федерация)' in s:
    #        print(d)
    for l in re.split(r',', d['langs']):
        if len(l)>1:
            etr.append(d)
print(len(etr))

