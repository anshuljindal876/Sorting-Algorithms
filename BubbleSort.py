arr = [12, 77, 88, 55, 9, 3, 7, 8, 46, 1]   ## Input unsorted array
num = 1

while(num):                                 ## Repeat entire operation till no more swaps are possible
    num = 0                                 ## Initiate num as 0
    for i in range(0, len(arr) - 1):
        if(arr[i] >= arr[i+1]):             ## If next adjacent element is bigger, then swap. Replace '<' with '>' to get output as descending order
            num = num + 1
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp

print(arr)                                  ## Output sorted array

