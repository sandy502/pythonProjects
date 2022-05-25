import sys

def reverseinteger(n):
    ans = 0
    a = False

    if n < 0:
        num = - n
        a = True

    while num != 0:
        if ans >= 2 ** 31 - 1 or ans <= -2 ** 31:  # constraint 
            return -1
        digit = num % 10  # to get single digit from the number
        ans = int(ans * 10 + digit) # to place/reverse the digit from last position yp according positions 
        num = int(num / 10) # to increment the given number
    if a:
        return -ans
    else:    
        return ans
def main():
    n = int(input('enter number: '))

    print(reverseinteger(n))

if __name__ == "__main__":
    main()    