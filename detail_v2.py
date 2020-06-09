import re
from collections import Counter


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
sep = '*'

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
            i.replace(',','.')
            kaz_may.append(item)
            
# Казахстан считаем время апрель
for item in kaz_apr:
    if len(item) == 8:
        kaz_time_a.append(float(item[5]))
        
# Казахстан считаем сумму апрель
for item in kaz_apr:
    if len(item) == 8:
        kaz_summ_a.append(float(item[-1]))
        

# Казахстан считаем время и сумму май

for item in kaz_may:
    if len(item) >= 8:
        kaz_time_m.append(float(item[5]))

for item in kaz_may:
    if len(item) >= 8:
        kaz_summ_m.append(float(item[-1]))        

ka = round(listsum(kaz_time_a)/60, 1) # вычисляем минуты в апреле
km = round(listsum(kaz_time_m)/60, 1) # вычисляем минуты в мае
kaz_sa = round(listsum(kaz_summ_a), 2) # вычисляем сумму  в апреле
kaz_sm = round(listsum(kaz_summ_m), 2) # вычисляем сумму в мае

#Украина
ukr_apr=[]
ukr_may=[]
ukr_time_a=[]
ukr_time_m=[]
ukr_summ_a=[]
ukr_summ_m=[]

for item in ukr:
    for i in item:
        if re.search(r'04.2020', i):
            i.replace(',','.')
            ukr_apr.append(item)
        elif re.search(r'05.2020', i):
            i.replace(',','.')
            ukr_may.append(item)
# Украина считаем время апрель
for item in ukr_apr:
    if len(item) >= 8:
        ukr_time_a.append(float(item[5]))

# Украина считаем время май

for item in ukr_may:
    if len(item) >= 8:
        ukr_time_m.append(float(item[5]))


# Украина считаем сумму май и апрель

for item in ukr_apr:
    if len(item) >= 8:
        ukr_summ_a.append(float(item[-1]))

for item in ukr_may:
    if len(item) >= 8:
        ukr_summ_m.append(float(item[-1]))       

ua = round(listsum(ukr_time_a)/60, 1) # вычисляем минуты в апреле
um = round(listsum(ukr_time_m)/60, 1) # вычисляем минуты в мае
ukr_sa = round(listsum(ukr_summ_a), 2) # вычисляем сумму  в апреле
ukr_sm = round(listsum(ukr_summ_m), 2) # вычисляем сумму в мае

#Беларусь
bel_apr=[]
bel_may=[]
bel_time_a=[]
bel_time_m=[]
bel_summ_a=[]
bel_summ_m=[]

for item in bel:
    for i in item:
        if re.search(r'04.2020', i):
            i.replace(',','.')
            bel_apr.append(item)
        elif re.search(r'05.2020', i):
            i.replace(',','.')
            bel_may.append(item)
# Беларусь считаем время апрель
for item in bel_apr:
    if len(item) >= 8:
        bel_time_a.append(float(item[5]))

# Беларусь считаем время май

for item in bel_may:
    if len(item) >= 8:
        bel_time_m.append(float(item[5]))


# Беларусь считаем сумму май и апрель

for item in bel_apr:
    if len(item) >= 8:
        bel_summ_a.append(float(item[-1]))

for item in bel_may:
    if len(item) >= 8:
        bel_summ_m.append(float(item[-1]))       

ba = round(listsum(bel_time_a)/60, 1) # вычисляем минуты в апреле
bm = round(listsum(bel_time_m)/60, 1) # вычисляем минуты в мае
bel_sa = round(listsum(bel_summ_a), 2) # вычисляем сумму  в апреле
bel_sm = round(listsum(bel_summ_m), 2) # вычисляем сумму в мае


#Кыргызтан
kg_apr=[]
kg_may=[]
kg_time_a=[]
kg_time_m=[]
kg_summ_a=[]
kg_summ_m=[]

for item in kyrg:
    for i in item:
        if re.search(r'04.2020', i):
            i.replace(',','.')
            kg_apr.append(item)
        elif re.search(r'05.2020', i):
            i.replace(',','.')
            kg_may.append(item)
# Кыргызтан считаем время апрель
for item in kg_apr:
    if len(item) >= 8:
        kg_time_a.append(float(item[5]))

# Кыргызтан считаем время май

for item in kg_may:
    if len(item) >= 8:
        kg_time_m.append(float(item[5]))


# Кыргызтан считаем сумму май и апрель

for item in kg_apr:
    if len(item) >= 8:
        kg_summ_a.append(float(item[-1]))

for item in kg_may:
    if len(item) >= 8:
        kg_summ_m.append(float(item[-1]))       

kga = round(listsum(kg_time_a)/60, 1) # вычисляем минуты в апреле
kgm = round(listsum(kg_time_m)/60, 1) # вычисляем минуты в мае
kg_sa = round(listsum(kg_summ_a), 2) # вычисляем сумму  в апреле
kg_sm = round(listsum(kg_summ_m), 2) # вычисляем сумму в мае


# Соединенные Штаты Америки
usa_apr=[]
usa_may=[]
usa_time_a=[]
usa_time_m=[]
usa_summ_a=[]
usa_summ_m=[]

for item in usa:
    for i in item:
        if re.search(r'04.2020', i):
            i.replace(',','.')
            usa_apr.append(item)
        elif re.search(r'05.2020', i):
            i.replace(',','.')
            usa_may.append(item)
# Соединенные Штаты Америки считаем время апрель
for item in usa_apr:
    if len(item) >= 8:
        usa_time_a.append(float(item[5]))

