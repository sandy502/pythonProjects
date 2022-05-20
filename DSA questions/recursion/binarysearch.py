def binarySearch(arr,target,start,end):
    if end >= start:
        mid = int(start + (end-start)/2)

        if target < arr[mid] :
            end = mid-1
            return binarySearch(arr,target,start,end)
            
        elif target == arr[mid] :
            return mid       
        else:
            start = mid + 1
            return binarySearch(arr,target,start,end)
                    
    else:
        print("no item found!!!")
        return -1 

def main():
    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    ele = int(input())
    ans = binarySearch(arr, ele, 0, n-1)
    print(ans)

if __name__ == "__main__":  # main function
    main()        