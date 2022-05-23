def insertionsort(a, n):
    if n <= 1:  # base condition
        return a

    print(insertionsort(a, n - 1))   # recurrence relation
    
    # processing
    value_to_be_swapped_at_right_place = a[n - 1]   # here value_to_be_swapped_at_right_place is a value              
    index_of_successor_of_value = n - 2    # index_of_successor_of_value is an index

    while index_of_successor_of_value >= 0 and a[index_of_successor_of_value] > value_to_be_swapped_at_right_place:

        a[index_of_successor_of_value + 1] = a[index_of_successor_of_value]
        # decrementing the value so it can compare all the elements to the left with the value.
        index_of_successor_of_value = index_of_successor_of_value - 1   

    a[index_of_successor_of_value + 1] = value_to_be_swapped_at_right_place
    print(a)


def main():
    a = [7, 4, 9, 1, 3, 2, 5]
    n = len(a) - 1
    insertionsort(a, n)

if __name__ == "__main__":  # main function
    main()     