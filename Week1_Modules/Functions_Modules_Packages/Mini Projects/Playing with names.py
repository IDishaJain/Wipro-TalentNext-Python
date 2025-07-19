# Create a python module with the following functions:
# ispalindrome(name) - Checks if a name reads the same forwards and backwards (case-insensitive)
# count_the_vowels(name) - Counts the number of vowels (a, e, i, o, u) in the name
# frequency_of_letters(name) - Returns a dictionary with the frequency of each letter
def ispalindrome(name):
    """Check if a name is a palindrome (reads same forwards and backwards)"""
    name_clean = name.lower().replace(" ", "")
    return name_clean == name_clean[::-1]

def count_the_vowels(name):
    """Count the number of vowels in a name"""
    vowels = "aeiou"
    count = 0
    for char in name.lower():
        if char in vowels:
            count += 1
    return count

def frequency_of_letters(name):
    """Count frequency of each letter in the name"""
    freq = {}
    for char in name.lower():
        if char.isalpha():  
            freq[char] = freq.get(char, 0) + 1
    return freq

if __name__ == "__main__":
    test_name = "bob"
    
    print(f"Sample input: {test_name}")
    print()
    
    if ispalindrome(test_name):
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")

    vowel_count = count_the_vowels(test_name)
    print(f"No of vowels: {vowel_count}")
    
    freq = frequency_of_letters(test_name)
    freq_str = ", ".join([f"{letter}-{count}" for letter, count in sorted(freq.items())])
    print(f"Frequency of letters: {freq_str}")