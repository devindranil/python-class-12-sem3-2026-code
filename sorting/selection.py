def selection_sort(arr):
    n=len(arr) # get the total number of elements in the list
    # outer loop
    # this loop moves one element at a time
    for i in range(n):
        # assume the current position contains
        # the smallest element
        min_index=i
        # inner loop
        # used to find the actual smallest elementr
        # in the remaining unsorted array
        for j in range(i+1,n):
            # compare current element with the current minimum element
            if arr[j]<arr[min_index]:
                # update minimum index if smaller element is found
                # update to current element
                min_index=j
        # swap the smallest element if found
        # with the element at current position
        arr[i],arr[min_index]=arr[min_index],arr[i]

        # print array after each pass
        print("After Pass: ",i+1," :",arr)
    #return the sorted array
    return arr


numbers = [64,25,12,22,11] #unsorted array

print("Original array: ")
print(numbers)

selection_sort(numbers)
print("Sorted Array: ")
print(numbers)