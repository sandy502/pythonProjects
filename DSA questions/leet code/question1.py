#Question 1
#find the elements that have even number of total digits in the list.
#two approaches can be there
#first - we can convert it in strings and get the length of strings.
#second - we can count digits with maths.
# nums = [437,315,322,431,686,264,442]
# evendigits = 0
# for i in range(len(nums)):
#     count = 0
#     while int(nums[i])>0 :
#         count=count+1
#         nums[i]=nums[i]/10
            
#     if count%2 == 0:
#         evendigits = evendigits+1
            
# print(evendigits)


#Question 2
#find the row having the maximum sum.
accounts = [[2,8,7],[7,1,3],[1,9,5]]
max = 0

for i in range(len(accounts)):
    sum = 0
    for j in range(len(accounts[i])):
        sum = sum + accounts[i][j]

    if max < sum:
        max = sum
                
print(max)

#Question 3
#
# nums = [3,2,4,3] 
# target = 9
# lists = []
# numb = 0
# for i in range(len(nums)):
#     if nums[i] == target :
#         numb = nums[i]
#         print(i)
#     elif nums[i] < target :
#         numb = numb + nums[i]
#         lists.append(i)
#     else:
#         continue
#         #print(-1)  

# print(lists)        
