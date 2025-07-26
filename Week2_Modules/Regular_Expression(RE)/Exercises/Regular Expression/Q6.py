# Given below list of words, identify the words that begin and end with the same character

words = [
    "civic",
    "trust",
    "widows",
    "maximum",
    "museums",
    "aa",
    "as"
]

result = [word for word in words if word[0] == word[-1]]
print(result)
