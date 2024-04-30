# Selection Sort
# Time complexity => Best: O(n^2) | Average: O(n^2) | Worst: O(n^2)
# Space complexity => Worst: O(1)

from numpy import array
list1 = array(7,int)
list1 = [23,13,45,8,13,89,7]

print("Unsorted Array:\n", list1)

for i in range(0,len(list1)-1):
    min_index = i
    for j in range(i+1,len(list1)):
        if list1[min_index] > list1[j]:
            min_index = j
    temp = list1[i]
    list1[i] = list1[min_index]
    list1[min_index] = temp

print("Sorted Array:\n", list1)


