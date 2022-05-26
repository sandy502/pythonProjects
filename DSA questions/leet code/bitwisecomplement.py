def bitwiseComplement(n):
        m =n
        mask = 0
        if n == 0:
           return 1
        while m != 0:
            mask = (mask << 1) | 1
            m = m >> 1
            
        ans = (~n) & mask
        
        return ans

def main():
    n = int(input('enter number: '))

    print(bitwiseComplement(n))

if __name__ == "__main__":
    main()            