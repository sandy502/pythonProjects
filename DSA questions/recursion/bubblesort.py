def bubblesort(a, n):
    # base condition
    if n == 0 or n == 1:
        return a

    # processing 
    for i in range(0, n):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]

    # recurrence relation
    print(bubblesort(a, n-1))        


def main():
    a = [7, 4, 9, 1, 3, 2, 5]
    n = len(a) - 1
    bubblesort(a, n)

if __name__ == "__main__":  # main function
    main() 