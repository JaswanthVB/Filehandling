#with open('somefile.txt','w') as f:
   # f.writelines('hi this is babbu')
with open('somefile.txt','r') as f:
    readlines = f.readlines()
with open('somenewfile.txt','r') as f :
    read_lines = f.readlines()
store = []
for lines in readlines:
   if lines == '\n':
      for line in read_lines:
         store.append(line)
   else:
      store.append(lines.rstrip('\n'))  
with open('somenew1file.txt','w') as f:
    for line in store:
        line += '\n'
        f.write(line)

    
       


        