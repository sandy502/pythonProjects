from pip import main


def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n-1)

def main():
    n = int(input('number: '))
    print(factorial(n))

if __name__ == "__main__":
    main()        