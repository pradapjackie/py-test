person ={
    'first_name':'John',
'second_name':'peters',
'age':30,
'height':6.5}

print(person)
print(person['first_name'])
print(person.get('second_name'))

person['person']='5555-55-555'
print(person)

print(person.keys())
print(person.items())

person2=person.copy()

print(person2)
person2['city']='Boston'

print(person2)
del(person2['city'])
print(person2)

person2.pop('second_name')
print(person2)
person2.clear()
print(person2)

people =[
    {'first_name':'Pradap','last_name':'Pandiyan','age':30},
    {'first_name':'Jackie','last_name':'Pandiyan','age':20}
]

print(people)