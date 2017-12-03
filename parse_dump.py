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
# {'name': 'Медицинский совет в детской поликлинике', 'langs': 'русский', 'staff_address': '105082, г. Москва, ул. Бакунинская, д. 71, стр. 10', 'territory': 'зарубежные страны (Российская Федерация)', 'founders': [{'name': 'Общество с ограниченной ответственностью "РеФарм Медиа"', 'id': '1012663', 'inn': '7707767029'}], 'reg_date': '2012-08-27 00:00:00', 'reg_number_id': 323560, 'status_id': 1, 'id': 403867, 'reg_number': 'ПИ № ФС 77 - 50963', 'form_spread_id': 22, 'territory_ids': '1000', 'form_spread': 'печатное СМИ журнал'}
for d in data:
    #print(d)
    #print(d['territory'])
    if 'langs'not in d:
        if ('territory' in d) and ('зарубежные страны' in d['territory']):
            if 'reg_date' not in d: d['reg_date'] = '1970-01-01'
            if 'form_spread' not in d: d['form_spread'] = 'unknown:'
            print ('[%s]\t%s\t(%s) -> %s' % (d['form_spread'], d['name'], d['reg_date'], d['territory'])) #Health & Beauty Краснодар
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

