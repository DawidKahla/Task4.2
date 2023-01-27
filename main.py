# input: string
# output: True if argument is palindrom or False if argument is not palindrom 
def is_palindrom(word: str):
    # assumption: 1 letter word is palindrom
    # handling expection of more than one word, empty string and wrong types
    if not word.isalpha():
        raise Exception("Argument of is_palindrom must be single word, type: str.")
    word = word.lower()
    for i in range(0,len(word)//1):
        if word[i] != word[-i-1]:
            return False
    return True

word = input('Wpisz wyraz, aby sprawdzić, czy jest palindromem: ') 
print(f"Wyraz {word}{'' if is_palindrom(word) else ' nie'} jest palindromem.")