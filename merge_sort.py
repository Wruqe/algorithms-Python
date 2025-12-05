## We are gonna be implementing algorithims in Python, a few for the final exam



array = [2,8,5,3, 9, 4, 1, 7]


def merge_sort(arr):
    print("array before sorting", arr)
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[mid:])
    right = merge_sort(arr[:mid])

    sorted_arr = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1 

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    print("array after sorting", sorted_arr)
    return sorted_arr

if __name__ == "__main__":
    merge_sort(array)




