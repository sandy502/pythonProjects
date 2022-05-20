def saydigit(n, num):
    if n == 0:
        return

    digit = int(n % 10)
    n = int(n / 10)

    saydigit(n, num)
    print(num[digit])    

def main():
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    n = int(input('number: '))
    print(saydigit(n, num))

if __name__ == "__main__":  # main function
    main() 