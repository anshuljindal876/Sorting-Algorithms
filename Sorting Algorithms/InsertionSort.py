arr = [12, 77, 88, 55, 9, 3, 7, 8, 46, 1]   ## Input unsorted array


for i in range(1, len(arr)):
    for j in range(0, i):                   ## Compare the ith element with all those behind it
        if(arr[i] <= arr[j]):               ## If next element is bigger, then swap. Replace '<' with '>' to get output as descending order
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)                                  ## Output sorted array
