# encodes a list of strings to a single string
# Encoded:  4#lint4#code4#love3#you
def encode(input):
    res = ""
    for word in input:
        res += str(len(word)) + "#" + word # length of word + # + word
    print(res)
    return res

# decodes a single string to a list of strings 
# Decoded:  ['lint', 'code', 'love', 'you'] 
def decode(input):
    res, index_len = [], 0 

    while index_len < len(input):  
        pound_pos = index_len       

        while input[pound_pos] != "#":
            pound_pos += 1          

        actual_len = int(input[index_len:pound_pos]) # get value at index where we placed length of word
        res.append(input[pound_pos+1 : pound_pos+1+actual_len]) # add the word to res
        index_len = pound_pos + 1 + actual_len # update current position
        
    return res


input = ["lint", "code", "love", "you"]
encoded = encode(input)
print("\nEncoded: ", encoded)
decoded = decode(encoded)
print("Decoded: ", decoded)
print()

input = ["we", "say", ":", "yes"]
encoded = encode(input)
print("\nEncoded: ", encoded)
decoded = decode(encoded)
print("Decoded: ", decoded)
print()

input = ["neet", "code"]
encoded = encode(input)
print("\nEncoded: ", encoded)
decoded = decode(encoded)
print("Decoded: ", decoded)
print()
