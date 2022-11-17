# largest before smallest:  add them up
# smallest before largest:  subtract smaller
def romanToInt(s):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
    
    res = 0

    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:    # check if it's in bounds and...
                                                                # if character at i is smaller than after i
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
        
    return res

s = "III"
result = romanToInt(s)
print(s, ":", result)

s = "LVIII"
result = romanToInt(s)
print(s, ":", result)

s = "MCMXCIV"
result = romanToInt(s)
print(s, ":", result)
