

data = []

with open ('detail.csv',encoding='utf8', mode='r') as f:
    for line in f:
        s = str(line)
        s = s.replace('\n','')
        s = s.replace('"','')
        s = s.replace(',','.')
        s = s.split(';')
        data.append(s)

print(len(data))

data_detail=[]


for item in data:
    if len(item) >= 3:
        data_detail.append(item)
    else:
        print(item)
        
print(len(data_detail))


    
        
        

            
