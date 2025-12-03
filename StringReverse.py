word = str(input("Please enter a word: ")) 

re_word =""

i =len(word) -1

while i >= 0:
    re_word += word[i]
    i -= 1

print(f" reversed word is {re_word}")