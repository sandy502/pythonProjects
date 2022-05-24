def pairsum(a, n, s):
    ans = []
    for i in range (0, n):
        j = i + 1
        while j < n:
            if a[i] + a[j] == s:
                temp = []
                temp.append(min(a[i], a[j]))
                temp.append(max(a[i], a[j]))
                ans.append(temp)
            j = j + 1

    return sorted(ans)            

def main():
    a1 = []
    n = int(input('enter size of first array: '))

    for i in range (0, n):
        ele = int(input())
        a1.append(ele)

    print(a1)  
    s = int(input('enter sum: '))
    # m = int(input('enter size of second array: '))

    # for i in range (0, m):
    #     ele = int(input())
    #     a2.append(ele)

    # print(a2)

    print(pairsum(a1, n, s)) 

if __name__ == "__main__":
    main()