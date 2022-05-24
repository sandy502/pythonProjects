def intersection(a1, a2, n, m):
    new_arr = []
    # for i in range (0, n):
    #     for j in range (0, m):
    #         if a1[i] == a2[j]:
    #             new_arr.append(a2[j])
    #             a2[j] = -231234

    i = 0
    j = 0
    while i < n and j < m:
        if a1[i] < a2[j]:
            i = i + 1
        elif a1[i] == a2[j]:
            new_arr.append(a1[i])
            a2[j] = -1
            i = i + 1
            j = j + 1
        else:
            j = j + 1    

    return new_arr            


def main():
    a1 = []
    a2 = []
    n = int(input('enter size of first array: '))

    for i in range (0, n):
        ele = int(input())
        a1.append(ele)

    print(a1)  
   
    m = int(input('enter size of second array: '))

    for i in range (0, m):
        ele = int(input())
        a2.append(ele)

    print(a2)

    a3 = intersection(a1, a2, n, m) 

    print(a3)
if __name__ == "__main__":
    main()