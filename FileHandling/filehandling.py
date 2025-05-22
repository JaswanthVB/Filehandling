##To read a unknown file##
#with open('babbuls.txt', 'r') as f:
    #print(f.read())
#f3 = open('babbuls.txt', 'w')
#print('this is f3',f3)
#different functions ##
#read
#readable
#readline
#readlines
#print(f.read())
#print(f.readable())
#print(f.readlines())
## to open a new file which is not existing
#f1 = open('sekar', 'w')
#f1.write('shekar doesnt believe anyone')
#f = open('babbuls.txt','r')
#l1 = f.readlines(15)
#l2 = f.readlines(30)

#print(l1)
#print(l2)
with open('sekar',"r") as f1:
   alllines = f1.readlines()
   print(alllines)
with open("babbuls.txt", "r") as f:
   all_lines = f.readlines()
   print(all_lines)
   
titles = []
sequences = []

#for line in all_lines:
#   if "." in line[0]:
#        titles.append(line.rstrip("\n"))
#        all_lines.remove(line)

#for lines in all_lines:
#    if lines == '\n':
#        for line in alllines:
#            sequences.append(line)
#    else:
#        sequences.append(lines.rstrip("\n"))
#file_path = "babbuls1.txt"
#with open(file_path, "w") as file:
#    for line1 in sequences:
#        line1 += "\n"
 #       file.write(line1)
#with open(file_path,'r') as file:
#    print(file.readlines())
 
 
         
##THIS IS MAKING OF A SMALL DATA CALLING##


#x = input("enter your name:")
#y = input("enter your number:")

#b=0
#studentData = []
#with open('num.deb','r') as f1:
#    num = f1.readlines()
#    for data in num:
#        b = int(data) + 1
#with open("num.deb","w") as f2:
#    f2.writelines(str(b))

#with open("student.deb", 'r') as f:
#    studentData = f.readlines()
#    z = str(b) + ',' + x + ',' + y + '\n'

#    studentData.append(z)

#with open("student.deb", 'w') as f:
#    for data in studentData:
#        f.write(data)







