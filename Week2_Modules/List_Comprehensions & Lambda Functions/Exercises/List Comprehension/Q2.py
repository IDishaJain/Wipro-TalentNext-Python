# Make a dictionary of the 26 English alphabets mapping each to its corresponding integer

alphabet_dict = {chr(i+97): i+1 for i in range(26)}
print(alphabet_dict)
