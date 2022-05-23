# how to initialize it

# a = []  # empty list

# note: list can take several datatypes as input in single list 
# whereas array takes same type os elements as input in one array.

# how we take inputs

# n = int(input('enter the size:'))

# for i in range (0, n):
#     ele = int(input())  # we are only taking integer value as input in an array
#     a.append(ele)

# print(a)   

# initializing whole array with single value

# arr = [0] * n

# print(arr)

# find minimum and maximum in array

# mini = min(a)
# maxi = max(a)
# print(mini , maxi)


def sumofarr(a, n):
    sum = 0
    for i in range (0, n):
        sum = sum + a[i]
    return sum 

def searchele(a, n, val):
    for i in range (0, n):
        if a[i] == val:
            return True
    return False  

def reversearr(a, n):
    start = 0
    end = n - 1
    while start <= end:
        a[start], a[end] = a[end], a[start]
        start = start + 1
        end = end - 1
    return a

def main():
    n = int(input('enter size: '))
    a = []

    for i in range (0, n):
        ele = int(input())
        a.append(ele)
    print(a)    


    # print(sum(a))
    # print('sum: ', sumofarr(a, n)) 

    # linear search an element in an array
    # val = int(input('enter value to be searched: '))
    # print('The element present status is: ', searchele(a, n, val)) 

    # reverse an array
    # reverse = list(reversed(a)) # here we dont change the original array 
    # it returns a list of reversed array

    # it changes the original array and returns it.
    # a.reverse()
    # print(a)

    # using slicing we create new list of reversed array preserving the old one
    # reverse = a[::-1]
    # print(reverse)

    print('reversed array is: ', reversearr(a, n)) 
    
if __name__ == "__main__":  # main function
    main()   