# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
letters = set(char)
new_list = []

for word in word_list:
 if letters & set(word):
  print (word)
  new_list.append(word)
print ("newList =",new_list)
