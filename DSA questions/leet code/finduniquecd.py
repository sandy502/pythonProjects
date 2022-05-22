def findunique(a, n):
    ans = 0

    for i in range (0, n):
        ans = ans ^ a[i] # used for xor operations
    return ans

def main():
    a = [2, 3, 1, 6, 3, 2, 1]
    n = len(a)
    print(findunique(a, n))

if __name__ == "__main__":  # main function
    main()           