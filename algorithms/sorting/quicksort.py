# Quick Sort (Fastest Algo)
# Time complexity => Best: O(nlogn) | Average: O(nlogn) | Worst: O(n^2)
# Space complexity => Worst: O(logn) - Due to Recursive call

list1 = [12,12,23,56,28,40,23,48,79,11]

def quicksort(arr, low, high):
    if low<high:
        pivot_index = get_pivot(arr, low,high)
        quicksort(arr, low, pivot_index-1)
        quicksort(arr, pivot_index+1, high)

def get_pivot(arr, low, high):
    i = low
    j = high
    pivot_element = arr[low]

    while(i<j):
        while arr[i]<=pivot_element:
            i += 1
        while arr[j]>pivot_element:
            j -= 1
        if i<j:
            swap(arr, i, j)
    swap(arr, low, j)
    return j

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

quicksort(list1, 0, len(list1)-1)
print(list1)
