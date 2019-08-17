#String Formatting
name ='Pradap'
age=35
print(name+' and my age is ' +str(age))
print('My name is {name} and Iam age {age}'.format(name=name,age=age))

#F-Strings
print(f'My name is {name} and age is {age}')

s='hello world'
print(s)
print(s.capitalize())
print(s.upper())
print(s.swapcase())
print(len(s))
print(s.replace('hello','First'))
print(s.count('w'))
print(s.split())