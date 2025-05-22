phone= input('enter your phone number:')
list = []
splitagain = []
with open('StudentData','r') as f:
    list = f.readlines()
    print(list)  
    for namechange in list:
        splitagain1 = namechange.split(',')
        if splitagain1[1] == (phone):
            splitagain1[2] = str(input('update your name:'))
            namechange=splitagain1[0]+','+splitagain1[1]+','+splitagain1[2]
            splitagain.append(namechange)
        else:
            splitagain.append(namechange)
with open('StudentData','w') as f:
    for data in splitagain:
        f.write(str(data))
#for i , lists in enumerate(list):
#if splitagain1[2] == (phone+'\n'):
#list[i] = splitagain
#print(list)
#with open('StudentData','r') as f:
#for namesdata in f.readlines():
#splitdata = namesdata.split(',')
#if splitdata[2] == (phone+'\n'):
#update = str(input('update your name:'))
#record = update