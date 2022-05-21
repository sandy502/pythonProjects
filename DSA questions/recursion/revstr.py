def reverse(i, j, lstr):
    # print(lstr)
    if j == 0:
        return []
    if j == 1:
        return lstr    
    if i>j:
        return lstr
    temp = lstr[i]
    lstr[i] = lstr[j]
    lstr[j] = temp

    print(reverse(i+1, j-1, lstr))

def main():
    str1 = 'sandaly'
    i = 0
    j = len(str1)-1
    lstr = list(str1)
    reverse(i, j, lstr)

if __name__ == "__main__":  # main function
    main()  