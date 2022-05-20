#Binary search

# arr = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]
# start = 0
# end = len(arr) - 1

#this is iterative method
# def binarySearch(arr,target,start,end):
#     while end >= start:
#         mid = int(start + (end-start)/2)

#         if target < arr[mid] :
#             end = mid - 1
            
#         elif target == arr[mid] :
#             return mid       
#         else:
#             start = mid + 1
                
    
#     print("no item found!!!")
#     return -1 

#this is recursive method
# def binarySearch(arr,target,start,end):
#     if end >= start:
#         mid = int(start + (end-start)/2)

#         if target < arr[mid] :
#             end = mid-1
#             return binarySearch(arr,target,start,end)
            
#         elif target == arr[mid] :
#             return mid       
#         else:
#             start = mid + 1
#             return binarySearch(arr,target,start,end)
                    
#     else:
#         print("no item found!!!")
#         return -1 

# result = binarySearch(arr,7,start,end)
# print(result)

# Order agnostic binary search
#here we give importance to the order in which our list is given, asc or desc.
#here also we have used iterative method
# def binarySearch(arr,target,start,end):

#     if arr[start] < arr[end] :
#         asc = True
#     else:
#         asc = False

#     while start <= end :
#         mid = int(start + (end-start)/2)

#         if target == arr[mid] :
#             return mid

#         if asc:
#             if target < arr[mid] :
#                 end = mid - 1
#             else:
#                 start = mid + 1
#         else:
#             if target > arr[mid] :
#                 end = mid - 1
#             else:
#                 start = mid + 1       
    
#     print("element not found!!!")
#     return -1


# arr = [78 , 23 , 3 , 1 , 0 , -1]  
# target = 80
# start = 0
# end = len(arr) - 1

# n = binarySearch(arr,target,start,end)
# print(n)

#Ceiling of a number
# ceiling of a number is smallest number in the list geater than or equal to the target.
#here we have used iterative method and we are assuming that we have given list in ascending order.
# def ceiling(arr,target,start,end):
#     if target > arr[end] :
#         return -1
#     while end >= start:
#         mid = int(start + (end-start)/2)

#         if target < arr[mid] :
#             end = mid - 1
#             # return ceiling(arr,target,start,end)
#         elif target == arr[mid] :
#             return mid       
#         else:
#             start = mid + 1
#             # return ceiling(arr,target,start,end)    
    
#     return start

# arr = [1, 2 ,4, 6, 30, 56, 78]
# target = 10
# start = 0
# end = len(arr) - 1     

# n = ceiling(arr,target,start,end)
# print(n)


#Floor of a number

# def floor(arr,target,start,end):
#     if target < arr[end] :
#         return -1
#     if end >= start:
#         mid = int(start + (end-start)/2)

#         if target < arr[mid] :
#             end = mid - 1
#             return floor(arr,target,start,end)
#         elif target == arr[mid] :
#             return mid       
#         else:
#             start = mid + 1
#             return floor(arr,target,start,end)    
#     else:
#         return end

# arr = [1, 2 ,4, 6, 30, 56, 78]
# target = -1
# start = 0
# end = len(arr) - 1     

# n = floor(arr,target,start,end)
# print(n)

# https://leetcode.com/problems/find-smallest-letter-greater-than-target/


# def nextGreatestLetter(self, letters, target) -> str:
#         start = 0
#         end = len(letters) - 1 
#         while start <= end:
#             mid = int(start + (end-start)/2)

#             if target < letters[mid] :
#                 end = mid - 1      
#             else:
#                 start = mid + 1   

#         return letters[start % len(letters)]

# letters = ["c","f","j"]
# target = "d"
# n = nextGreatestLetter(letters,target)
# print(n)

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# def searchRange(nums, target):
#         ans = [-1,-1]
#         def search(nums, target, startindex):
#             ans = -1
#             start = 0
#             end = len(nums) - 1 
#             while end >= start:
#                 mid = int(start + (end-start)/2)

#                 if target < nums[mid] :
#                     end = mid - 1
#                 elif target == nums[mid] :
#                     ans = mid
#                     if startindex :
#                         end = mid - 1
#                     else :
#                         start = mid + 1           
#                 else:
#                     start = mid + 1    
#             return ans
#         start = search(nums, target, True)
#         end = search(nums, target, False) 

