
# encodes a list of strings to a single string
#.      ["lint","code","love","you"]
#. >>>  4#lint4#code4#love3#you
def encode(input):
    res = ""
    for word in input:
        res += str(len(word)) + "#" + word
    return res

# decodes a single string to a list of strings 
#.      4#lint4#code4#love3#you
#. >>>  ["lint","code","love","you"]
def decode(input):
    res = []
    len_index = 0

    while len_index < len(input):
        pound_pos = len_index

        while input[pound_pos] != "#":
            pound_pos += 1

        len_val = int(input[len_index:pound_pos]) # get value at index where length of word
        word = input[pound_pos+1 : pound_pos+1+len_val]
        res.append(word)
        len_index = pound_pos+1+len_val # update index by adding previous pound pos 
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
