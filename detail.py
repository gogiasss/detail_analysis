

data = []

with open ('detail.csv',encoding='utf8', mode='r') as f:
    for line in f:
        s = str(line)
        s = s.replace('\n','')
        s = s.replace('"','')
        s = s.replace(',','.')
        s = s.split(';')
        data.append(s)

data_detail=[]

world =[]
russia=[]

for item in data:
    if len(item) >= 3:
        data_detail.append(item)
    else:
        pass

for item in data_detail:
    for i in item:
        if i == ('Исходящий международный'):            
            world.append(item)
            #print(item)
        elif i == ('Исх. междугородний'):
            russia.append(item)
        else:
            pass

world2=[]
for item in world:
    if len(item) >= 2:
        world2.append(float(item[-1]))

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print('Потрачено на междугородние переговоры',listsum(world2))
        
