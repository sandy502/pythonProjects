def main():
    n = int(input('number: '))

        # output
        # number: 3
        # * * *

        # * * *

        # * * *

    # i = 1

    # while i <= n:
    #     j = 1
    #     while j <= n:
    #         print('*', end=' ')
    #         j = j + 1
    #     print('\n')   
    #     i = i + 1


        # number: 3
        # 1 1 1

        # 2 2 2

        # 3 3 3

    # i = 1

    # while i <= n:
    #     j = 1
    #     while j <= n:
    #         print(i, end=' ')
    #         j = j + 1
    #     print('\n')   
    #     i = i + 1


        # number: 4
        # 1 2 3 4

        # 1 2 3 4

        # 1 2 3 4

        # 1 2 3 4

    # i = 1

    # while i <= n:
    #     j = 1
    #     while j <= n:
    #         print(j, end=' ')
    #         j = j + 1
    #     print('\n')   
    #     i = i + 1
        

        # number: 4
        # 4 3 2 1

        # 4 3 2 1

        # 4 3 2 1

        # 4 3 2 1

    # i = 1

    # while i <= n:
    #     j = 1
    #     while j <= n:
    #         print(n - j + 1, end=' ')
    #         j = j + 1
    #     print('\n')   
    #     i = i + 1   


        # number: 3
        # 1 2 3

        # 4 5 6

        # 7 8 9

    # i = 1
    # count = 1
    # while i <= n:
    #     j = 1
    #     while j <= n:
    #         print(count, end=' ')
    #         j = j + 1
    #         count = count + 1
    #     print('\n')   
    #     i = i + 1  


        # number: 3
        # *

        # * *

        # * * *

    # i = 1
    # while i <= n:
    #     j = 1
    #     while j <= i:
    #         print('*', end=' ')
    #         j = j + 1
    #     print('\n')   
    #     i = i + 1         


    # number: 3
    # 1

    # 2 2

    # 3 3 3

    # i = 1
    # while i <= n:
    #     j = 1
    #     while j <= i:
    #         print(i, end=' ')
    #         j = j + 1
    #     print('\n')   
    #     i = i + 1 


        # number: 3
        # 1

        # 2 3

        # 4 5 6

    # i = 1
    # count = 1
    # while i <= n:
    #     j = 1
    #     while j <= i:
    #         print(count, end=' ')
    #         j = j + 1
    #         count = count + 1
    #     print('\n')   
    #     i = i + 1 


        # number: 5
        # 1

        # 2 3

        # 3 4 5

        # 4 5 6 7

        # 5 6 7 8 9

    # i = 1
    # while i <= n:
    #     j = 1
    #     value = i
    #     while j <= i:
    #         print(value, end=' ')
    #         j = j + 1
    #         value = value + 1
    #     print('\n')   
    #     i = i + 1 



