# Clean up the following tweet so that it contains only the user’s message

import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
tweet = re.sub(r'RT\s+@\w+:?', '', tweet)                
tweet = re.sub(r'http\S+', '', tweet)                     
tweet = re.sub(r'@\w+', '', tweet)              
tweet = re.sub(r'#\w+', '', tweet)           
tweet = re.sub(r'[^\w\s]', '', tweet)                     
tweet = re.sub(r'\s+', ' ', tweet).strip()               
print(tweet)
