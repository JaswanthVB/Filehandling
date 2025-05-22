input1 = input('What is your operation either delete or update')
number = input('enter your number')
list = []
split = []
with open('StudentData', '+r') as f:
    list = f.readlines()
    if input1 == 'update':
        for datachange in list:
            split1 = datachange.split(',')
            if split1[2] == (number+'\n'):
                split1[1] = str(input('Update your name'))
                datachange = split1[0] +','+ split1[1]+','+ split1[2]
                split.append(datachange)
            else:
                split.append(datachange)
    if input1 == 'delete':
        for datachange in list:
            split1 = datachange.split(',')
            if split1[2] == (number+'\n'):
                #split1[1] = str(input('Update your name'))
                #atachange = split1[0] +','+ split1[1]+','+ split1[2]
                pass
            else:
                split.append(datachange)

with open('StudentData','w') as f:
    for data in split:
        f.write(str(data))