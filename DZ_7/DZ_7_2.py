
def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True


old_list = [19, 2, 31, 45, 6, 11, 121, 27]
print(old_list)
bubble_sort(old_list)
print(old_list)