# Соединенные Штаты Америки считаем время май

for item in usa_may:
    if len(item) >= 8:
        usa_time_m.append(float(item[5]))


# Соединенные Штаты Америки считаем сумму май и апрель

for item in usa_apr:
    if len(item) >= 8:
        usa_summ_a.append(float(item[-1]))

for item in usa_may:
    if len(item) >= 8:
        usa_summ_m.append(float(item[-1]))       

usa_a = round(listsum(usa_time_a)/60, 1) # вычисляем минуты в апреле
usa_m = round(listsum(usa_time_m)/60, 1) # вычисляем минуты в мае
usa_sa = round(listsum(usa_summ_a), 2) # вычисляем сумму  в апреле
usa_sm = round(listsum(usa_summ_m), 2) # вычисляем сумму в мае

# Германия
ger_apr=[]
ger_may=[]
ger_time_a=[]
ger_time_m=[]
ger_summ_a=[]
ger_summ_m=[]

for item in ger:
    for i in item:
        if re.search(r'04.2020', i):
            i.replace(',','.')
            ger_apr.append(item)
        elif re.search(r'05.2020', i):
            i.replace(',','.')
            ger_may.append(item)
# Германия считаем время апрель
for item in ger_apr:
    if len(item) >= 8:
        ger_time_a.append(float(item[5]))

# Германия считаем время май

for item in ger_may:
    if len(item) >= 8:
        ger_time_m.append(float(item[5]))


# Германия считаем сумму май и апрель

for item in ger_apr:
    if len(item) >= 8:
        ger_summ_a.append(float(item[-1]))

for item in ger_may:
    if len(item) >= 8:
        ger_summ_m.append(float(item[-1]))       

ger_a = round(listsum(ger_time_a)/60, 1) # вычисляем минуты в апреле
ger_m = round(listsum(ger_time_m)/60, 1) # вычисляем минуты в мае
ger_sa = round(listsum(ger_summ_a), 2) # вычисляем сумму  в апреле
ger_sm = round(listsum(ger_summ_m), 2) # вычисляем сумму в мае




print('75 % расходов в мае пришлось на эти страны: Казахстан, Украина, Беларусь')
print()
print('Казахстан звонков в апреле - ', len(kaz_apr), 'и в мае -', len(kaz_may))
print('Всего минут в апреле', ka, 'на сумму', kaz_sa,'; в мае ', km, 'на сумму',kaz_sm,'стоимость минуты звонка ~ 23.6 ')
print()
print('Украина звонков в апреле:', len(ukr_apr), 'и в мае -', len(ukr_may))
print('Всего минут в апреле', ua, 'на сумму', ukr_sa,' в мае ', um, 'на сумму', ukr_sm, 'стоимость минуты звонка: ~ 23.6')
print()
print('Беларусь звонков в апреле:', len(bel_apr), 'и в мае -', len(bel_may))
print('Всего минут в апреле', ba, 'на сумму', bel_sa,' в мае ', bm, 'на сумму', bel_sm, 'стоимость минуты звонка: ~ 30.2')
print()
print('Кыргызтан звонков в апреле:', len(kg_apr), 'и в мае -', len(kg_may))
print('Всего минут в апреле', kga, 'на сумму', kg_sa,' в мае ', kgm, 'на сумму', kg_sm, 'стоимость минуты звонка: ~ 22.2')
print()
print('США звонков в апреле:', len(usa_apr), 'и в мае -', len(usa_may))
print('Всего минут в апреле', usa_a, 'на сумму', usa_sa,' в мае ', usa_m, 'на сумму', usa_sm, 'стоимость минуты звонка: ~ 1.5')
print()
print('Германия звонков в апреле:', len(ger_apr), 'и в мае -', len(ger_may))
print('Всего минут в апреле', ger_a, 'на сумму', ger_sa,' в мае ', ger_m, 'на сумму', ger_sm, 'стоимость минуты звонка: ~ 7')
print()
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




print('Потрачено на местные переговоры всего с 1 апреля по 3 июня',listsum(russia2))
print()
print('Потрачено на междугородние переговоры всегос 1 апреля по 3 июня ',listsum(world2))

print(sep*50)
#Повторяющиеся номера 


print('Номера по которым было больше 5 звонков в месяц')
print(sep*50)



counts=[]

for item in world_april:
    if len(item) >= 2:
        counts.append(item[4])

counts_number = Counter(counts)

for key in counts_number:
    if counts_number[key] >=5:
        print('В апреле по номеру',key, 'совершено', counts_number[key], 'звонков')
        
list.clear(counts)

print(sep*50)

for item in world_may:
    if len(item) >= 2:
        counts.append(item[4])

counts_number = Counter(counts)

for key in counts_number:
    if counts_number[key] >=5:
        print('В мае по номеру',key, 'совершено', counts_number[key], 'звонков')

list.clear(counts)
        
print(sep*50)

print('Страны по которым было больше 10 звонков в месяц')
print(sep*50)

#Ищем популярные направления апрель
for item in world_april:
    if len(item) >= 2:
        counts.append(item[3])

counts_number = Counter(counts)

for key in counts_number:
    if counts_number[key] >=10:
        print('В апреле по направлению',key, 'совершено', counts_number[key], 'звонков')

print(sep*50)

list.clear(counts)

#Ищем популярные направления май 
for item in world_may:
    if len(item) >= 2:
        counts.append(item[3])

counts_number = Counter(counts)

for key in counts_number:
    if counts_number[key] >=10:
        print('В мае по направлению',key, 'совершено', counts_number[key], 'звонков')
        
