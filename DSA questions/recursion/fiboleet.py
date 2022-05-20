def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
        
    return (fib(n-1) + fib(n-2))

def main():
    n = int(input('number: '))
    print(fib(n))

if __name__ == "__main__":  # main function
    main()     