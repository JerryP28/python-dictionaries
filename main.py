

# groceries = {'bananas':5, 'oranges':3}
# print (groceries['bananas'])
# print (groceries.get('bananas'))

# contacts = {
  # 'joe':'123-4567',
  # 'jone': '987-6543'
# }


contacts = {
  'joe':{'phone':'123-4567', 'email':'ea@gamil.com'},
  'jone':{'987-6543'}
}

print(contacts['joe'])


sentence = "I like the name jerry beacuse the name jerry is the best"

word_counts = {
  'I':1,
  'like': 1,
  'the': 3
}

print(word_counts)
word_counts['jerry'] = 2
print(word_counts)


# word_counts['the'] = word_counts['the'] +1

#dict.items()
# print(word_counts.items())

#dict.keys()
# dict.values()
 
# print(word_counts)
# word_counts.pop('the')
# print(word_counts) 

print(word_counts)
word_counts.popitem()
print(word_counts) 