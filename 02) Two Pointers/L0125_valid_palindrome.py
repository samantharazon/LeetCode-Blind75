
# increment L...
# decrement R...
# while... value is NOT alphanumerical (NOT a letter or number)
# check... values are equal
# stop... when they meet in middle (equal) OR surpass (not equal)
def isPalindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1      # minus 1 because len(s) does not account for index position

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1                              # if not letter or number, move by 1
        while r > l and not s[r].isalnum():
            r -= 1                              # if not letter or number, move by 1
        if s[l].lower() != s[r].lower():        # make it lowercase to compare them
            return False
        
        l += 1
        r -= 1
        
    return True


s = "A man, a plan, a canal: Panama<{]':/?"
print("\ns:", s)
result = isPalindrome(s)
print("Is Palindrome: ", result)

s = "race a car"
print("\ns:", s)
result = isPalindrome(s)
print("Is Palindrome: ", result)

s = " =!"
print("\ns:", s)
result = isPalindrome(s)
print("Is Palindrome: ", result)
