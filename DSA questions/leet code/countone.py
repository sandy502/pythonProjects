# Problem Statement: Given a sorted binary array
# (consisting of only 0’s and 1’s), 
# the task is to find the total number of 1’s in the given array.


# brute force
# def countone(arr, n):
#     cnt = 0
#     for i in range(0, n):
#         if arr[i] == 1:
#             cnt = n-i
#             break
#     return cnt

     

# optimized approach can be using binary search

def countone(arr, n):
    start = 0
    end = n
    cnt = 0
    while start <= end:
        mid = int(start + (end - start) / 2)
        if arr[mid] < 1:
            start = mid + 1
        else:
            cnt = n - mid
            end = mid - 1
    return cnt                 

arr = [0,0,0,1,1,1,1,1,1]
n = len(arr)
print(countone(arr, n))   