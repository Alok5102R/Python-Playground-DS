# Merge Sort
# Time complexity => Best: O(nlogn) | Average: O(nlogn)
# Space complexity => Worst: O(n)

arrayList:list = [2,56,4,78,37,39,56,8,47]
low = 0
high = len(arrayList)-1


# Merge function to merge arrays in sorted manner
def merge(arr:list[int], low:int, mid:int, high:int):
    temp:list[int] = []
    left = low
    right = mid+1

    while left<=mid and right<=high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    while left<=mid:
        temp.append(arr[left])
        left+=1

    while right<=high:
        temp.append(arr[right])
        right+=1

    for i in range(low,high+1):
        arr[i] = temp[i-low]


# Mergesort function to sort elements recursively
def mergesort(arr:list[int], low:int, high:int):
    mid = (low+high)//2
    if(low>=high):
        return
    mergesort(arr, low, mid)
    mergesort(arr, mid+1, high)
    merge(arr,low,mid,high)

mergesort(arrayList,low,high)
print(arrayList)
