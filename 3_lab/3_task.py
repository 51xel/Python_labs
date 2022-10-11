text = "Sentenceeeee is given. Write a program that determines and displays whether the statement that its longest word has more than 10 characters is true."
max = 0
for i in text.split(' '):
    if len(i) > max:
        max = len(i)

if max > 10:
    print("The sentence contains a word longer than 10 characters")
else:
    print("There is no word more than 10 characters in the sentence")
