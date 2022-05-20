# Given an array of integers of size N, 
# Our task is to find the maximum difference between 
# two numbers such that (i < j) i.e Order should be maintained.

# Input: N = 5, array[] = {100, 1, 2, 5, 100}
# Output: 99
# Brute force

# def maxdiff(arr, n):
#     curr_maxdiff = 0
#     for i in range(0, n):
#         for j in range(i + 1, n):
#             diff = arr[j] - arr[i]
#             if diff > curr_maxdiff:
#                 curr_maxdiff = diff
#     return curr_maxdiff


# optimized approach

def maxdiff(arr, n):
    curr_maxdiff = arr[1] - arr[0]
    curr_minval = arr[0]
    for i in range(1, n):
        curr_maxdiff = max(curr_maxdiff, arr[i] - curr_minval)
        curr_minval = min(curr_minval, arr[i])

    return curr_maxdiff    

arr = [2, 3, 10, 6, 4, 8, 1]
n = len(arr)
print(maxdiff(arr, n))                