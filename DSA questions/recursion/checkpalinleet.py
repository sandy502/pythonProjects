def isPalindrome(s , i, j):
        if i > j:
            return True
        if new_s[i] != new_s[j]:
            return False
        i = i + 1
        j = j - 1
        return isPalindrome(new_s, i, j)

s = "A man, a plan, a canal: Panama"
new_s = ''.join(i for i in s if i.isalnum())
print(new_s)
new_s = new_s.lower()
print(new_s)
i = 0
j = len(new_s) - 1
print(isPalindrome(new_s, i, j))  


# leetcode answer
# def isPalindrome(self, s: str) -> bool:
# p = ''.join(filter(str.isalnum, s.lower())) # this is an alternative.
#         new_s = ''.join(i for i in s if i.isalnum())
#         new_s = new_s.lower()
#         i = 0
#         j = len(new_s) - 1
#         while i <= j:
            
#             if new_s[i] != new_s[j]:
#                 return False
#             i = i + 1
#             j = j - 1
#         return True  