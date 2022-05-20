# Sliding window technique
# Find max sum of k consecutive elements
# Brute force approach
# def findmaxelement(arr, n, k):
#     ind = []
#     maxsum = 0
#     for i in range(0, n-k):
#         currsum = 0
#         for j in range(0, k):
#             currsum = currsum + arr[i+j]
#         if maxsum < currsum:
#             maxsum = currsum
#     return  maxsum     


# Sliding window concept optimized brute force method

def findmaxelement(arr, n, k):
    currsum = 0
    for i in range(0, k):
        currsum = currsum + arr[i]
    maxsum = currsum
    for i in range(k, n-k):
        # to move the frame or to slide the frame
        currsum = currsum - arr[i-k]
        # to add the new element to the frame
        currsum = currsum + arr[i]
        if maxsum < currsum:
            maxsum = currsum
    return  maxsum   


arr = [1, 7, 6, 2, 3, 4, 5]
n = len(arr)
print(findmaxelement(arr, n, 2))     