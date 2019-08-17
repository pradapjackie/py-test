fruits=('apples','grapes','fig','pineapple','orange','mangoes','blueberry')
fruits1=tuple(('apples','grapes','fig','pineapple','orange','mangoes','blueberry'))
fruits2=('apples',)

print(fruits)
print(fruits1)
print(fruits[1])
#fruits[0]='guva'
del  fruits2

#print(fruits2,type(fruits2))

fruits_set={'apples','grapes','fig','pineapple','orange','mangoes','blueberry'}
print('apples' in fruits_set)
fruits_set.add('watermelon')
print(fruits_set)
fruits_set.remove('grapes')
print(fruits_set)
fruits_set.clear();
print(fruits_set)

