phone = input('enter your phone number:')
record = ''

with open ('StudentData','r') as f:

    for data in  f.readlines():
        splitdata = data.split(',')
        if splitdata[1] == (phone):
            record = data

if record:
    split = record.split(',')
    print('rollno:',split[0])
    print('phone no:',split[1]) 
    print('name:',split[2] )  
else:
    print('record not found')             