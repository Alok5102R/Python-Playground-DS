# Insertion Sort
# Time complexity => Best: O(n) | Average: O(n^2) | Worst: O(n^2)
# Space complexity => Worst: O(1)

list1 = [1,45,23,6,1,9,34]

for i in range(len(list1)):
    j = i
    while(j>0 and list1[j-1]>list1[j]):
        temp = list1[j-1]
        list1[j-1] = list1[j]
        list1[j] = temp
        j -= 1

print(list1)
