
# ----------------------------------------
# Linear Search
# ----------------------------------------
def linearSearch(arr, item):
    for i in range(0,len(arr)):
        if arr[i] == item:
            return i
    return -1

# ----------------------------------------
# Binary Search
# ----------------------------------------

# RECURSIVE
def binSearchrec(arr, minim, maxim, x): 
    if minim<=maxim and minim>=0:
        mid = (maxim+minim)//2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] < x: 
            return binSearchrec(arr, mid+1, maxim, x) 
        else: 
            return binSearchrec(arr, minim, mid-1, x) 
    else:  
        return -1
  
# ITERATIVE
def binSearchit(arr, minim, maxim, x): 
    while minim<=maxim: 
        mid = (minim+maxim)//2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] < x: 
            minim = mid + 1
        else: 
            maxim = mid - 1
    return -1

# ----------------------------------------
# Driver fuction
# ----------------------------------------
def main():
    arr = [3,6,1,7,12,9,10]
    item = 9
    n = len(arr)
    print("Array is", arr, "Item is", item)
    print("Using Linear Search -> ", linearSearch(arr,item))
    print()
    arr.sort()
    print("Array is", arr, "Item is", item)
    print("Using Recursive Binary Search -> ", binSearchrec(arr,0,n-1,item))
    print("Using Iterative Binary Search -> ", binSearchrec(arr,0,n-1,item))

if __name__ == '__main__':
    main()
