def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print("After Pass: ",i+1," :",arr)
    return arr

n=[64,34,25,12,22,11,90]
print("Original Array: ",n)
bubble_sort(n)
print("Sorted Array: ",n)