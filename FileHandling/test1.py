# def sort(list):
#     for i in range(len(list)-1,0,-1):
#         for j in range(i):
#             if list[j]>list[j+1]:
#                 var = list[j]
#                 list[j] = list[j+1]
#                 list[j+1] = var
# list = ['1111','2','3','4','22','5','54','34','27']
# print([int(item) for item in list])
# #print(sort(list))
# print(list)
# string = "some of my characters"
# print(string.replace("ome","owe"))
def searching(list,n):
    l = 0
    u = len(list)-1
    while l<=u:
        mid = (l+u)//2
        
        if list[mid]<n:
            l = mid + 1
        elif list[mid]>n:
            u = mid - 1
        else:
            print(list[mid])
            print("found here")
            return True
    print("Not Found")
    return False       


list = [1,2,3,4,5,6,7,8,9]
n = input("Enter the number to search From (1to9): ")
n = int(n)
searching(list,n)

##PROGRAMME TO CALCULATE THE FACTORIAL OF A NUMBER
