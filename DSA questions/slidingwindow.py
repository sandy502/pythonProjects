# Sliding window technique
# Find max sum of k consecutive elements

def findmaxelement(arr, n, k):
    ind = []
    maxsum = 0
    for i in range(0, n-k):
        currsum = 0
        for j in range(0, k):
            currsum = currsum + arr[i+j]
        if maxsum < currsum:
            maxsum = currsum
    return  maxsum   

arr = [1, 7, 6, 2, 3, 4, 5]
n = len(arr)
print(findmaxelement(arr, n, 3))   