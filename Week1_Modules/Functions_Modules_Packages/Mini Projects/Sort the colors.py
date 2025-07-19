# Project 1:
# Write a Python function that accepts a hyphen-separated sequence of colors as input
# and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
def sort_colors(color_sequence):
    colors = color_sequence.split('-')
    colors.sort()
    return '-'.join(colors)

input1 = "green-red-yellow-black-white"
output1 = sort_colors(input1)
print("Sample Output 1:", output1)  

input2 = "PINK-BLUE-TAN-PURPLE"
output2 = sort_colors(input2)
print("Sample Output 2:", output2) 

