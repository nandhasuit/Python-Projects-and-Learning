'''Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

Note, that during capitalization all the letters except the first one remains unchanged.

Input
A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. The length of the word will not exceed 103.'''


word = input('Enter the word: ')
m = ""
k = word[0].upper()
t = word.replace(word[0],k)
print(t)
