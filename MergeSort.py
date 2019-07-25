arr = [12, 77, 88, 55, 9, 3, 7, 8, 46, 1]                   ## Input unsorted array

def sort(arr):  ## Function to sort the given array in ascending order
    
    ## BASE CASES ##
    if(len(arr) == 1):  ## If length of arr is 1, it is sorted by default
        return arr
    
    elif(len(arr) == 2):    ## If length is 2 then swapping is used, if necessary, to sort the array
        if(arr[0] > arr[1]):
            arr[1], arr[0] = arr[0], arr[1]
        return arr

    ## RECURSION ##
    ## 'arr' is split into two smaller arrays A and B and then they are recursively sorted and then merged using merge() function
    else:
        if(len(arr)%2 == 0):
            A = arr[0 : int(len(arr)/2)]
            B = arr[int(len(arr)/2) : len(arr)]
        else:
            A = arr[0 : int((len(arr)+1)/2)]
            B = arr[int((len(arr)+1)/2) : len(arr)]

        A = sort(A)
        B = sort(B)
        C = merge(A, B)
        return C

def merge(A, B):    ## Function to merge two sorted arrays into one sorted array by sorting back and forth between the two arrays
    C = [0 for i in range(len(A) + len(B))]     ## Initialize the output sorted array (something like C = A + B)
    a = 0                                       ## Counter for A elements
    b = 0                                       ## Counter for B elements
    for k in range(len(C)):
        ## END CASES ##
        ## If all elements of one of the array have been put in 'C', then the remaining elements of the other array are directly copied into 'C'
        if(a >= len(A)):
            C[k:] = B[b:]
            return C
        if(b >= len(B)):
            C[k:] = A[a:]
            return C

        ## TESTING ##
        if(A[a] < B[b]):    ## If a'th element of A is smaller than b'th element of B, then save it into 'C' and compare the next elements
            C[k] = A[a]
            a = a + 1
        else:
            C[k] = B[b]
            b = b + 1
    return C        

    
arr = sort(arr)
print(arr)                                                  ## Output sorted array
