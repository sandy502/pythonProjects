def numberOfSteps(num):
    cnt = 0
    while num != 0:
        if num % 2 == 0:
            num = int(num / 2)
            cnt = cnt + 1
        else:
            num = num - 1
            cnt = cnt + 1 

    return cnt       


def main():
    n = int(input('enter number: '))

    print(numberOfSteps(n))

if __name__ == "__main__":
    main() 