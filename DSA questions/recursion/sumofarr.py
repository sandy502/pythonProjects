def sum(arr, n):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    return (arr[n-1] + sum(arr, n-1))    

def main():
    arr = [1, 2, 3, 4]
    n = len(arr)
    print(sum(arr, n))

if __name__ == "__main__":  # main function
    main()     