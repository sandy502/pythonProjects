def selectionsort(a, i, n):
    # base condition
    if i == n:
        return a 

    # processing
    minval = i
    for j in range(i, n):
        if a[minval] > a[j]:
            minval = j

    a[minval], a[i] = a[i], a[minval]     

    print(selectionsort(a, i+1, n))

def main():
    a = [7, 4, 9, 1, 3, 2, 5]
    i = 0
    n = len(a) - 1
    selectionsort(a, i, n)

if __name__ == "__main__":  # main function
    main() 