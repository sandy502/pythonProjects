def issorted(arr, n):
    if n == 1 or n == 0 :  # base condition
        return True
    if arr[0] > arr[1]:  # check for first
        return False
    else:
        remainingpart = arr[n-1] > arr[n-2] and issorted(arr, n - 1) # recurrence relation
        return remainingpart        


def main():
    arr = [1, 2, 3, 6, 4, 5]
    n = len(arr)
    
    ans = issorted(arr, n)
    if(ans):
        print('sorted')
    else:
        print('unsorted')

if __name__ == "__main__":  # main function
    main() 