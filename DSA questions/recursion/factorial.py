def factorial(n):  # funtion
    if n == 0:   # base case
        return 1

    return n * factorial(n-1)  # recurrence relation

def main():
    n = int(input('number: '))
    print(factorial(n))

if __name__ == "__main__":  # main function
    main()        