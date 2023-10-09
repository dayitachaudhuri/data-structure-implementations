# ----------------------------------------
# Bubble Sort
# ----------------------------------------
def bubblesort(arr,n):
    for i in range(0,n):
        swapCount = 0
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapCount += 1
        if swapCount == 0:
            break
    return arr

# ----------------------------------------
# Selection Sort
# ----------------------------------------
def selectionsort(arr,n):
    for i in range(0,n-1):
        element = arr[i]
        index = i
        for j in range(i+1,n):
            if arr[j]<element:
                element = arr[j]
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr

# ----------------------------------------
# Insertion Sort
# ----------------------------------------
def insertionsort(arr,n):
    for i in range(1,n-1):
        j = i-1
        while j>=0 and arr[j]>arr[i]:
            arr[j+1] = arr[j]
        arr[i], arr[j+1] = arr[j+1], arr[i]
    return arr

# ----------------------------------------
# Merge Sort
# ----------------------------------------
def mergesortRunner(arr,n):
    mergesort(arr,0,n-1)
    return arr

def mergesort(arr,left,right):
    if left<right:
        mid = (left+right)//2
        mergesort(arr,left,mid)
        mergesort(arr,mid+1,right)
        merge(arr,left,mid,right)

def merge(arr,left,mid,right):
    temp = []
    i = left
    j = mid+1
    while i<=mid and j<=right:
        if arr[i]<arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    while i<=mid:
        temp.append(arr[i])
        i+=1
    while j<=right:
        temp.append(arr[j])
        j+=1
    arr[left:right+1] = temp

# ----------------------------------------
# Quick Sort
# ----------------------------------------

def quicksortRunner(arr,n):
    quicksort(arr,0,n-1)
    return arr

def quicksort(arr,left,right):
    if left<right:
        pivot = partition(arr,left,right)
        quicksort(arr,left,pivot-1)
        quicksort(arr,pivot+1,right)

def partition(arr,left,right):
    l = left
    r = right
    pivot = arr[left]
    while l<r:
        while arr[l]<=pivot:
            l += 1
        while arr[r]>pivot:
            r -= 1
        if l<r:
            arr[l],arr[r] = arr[r],arr[l]
    arr[left] = arr[r]
    arr[r] = pivot
    return r

# ----------------------------------------
# Driver fuction
# ----------------------------------------
def main():
    arr = [3,6,1,7,3,2,1]
    n = len(arr)
    print("Bubble sorted Array -> ", bubblesort(arr,n))
    print("Selection sorted Array -> ", selectionsort(arr,n))
    print("Insertion sorted Array -> ", insertionsort(arr,n))
    print("Merge sorted Array -> ", mergesortRunner(arr,n))
    print("Quick sorted Array -> ", quicksortRunner(arr,n))


if __name__ == '__main__':
    main()