#         ans[0] = start
#         ans[1] = end

#         return ans


# nums = [20,34,34,34,45,56,56,56,56,67,67,67,78,89,90,100]
# target = 67    
# n = searchRange(nums,target)
# print(n)

# https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/

# Program to demonstrate working of an algorithm that finds an element in an array of infinite size
# we are trying not to use length function to calculate the indices.

# def binarySearch(arr,target,start,end):
#     while end >= start:
#         mid = int(start + (end-start)/2)

#         if target < arr[mid] :
#             end = mid - 1
            
#         elif target == arr[mid] :
#             return mid       
#         else:
#             start = mid + 1
                
    
#     print("no item found!!!")
#     return -1 

# def findingrange(arr,target):
#     start = 0
#     end = 1
#     # here we are trying to take a range in between our target will lie
#     while target > arr[end]:
#         temp = end + 1
#         # double the box value
#         end = end + (end - start + 1)*2
#         start = temp

#     return binarySearch(arr,target,start,end)

# arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# target = 9
# ans = findingrange(arr,target)
# print(ans)  

# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# 

# mountain array or bi-tonic array is first it starts to increases then decreases 
# and we have to find the max peak reached once it starts decreasing

# inshort finding the maximum value in the array

# def peakIndexInMountainArray(arr):
#     start = 0
#     end = len(arr) - 1  

#     while start < end :
#         mid = int(start + (end-start)/2)
#         if arr[mid] > arr[mid + 1]:
#             end = mid
#         else:
#             start = mid + 1

#     return start            


# https://leetcode.com/problems/find-in-mountain-array/

# function to find peak index in mountain array
# def peakIndexInMountainArray(mountain_arr):
#     start = 0
#     end = len(mountain_arr) - 1 
#     while start < end :
#         mid = int(start + (end-start)/2)
#         if mountain_arr[mid] > mountain_arr[mid + 1]:
#             end = mid
#         else:
#             start = mid + 1

#     return start

# #  function to search the index of the target
# def OrderAgnosticbinarySearch(mountain_arr,target,start,end):

#     if mountain_arr[start] < mountain_arr[end] :
#         asc = True
#     else:
#         asc = False

#     while start <= end :
#         mid = int(start + (end-start)/2)

#         if target == mountain_arr[mid] :
#             return mid

#         if asc:
#             if target < mountain_arr[mid] :
#                 end = mid - 1
#             else:
#                 start = mid + 1
#         else:
#             if target > mountain_arr[mid] :
#                 end = mid - 1
#             else:
#                 start = mid + 1       
    
#     print("element not found!!!")
#     return -1

# def findInMountainArray(mountain_arr,target):
#     peak = peakIndexInMountainArray(mountain_arr)  
#     firstside = OrderAgnosticbinarySearch(mountain_arr,target,0,peak)
#     if firstside != -1:
#         return firstside
    
#     return OrderAgnosticbinarySearch(mountain_arr,target,peak+1,len(mountain_arr)-1)



# mountain_arr = [1,2,3,4,5,3,1]
# target = 3

# n = findInMountainArray(mountain_arr,target)
# print(n)


# https://leetcode.com/problems/search-in-rotated-sorted-array/

def searchit(nums, target):
    #something here
    pivot = findPivot(nums)
    print("hey")
    if pivot == -1:
        return binarySearch(nums, target, 0, len(nums)-1)

    if nums[pivot == target]:
        return pivot

    if target >= nums[0]:
        return binarySearch(nums, target, 0, pivot - 1)

    return binarySearch(nums, target, pivot+1, len(nums)-1)    


def binarySearch(nums,target,start,end):
    while end >= start:
        mid = int(start + (end-start)/2)

        if target < nums[mid] :
            end = mid - 1
            
        elif target == nums[mid] :
            return mid       
        else:
            start = mid + 1
                
    
    print("no item found!!!")
    return -1 


def findPivot(nums):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = int(start + (end-start)/2)
        #4 cases
        if mid < end and nums[mid] > nums[mid+1]:
            return mid
        if mid > start and nums[mid] < nums[mid-1]:
            return mid-1   
        if nums[mid] <= nums[start]:
            end = mid - 1
        else:
            start = mid +1
    return -1         

nums = [4,5,6,7,0,1,2]
target = 0
n = searchit(nums, target)
print(n)
      