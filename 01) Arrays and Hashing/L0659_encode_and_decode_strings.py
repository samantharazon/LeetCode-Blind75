
# encodes a list of strings to a single string
def encode(input):
    res = ""
    for word in input:
        res += str(len(word)) + "#" + word 
    return res

# decodes a single string to a list of strings
def decode(input):
    res, curr_pos = [], 0 # make result array and pointer i to store position in current string

    while curr_pos < len(input):    # while i in bounds...
        pound_pos = curr_pos        # second pointer j

        while input[pound_pos] != "#":
            pound_pos += 1            # increment until we get to # character

        length = int(input[curr_pos:pound_pos]) # go from i to j but not including j -> length tells us how many characters we have to read after j to get every character of string
        res.append(input[pound_pos+1 : pound_pos+1+length]) # gives us entire string & append to result
        curr_pos = pound_pos + 1 + length # update pointer i to beginning of next string (or end of entire string)
        
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
