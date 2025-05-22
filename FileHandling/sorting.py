             
from sorting_logic import types_of_sorting
sort_phone = []


with open('StudentData', 'r') as f:
    list = f.readlines()
    for data in list:
        splitdata = data.split(',')
        splitteddata = splitdata[1]
        if splitteddata == 'phonenumber':
            pass
        else:
            sort_phone.append(int(splitteddata))
new_sort = sort_phone #[int(item) for item in sort_phone]
print(new_sort)
print(sort_phone)        
types_of_sorting.sort(new_sort) 
print(new_sort) 
test = []
with open ('StudentData','r') as f:
    list = f.readlines()
    for data in new_sort:
        for storing in list:
            split = storing.split(',')
            print(split[1])
            print(data)
            if str(split[1]) == str(data):
                test.append(storing)
print(test)        
with open('StudentData','w') as f:
    f.writelines(test)
