def bin2dec(n):

    ans = 0
    i = 0
    # when we are working with integer input and not binary input
    # while n != 0:
    #     bit = n & 1
    #     ans = bit * pow(10, i) + ans

    #     n = n >> 1
    #     i = i + 1
    # when we are working on binary input 
    while n != 0:
        digit = n % 10
        if digit == 1:
            ans = ans + pow(2, i)

        n = int(n / 10)
        i = i + 1

    return ans    

def main():
    n = int(input('enter number: '))

    print(bin2dec(n))

if __name__ == "__main__":
    main()    