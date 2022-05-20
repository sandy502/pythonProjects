# Given an array of integers and a number K. 
# Find the count of distinct elements in 
# every window of size K in the array.

# brute force
def window(arr, k):
    cnt = 0
    for i in range(0, k):
        j = 0
        for j in range(0, i):
            if arr[i] == arr[j]:
                break
            else:
                j = j + 1
        if i == j:
            cnt=cnt+1
    return cnt       

def countele(arr, n, k):
    for i in range(n-k+1):
        print(window(arr[i : k + i], k))

k=4
arr = [ 1, 2, 1, 3, 4, 2, 3]
n = len(arr)
countele(arr, n, k)         