def isPowerOfTwo(n):
    # if n <= 0:
    #         return False
    #     return 3**round(math.log(n, 3)) == n

    # if n==1:
    #     return True
    # if n%2==0 or n==0:      #if the number is even it can't be power of 3 , (same goes with 2 and 4 but the number can not be ODD )
    #     return False
    
    # while n%3==0:           #works until the remainder is zero   eg. (9%3==0)
    #     n=n//3
    #     if n==1:            # If n becomes 1 it means it comes down to its last value so we return True
    #         return True
    #     if n%3!=0:         # if the remainder becomes anything other than 0 , we return False
    #         return False
    # return False

    # same for power of 3 and 4
        for i in range (0, 31):
            ans = pow(2, i)
            
            if ans == n:
                return True
        return False 

        

def main():
    n = int(input('enter number: '))

    print(isPowerOfTwo(n))

if __name__ == "__main__":
    main() 