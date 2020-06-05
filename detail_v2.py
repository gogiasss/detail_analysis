import re

# функция суммирования
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return round(theSum, 2)

# Переменные
data = []
world =[]
world2=[]
russia=[]
russia2=[]
world_may=[]
world_april=[]
russia_april=[]
russia_may=[]
inbox=[]
message=[]

price_russia_april=[]
price_russia_may=[]

price_world_april=[]
price_world_may=[]

# Открываем файл и записываем в data
with open ('detail_v2.csv',encoding='utf8', mode='r') as f:
    for line in f:
        s = str(line)
        s = s.replace('\n','')
        s = s.replace('"','')
        s = s.replace(',','.')
        s = s.split(';')
        data.append(s)

# Делим звонки по направлениям

for item in data:
    for i in item:
        if re.search(r'Исходящий международный', i):            
            world.append(item)
        elif re.search(r'Исходящий на', i):
            russia.append(item)
        elif re.search(r'Исх.', i):
            russia.append(item)
        elif re.search(r'Вх.', i):
            inbox.append(item)
        elif re.search(r'Штука', i):
            message.append(item)
        else:
            pass


#ищем все звонки по Миру

for item in world:
    if len(item) >= 2:
        world2.append(float(item[-1]))

# ищем все звонки по РФ

for item in russia:
    if len(item) >= 2:
        russia2.append(float(item[-1]))

# Россия апрель и май
for item in russia:
    for i in item:
        if re.search(r'04.2020', i):
            russia_april.append(item)
        elif re.search(r'05.2020', i):
            russia_may.append(item)
        else:
            pass

# Заграница апрель и май
for item in world:
    for i in item:
        if re.search(r'04.2020', i):
            world_april.append(item)
        elif re.search(r'05.2020', i):
            world_may.append(item)
        else:
            pass
        
# считаем сумму апрель Россия
for item in russia_april:
    if len(item) >= 2:
        price_russia_april.append(float(item[-1]))

# считаем сумму май Россия
for item in russia_may:
    if len(item) >= 2:
        price_russia_may.append(float(item[-1]))

# считаем сумму апрель Мир
for item in world_april:
    if len(item) >= 2:
        price_world_april.append(float(item[-1]))

# считаем сумму май Мир
for item in world_may:
    if len(item) >= 2:
        price_world_may.append(float(item[-1]))

# Делим по странам Апрель

kaz=[]
ukr=[]
bel=[]
kyrg=[]
usa=[]
ger=[]

for item in world:
    for i in item:
        if re.search(r'Казахстан', i):            
            kaz.append(item)
        elif re.search(r'Украина', i):
            ukr.append(item)
        elif re.search(r'Беларусь', i):
            bel.append(item)
        elif re.search(r'Кыргызстан', i):
            kyrg.append(item)
        elif re.search(r'Соединенные Штаты Америки', i):
            usa.append(item)
        elif re.search(r'Германия', i):
            ger.append(item)
        else:
            pass



#Казахстан считаем звонки и сумму
kaz_apr=[]
kaz_may=[]
kaz_time_a=[]
kaz_time_m=[]
kaz_summ_a=[]
kaz_summ_m=[]

for item in kaz:
    for i in item:
        if re.search(r'04.2020', i):
            i.replace(',','.')
            kaz_apr.append(item)
        elif re.search(r'05.2020', i):
            kaz_may.append(item)
            
# Казахстан считаем время апрель
for item in kaz_apr:
    if len(item) >= 8:
        kaz_time_a.append(float(item[5]))
        
# Казахстан считаем сумму апрель
for item in kaz_apr:
    if len(item) >= 8:
        kaz_summ_a.append(float(item[-1]))
        

# Казахстан считаем сумму май

for item in kaz_may:
    if len(item) >= 8:
        kaz_time_m.append(float(item[5]))

for item in kaz_may:
    if len(item) >= 8:
        kaz_summ_m.append(float(item[-1]))        

ka = round(listsum(kaz_time_a) / 60, 1) # вычисляем минуты в апреле
km = round(listsum(kaz_time_m) / 60, 1) # вычисляем минуты в мае
kaz_sa = round(listsum(kaz_summ_a), 2) # вычисляем сумму  в апреле
kaz_sm = round(listsum(kaz_summ_m), 2) # вычисляем сумму в мае

#Украина считаем звонки и сумму
ukr_apr=[]
ukr_may=[]
ukr_time_a=[]
ukr_time_m=[]

for item in ukr:
    for i in item:
        if re.search(r'04.2020', i):
            i.replace(',','.')
            ukr_apr.append(item)
        elif re.search(r'05.2020', i):
            ukr_may.append(item)
# Украина считаем время апрель
for item in ukr_apr:
    if len(item) >= 8:
        ukr_time_a.append(float(item[5]))

# Украина считаем время май

for item in kaz_may:
    if len(item) >= 8:
        ukr_time_m.append(float(item[5]))

ua = round(listsum(ukr_time_a) / 60, 1) # вычисляем минуты в апреле
um = round(listsum(ukr_time_m) / 60, 1) # вычисляем минуты в мае

print('Казахстан всего звонков:', len(kaz), 'из них в апреле - ', len(kaz_apr), 'и в мае -', len(kaz_may))
print('Всего минут в апреле', ka, 'на сумму', kaz_sa,'; в мае ', km, 'на сумму',kaz_sm,'стоимость минуты звонка')
print()
print('Украина всего звонков:', len(ukr), 'из них в апреле: ', len(ukr_apr), 'и в мае -', len(ukr_may))
print('Всего минут в апреле', ua, 'в мае ', um, 'стоимость минуты звонка: ')
print()
print(len(bel))
print(len(kyrg))
print(len(usa))
print(len(ger))

# Делим по странам Май

all = len(russia) + len(world)
        
print('Всего платных действий совершено', all)
print()
print('Совершено звонков по РФ за 2 месяца',len(russia))
print()
print('Совершено звонков по миру за 2 месяца',len(world))
print()
        
print('Исходящих звонков в апреле по миру',len(world_april))
print('На сумму: ', listsum(price_world_april))
print()
print('Исходящих звонков в мае по миру', len(world_may))
print('На сумму: ', listsum(price_world_may))
print()
print('Исходящих звонков в апреле по РФ', len(russia_april))
print('На сумму: ', listsum(price_russia_april))
print()
print('Исходящих звонков в мае по РФ', len(russia_may))
print('На сумму: ', listsum(price_russia_may))
print()




print('Потрачено на местные переговоры всего за 2 месяца',listsum(russia2))
print()
print('Потрачено на междугородние переговоры всего за 2 месяца',listsum(world2))
        