# try to print wothout using value
    # i = 1
    # while i <= n:
    #     j = 1
    #     value = i
    #     while j <= i:
    #         print(value, end=' ')
    #         j = j + 1
    #         value = value + 1
    #     print('\n')   
    #     i = i + 1   


        # number: 3
        # 1

        # 2 1

        # 3 2 1


    # i = 1
    # while i <= n:
    #     j = 1
    #     while j <= i:
    #         print(i - j + 1, end=' ')
    #         j = j + 1
    #     print('\n')   
    #     i = i + 1  


        # number: 3
        # A A A

        # B B B

        # C C C

    # i = 1
    # ch = 'A'
    # while i <= n:
    #     j = 1
    #     while j <= n:
    #         new_ch = ord(ch) + i - 1
            
    #         print(chr(new_ch), end=' ')
    #         j = j + 1  
    #     print('\n')   
    #     i = i + 1


        # number: 3
        # A B C

        # A B C

        # A B C

    # i = 1
    # ch = 'A'
    # while i <= n:
    #     j = 1
    #     while j <= n:
    #         new_ch = ord(ch) + j - 1
            
    #         print(chr(new_ch), end=' ')
    #         j = j + 1  
    #     print('\n')   
    #     i = i + 1        


        # number: 3
        # A B C

        # D E F

        # G H I

    # i = 1
    # ch = 'A'
    # while i <= n:
    #     j = 1
    #     while j <= n:
            
    #         print(ch, end=' ')
    #         ch = ord(ch) + 1
    #         ch = chr(ch)
    #         j = j + 1  
    #     print('\n')   
    #     i = i + 1


        # number: 3
        # A B D

        # B D G

        # C F J

    # i = 1    
    # while i <= n:
    #     ch = 'A'
    #     j = 1
    #     while j <= n:
    #         ch = ord(ch) + i + j - 2
    #         ch = chr(ch)
    #         print(ch, end=' ')
    #         j = j + 1
        
    #     print('\n')   
    #     i = i + 1 


        # number: 3
        # A

        # B B

        # C C C

    # i = 1
    # while i <= n:
    #     ch = 'A'
    #     ch = ord(ch) + i - 1
    #     ch = chr(ch)   
    #     j = 1
    #     while j <= i:
            
    #         print(ch, end=' ')
    #         j = j + 1
 
        
    #     print('\n')   
    #     i = i + 1         


        # number: 4
        #       *

        #     * *

        #   * * *

        # * * * *

    # i = 1
    # while i <= n:
    #     # print space
    #     space =  n - i
    #     while space:
    #         print(' ', end = ' ')
    #         space = space - 1

    #     # print star
    #     j = 1
    #     while j <= i:
    #         print('*', end = ' ') 
    #         j = j + 1
    #     print('\n')
    #     i = i + 1    


        # number: 5
        #         1

        #       1 2 1

        #     1 2 3 2 1

        #   1 2 3 4 3 2 1

        # 1 2 3 4 5 4 3 2 1

    # i = 1
    # while i <= n:
    #     # print space
    #     space =  n - i
    #     while space:
    #         print(' ', end = ' ')
    #         space = space - 1

    #     # print first triange
    #     j = 1
    #     while j <= i:
    #         print(j, end = ' ') 
    #         j = j + 1

    #     # print second triange
    #     start = i - 1
    #     while start:
    #         print(start, end = ' ')
    #         start = start - 1  
    #     print('\n')
    #     i = i + 1  


        # number: 4
        # X X X X

        # X X X

        # X X

        # X

    # i = 1
    # while i <= n:
    #     j = 1
    #     while j <= n - i + 1:
    #         print('X', end = ' ')
    #         j = j + 1
    #     print('\n')
    #     i = i + 1    


        # number: 3
        # X X X

        #   X X

        #     X    

    # i = 1
    # while i <= n:
    #     # print space
    #     space = 0
    #     while space < i - 1:
    #         print(' ', end = ' ')
    #         space = space + 1

    #     # print X
    #     j = 1
    #     while j <= n - i + 1:
    #         print('X', end = ' ')
    #         j = j + 1
    #     print('\n')
    #     i = i + 1 


        # number: 4
        # 1 2 3 4 4 3 2 1

        # 1 2 3 * * 3 2 1

        # 1 2 * * * * 2 1

        # 1 * * * * * * 1

    i = 1
    while i <= n:

        # print triangle number1
        j = 1
        while j <= n - i + 1:
            print(j, end = ' ')
            j = j + 1


        # print triangle star1
        star1 = 0
        while star1 < i - 1:
            print('*', end = ' ')
            star1 = star1 + 1

        
        # print triangle star2
        star2 = 0
        while star2 < i - 1:
            print('*', end = ' ')
            star2 = star2 + 1

        # print triangle number2      
        j = j - 1
        while j > 0:
            print(j, end = ' ')
            j = j - 1
        print('\n')
        i = i + 1 
        

if __name__ == "__main__":  # main function
    main()   
