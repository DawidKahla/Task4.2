def is_palindrom(word):
  for i in range(0,len(word)//1):
    if word[i] != word[-i-1]:
      return False
  return True

print(is_palindrom('kajak'))