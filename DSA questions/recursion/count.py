def count(n):  # funtion
    if n == 0:   # base case
        return
    print(n)      # processing condition
    return count(n-1)  # recurrence relation

def main():
    n = int(input('number: '))
    print(count(n))

if __name__ == "__main__":  # main function
    main()   