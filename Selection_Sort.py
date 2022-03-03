def Selection_Sort(arr):
    length = len(arr)
    for i in range(length-1):
        min_index = i
        for j in range(i+1,length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index]=arr[min_index],arr[i]







arr=[ 3,5, 7, 2,1 , 0,4]
Selection_Sort(arr)
print(arr)
#check krne code chukiche ahe
# while(i<j-1):   # 0 < 6 0 1 2 3 4 5
#
#         if arr[i] < arr[j] :
#             j=j+1
#         else:
#             arr[i], arr[j] = arr[j], arr[i]
#             i=i+1