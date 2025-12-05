from merge_sort import array, merge_sort



target = 3

def binary_search(array, target):
    ## this is slow, dont do this is is just for sorting it in the meantime. 
    ## only use binary search on a sorted array, hence thats why im sorting it lazily here
    sorted_array = merge_sort(array)

    low = 0
    high = len(sorted_array) -  1
    while low <= high:
        mid = (low + high) // 2 


        if target == sorted_array[mid]:
            return mid
        if target > sorted_array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print("target index", binary_search(array, target))        


