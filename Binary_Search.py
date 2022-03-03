

def Binary_Search(arr,element):
    start = 0
    end = len(arr)-1
    while(start<=end):
        mid = (start+end)//2
        if element < arr[mid]:
            end = mid -1
        elif element > arr[mid]:
            start = mid +1
        else:
            return mid
    return -1
arr = [1,3,5,7,8,9,15]
element = 15
print(Binary_Search(arr,element))