arr = [1,2,3,4,5]

# def rotate_arr (arr, d):
#     temp = []
#     n = len(arr)
#     for i in range(d,n):
#         temp.append(arr[i])
#     for j in range(0, d):
#         temp.append(arr[j])
#     arr = temp.copy()
#     return arr

# print(rotate_arr(arr, 2))


# this function is for rotating the array number of times it is given like in this case it is d = 2 
def rotate_arr(arr, d):
    n = len(arr)
    for i in range(d):
        rotate(arr, n)
    return arr    
# this array is to shift the elements one by one inside the array
def rotate(arr, n):
    temp = arr[0]
    for j in range(n-1):
        arr[j]=arr[j+1]
    arr[n-1] = temp

print(rotate_arr(arr,2))