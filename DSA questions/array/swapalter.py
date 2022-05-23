def alterswap(a, n):
    start = 0
    
    for i in range (0, n):
        if start + 1 < n:
            a[start], a[start + 1] = a[start + 1], a[start]
            start = start + 2

    return a    

def main():
    n = int(input('enter size: '))
    a = []

    for i in range (0, n):
        ele = int(input())
        a.append(ele)
    print(a)
    print('alternate swapped values are: ', alterswap(a, n))

if __name__ == "__main__":  # main function
    main() 