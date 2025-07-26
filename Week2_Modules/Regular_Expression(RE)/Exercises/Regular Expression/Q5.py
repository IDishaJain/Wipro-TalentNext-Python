# Extract all the text portions between the tags

import requests
from bs4 import BeautifulSoup

url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


text_list = [text.strip() for text in soup.stripped_strings]

print(text_list)
