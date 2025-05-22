l = 0
list = []

x = input('enter your name:')
y = input('enter your phone number:')

with open('Generator','r') as f:
    Initial_num = f.readlines()
    for num in Initial_num:
        l = int(num) + 1
with open('Generator','w') as f:
    f.writelines(str(l))
with open('StudentData','r') as f :
    list = f.readlines()
    z = str(l) + ',' + x + ',' + y + '\n'
    list.append(z)
with open('StudentData','w') as f:
    for data in list:
        f.write(data)    
   