#Jack Robey
#9/6/17
#nameAge.py - prints how many characters are in each name entered and how old the person will be next year based on their entered age

name = input('Enter your first and last name: ')
age = int(input('Enter your age: '))
firstName, lastName = name.split()
charactersFirst = len(firstName)
print('There are', charactersFirst, 'characters in your first name')
chracterSecond = len(lastName)
print('There are', chracterSecond, 'characters in your last name')
nextAge = age + 1
print('Next year you will be', nextAge, 'years old')

