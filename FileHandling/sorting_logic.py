class types_of_sorting:
    def sort(new_sort):
        for i in range(len(new_sort)-1,0,-1):
            for j in range(i):
                if new_sort[j]>new_sort[j+1]:
                    var = new_sort[j]
                    new_sort[j] = new_sort[j+1]
                    new_sort[j+1] = var   

class linear_search:
    def search_while(list,n):
        i = 0
        while i < len(list):
            if list[i] == n:
                return True
            i += 1
        return False

    def search_for(list,n):
        for i in range(len(list)):
            if list[i] == n:
                return True
        return False 

class binary_search:
    
    def search_while(list,target):
        end = len(list) - 1
        start = 0
        while start<=end:
            mid = (start+end)//2
            if list[mid] < target:
                start = mid + 1
            elif list[mid] > target:
                end = mid - 1
            else:
                return True
        return False        
