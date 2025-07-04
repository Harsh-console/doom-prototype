arr  = [5,1,4,2,8,7,0,9,3,6]

def merge(arr, start, mid, end):
    arr1 = []
    arr2 = []
    for i in range(mid-start+1):
        arr1.append(arr[start+i])
    for i in range(end-mid):
        arr2.append(arr[mid+i+1])
    i = 0
    j = 0
    k = start
    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i+=1
        else:
            arr[k] = arr2[j]
            j+=1
        k+=1
    while i<len(arr1):
        arr[k] = arr1[i]
        i+=1
        k+=1
    while j<len(arr2):
        arr[k] = arr2[j]
        j+=1
        k+=1
def mergeSort(arr, i, j):
    if i>=j:
        return
    mid = i + (j-i)//2
    mergeSort(arr, i, mid)
    mergeSort(arr, mid+1, j)
    merge(arr, i, mid, j)

mergeSort(arr, 0, len(arr)-1)
for num in arr:
    print(num)
