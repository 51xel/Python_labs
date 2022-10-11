text = "Get the skin 5th character starting from the beginning and up to the 21st character (21st character is not included)."
if len(text) >= 21:
    print("Result = " + text[4:21:5])
else:
    print("Sentence has less than 21 characters")
