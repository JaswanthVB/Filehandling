phone = input("Enter your phone number: ")
record = ''
with open("student.deb", 'r') as f:
    for data in f.readlines():
        splitData = data.split(',')
        if splitData[2] == (phone+'\n'):
            record = data

if record:
    print(record)
else:
    print("No record found")