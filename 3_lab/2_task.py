import re

word = "beginning"
customer_word = input("Enter your word: ")

if re.search("["+word+"]+", customer_word).group(0) == customer_word:
    print("All letters in (" + word + ") are in this word (" + customer_word +")")
else:
    print("Not all letters were found")
