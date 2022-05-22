def findduplicate(a, n):
    ans = 0

    for i in range (0, n):
        ans = ans ^ a[i] # used for xor operations

    for i in range (1, n):
        ans = ans ^ i  
    return ans

def main():
    a = [4, 2, 1, 3, 1]
    n = len(a)
    print(findduplicate(a, n))

if __name__ == "__main__":  # main function
    main()           