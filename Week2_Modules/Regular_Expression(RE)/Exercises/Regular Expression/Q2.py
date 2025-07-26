# Extract the user id, domain name and suffix from the following email addresses.

import re

emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

pattern = r'([\w\d]+)@([\w\d]+)\.([a-z]+)'
matches = re.findall(pattern, emails)

for match in matches:
    print(f"User: {match[0]}, Domain: {match[1]}, Suffix: {match[2]}")
