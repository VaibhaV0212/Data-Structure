import sys
LL = []

LL.append('Mera')
LL.append('Desh')
LL.append('great')

print('The current list is ', LL)

choice = 0
while choice < 5:
    print('1. Add Element')
    print('2. Remove')
    print('3. Replace')
    print('4. Search')
    print('5. Exit')
    choice = int(input('Enter choice = '))

    if choice == 1:
        element = input('Enter Element = ')
        position = int(input('At which location '))
        LL.insert(position, element)
    if choice == 2:
        element = input('Enter element to be removed = ')
        try:
            LL.remove(element)
        except ValueError as e:
            print('Not found')
    if choice == 3:
        element = input('Enter element to be replaced = ')
        position = int(input('At which position = '))
        LL.pop(position)
        LL.insert(position, element)
    if choice == 4:
        element = input('Enter element to be searched = ')
        try:
            position = LL.index(element)
            print('Found at position - ', position)
        except Exception as e:
            print('Not Found')



    if choice == 5:
        sys.exit('bye')
    print('The new list is = ', LL)
print()
