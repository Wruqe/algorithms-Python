from merge_sort import array



## I just imported the same array in the merge sort file so I dont have to keep duplicating 


def bubble_sort(array):
    print("Array before sorting", array)
    length_of_array = len(array)


    for i in range(length_of_array):
        swapped = False

        for j in range(0, length_of_array - i - 1):
            if array[j] > array[j + 1 ]: 
                array[j], array[j + 1] = array[j + 1 ], array[j]
            swapped = True

        ## If we go a whole pass without sorting its sorted already so lets break the loop
        if not swapped:
            break
    print("Array after sorting", array)
    return array

bubble_sort(array)
