# Given an array/list 'ARR' of integers and a position ‘M’. 
# You have to reverse the array after that position.


def reverseArray(arr, m):
    # Write your code here.
    n = len(arr)
    i = m + 1
    while i + 1 < n:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i = i + 1
    print(arr)

def main():
    a = [10, 9, 8, 7, 6]
    m = 2
    reverseArray(a, m)

if __name__ == "__main__":
    main()