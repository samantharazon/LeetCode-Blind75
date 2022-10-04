def isPalindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1  # minus 1 because len(s) does not account for index position

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while r > l and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        
        l = l + 1
        r = r - 1
    return True


s = "A man, a plan, a canal: Panama"
result = isPalindrome(s)
print(s)
print("\nIs Palindrome: ", result)
print("--------------------")

s = "race a car"
result = isPalindrome(s)
print(s)
print("\nIs Palindrome: ", result)
print("--------------------")

s = " "
result = isPalindrome(s)
print(s)
print("\nIs Palindrome: ", result)
print("--------------------")