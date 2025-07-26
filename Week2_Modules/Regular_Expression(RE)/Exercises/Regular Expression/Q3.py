# Split the following irregular sentence into proper words

sentence = """A, very    very; irregular_sentence"""
import re
clean_sentence = re.sub(r'[^\w\s]', ' ', sentence)
clean_sentence = re.sub(r'\s+', ' ', clean_sentence).strip()

print(clean_sentence)
