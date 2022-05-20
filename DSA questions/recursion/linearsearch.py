def linearsearch(arr, n, ele):

    # base condition
    if n == 0:
        return False
    return arr[n-1] == ele or linearsearch(arr, n-1, ele)        

def main():
    arr = [1, 2, 3, 6, 4, 5]
    n = len(arr)
    ele = int(input())
    ans = linearsearch(arr, n, ele)
    if(ans):
        print('found')
    else:
        print('not found')

if __name__ == "__main__":  # main function
    main()