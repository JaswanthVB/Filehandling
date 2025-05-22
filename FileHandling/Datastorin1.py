l = 0
dict = []#a variable to store the data

x = input('enter your name:')#taking input of name from user
y = input('enter your phone number:')#taking input of phone number from user
with open('Generator','r') as f:#generating roll number
    Initial_num = f.readlines()
    for num in Initial_num:
        l = int(num) + 1
with open('Generator','w') as f:#storing the generated roll number
    f.writelines(str(l))
with open('StudentData','r') as f :#opening the file to read
    dict = f.readlines()  #reading the file
    z = str(l) + ',' + y + ',' + x +'\n'
    dict.append(z)#appending the data to the list
with open('StudentData','w') as f:#writing the data to the file
    for data in list:
        f.write(data)   