def power(a, b):

    # base condition
    if b == 0:
        return 1
    if b == 1:
        return a

    # reccurrence relation
    ans = power(a, int(b/2))

    # processing 
    if b % 2 == 0:
        return ans * ans
    else:
        return a * ans * ans    


def main():
    a = int(input('number: '))
    b = int(input('power: '))
    print(power(a, b))

if __name__ == "__main__":  # main function
    main() 