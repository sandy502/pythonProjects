def power(n):  # funtion
    if n == 0:   # base case
        return 1

    return 2 * power(n-1)  # recurrence relation

def main():
    n = int(input('number: '))
    print(power(n))

if __name__ == "__main__":  # main function
    main()   