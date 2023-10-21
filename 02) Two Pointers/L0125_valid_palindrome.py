# increment L
# decrement R
# until... they meet in middle (equal) OR surpass (not equal)
# continusly check L is equal to R...
# ...while it is NOT a letter or number (not alphanumerical)
# so we are ignoring whitespaces, periods, etc
# also make it lowercase to compare them

def isPalindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1  # minus 1 because len(s) does not account for index position

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1  # if not letter or number, move by 1
        while r > l and not s[r].isalnum():
            r -= 1 # if not letter or number, move by 1
        if s[l].lower() != s[r].lower():
            return False
        # increment to compare
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