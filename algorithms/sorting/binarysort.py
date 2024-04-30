# Bubble Sort
# Time complexity => Best: O(n) | Average: O(n^2) | Worst: O(n^2)
# Space complexity => Worst: O(1)

list1_for_loop = [2,6,3,9,45,6,1,26]
swap = False

for i in range(len(list1_for_loop)):
    for j in range(len(list1_for_loop)-1):
        if list1_for_loop[j] > list1_for_loop[j+1]:
            swap = True
            temp = list1_for_loop[j]
            list1_for_loop[j] = list1_for_loop[j+1]
            list1_for_loop[j+1] = temp
    if swap == False:
        break

print(list1_for_loop)


list2_while_loop = [34,56,12,3,89,56,38]
swap = True

while swap==True:
    for j in range(1,len(list2_while_loop)):
        if list2_while_loop[j] < list2_while_loop[j-1]:
            temp = list2_while_loop[j-1]
            list2_while_loop[j-1] = list2_while_loop[j]
            list2_while_loop[j] = temp
            swap = False
    if swap == True:
        break
    else:
        swap = True
        
print(list2_while_loop)