def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] =  arr[j-1], arr[j]
            j -= 1

arr1 = [5, 1, 13, 18, 11, 44, 31]
insertion_sort(arr1)
print(arr1)