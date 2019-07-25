arr = [12, 77, 88, 55, 9, 3, 7, 8, 46, 1]                   ## Input unsorted array


temp = 1000     ## Temporary Variable
min_i = 0       ## Counter which stores the index of (min_i + 1)th smallest element of the array.
                    ## For example, if min_i = 7, then, arr[min_i] would store the 8th smallest element
                    ## in the original 'arr'(which was given as input).

for i in range(0, len(arr)):
    temp = min(arr[min_i : len(arr)])                       ## 'temp' stores the minimum value of the unsorted elements of arr
    ind = arr.index(min(arr[min_i : len(arr)]))             ## Stores the index of 'temp' inside 'arr'

    """
    Here, the elements of 'arr' are shifted by 1 to the right and then the smallest value is shifted leftwards to the first place.
    Same is repeated for the second smallest value - all elements having indices (2 to len(arr)) are shifted to the right and the second smallest value is put in the secon place.
    """
    arr[min_i + 1: ind + 1] = arr[min_i : ind]              ## Shift the values upto index 'ind' to the right.
    arr[ind + 1: len(arr)] = arr[ind + 1 : len(arr)]        ## Retain the values after index 'ind'
    arr[min_i] = temp                                       ## Assign the (min_i + 1)th smallest element of the array (=temp) to the 'min_i' index of ;arr'
    min_i = min_i + 1                                       ## Increment min_i

print(arr)                                                  ## Output sorted array


