#Question 1
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


Question 2
accounts = [[2,8,7],[7,1,3],[1,9,5]]
max = 0

for i in range(len(accounts)):
    sum = 0
    for j in range(len(accounts[i])):
        sum = sum + accounts[i][j]

    if max < sum:
        max = sum
                
print(max)
      
