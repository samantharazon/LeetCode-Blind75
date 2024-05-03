
def isPalindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1  

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1  
        while r > l and not s[r].isalnum():
            r -= 1 
        if s[l].lower() != s[r].lower():
            return False
        
        l += 1
        r -= 1
        
    return True


s = "\nA man, a plan, a canal: Panama<{]':/?"
result = isPalindrome(s)
print(s)
print("Is Palindrome: ", result)
print("--------------------")

s = "race a car"
result = isPalindrome(s)
print(s)
print("Is Palindrome: ", result)
print("--------------------")

s = " "
result = isPalindrome(s)
print(s)
print("Is Palindrome: ", result)
print("--------------------")
print()