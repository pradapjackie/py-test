names=['john','sample','pradap','arun','news','west','east']

for newnames in names :
    print(f'current person :{newnames}')


print('----------------------------------------------------------')

for newnames in names:
    if newnames =='arun':
        break
    print(f'current person :{newnames}')

print('----------------------------------------------------------')

for newnames1 in names:
    if newnames1 == 'arun':
        continue
    print(f'current person :{newnames1}')

print('----------------------------------------------------------')
for i in range (len(names)):
    print(names[i])


print('----------------------------------------------------------')
for i in range(10,55):
    print(f'Prining value is {i}')


print('----------------------------------------------------------')
count=0
while count <=20:
    print(f'print value of count {count}')
    count+=1