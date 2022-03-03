def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i-1
        temp = arr[i]
        for i in range(1,len(arr)):
            j=i-1
            temp=arr[i]
            while(j>=0) and arr[j]>temp:
                arr[j+1]=arr[j]
                j=j-1
            arr[j+1]=temp

arr=[ 3,5, 7, 2,1 ,3, 0,4]
insertion_sort(arr)

print(arr)