def bubbble_sort(arr):

    for i in range(len(arr)-1):  # if len(arr)=6 (0,5) 0 1 2 3 4
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]



# arr=[6,4,8,3,1,2]
arr=[ 3,5, 7, 2,1 , 0,4]
bubbble_sort(arr)

print(arr)
