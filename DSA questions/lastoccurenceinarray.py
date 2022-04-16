# Given a sorted array of N integers, 
# write a program to find the index of the last occurrence of the
# target key. If the target is not found then return -1.

# Input: N = 7, target=13, array[] = {3,4,13,13,13,20,40}
# Output: 2
#Brute force
# def lastoccur(arr, n, target):
#     occur = 0
#     for i in reversed(range(n)):
#         if arr[i] == target:
#             occur =  i
#             break
#         else:
#             occur = -1   
#     return occur         

# optimizing solution using binary search
def lastoccur(arr, n, target):
    start = 0
    end = n
    occur = -1
    while start<=end:
        mid = int(start + (end - start) / 2)
        if arr[mid] == target:
            occur = mid
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1   
    return occur            

target=13 
arr = [3,4,13,13,13,20,40] 
n = len(arr)
print(lastoccur(arr, n, target))