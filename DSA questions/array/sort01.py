def sort01(a, n):
    ans = []
    i = 0
    j = n - 1
    while i <= j:
        if a[i] > a [j]:
            a[i], a[j] = a[j], a[i]
            i = i + 1
            j = j - 1 
        
        elif a[i] == a[j]:
            j = j - 1
        else:
            i = i + 1    
    ans.append(a)        
    return ans
def main():
    a = []
    n = int(input('enter size of first array: '))

    for i in range (0, n):
        ele = int(input())
        a.append(ele)

    print(a)

    print(sort01(a, n))
if __name__ == "__main__":
    main()