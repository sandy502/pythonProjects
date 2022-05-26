def subtractProductAndSum(n):
        product = 1
        sm = 0
        digit = 0
        while n != 0:
            digit = n % 10
            product = product * digit
            sm = sm + digit
            n = int(n/10)
            
        ans = product - sm
        return ans

def main():
    n = int(input('enter number: '))

    print(subtractProductAndSum(n))

if __name__ == "__main__":
    main()                