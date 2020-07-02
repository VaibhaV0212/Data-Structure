'''
1. Traversing a node - for element in list: print(element)
2. Appending - append(element)
3. Inserting - insert(position, element)
4. Removing - remove(element) OR pop(element) and if not found ValueError will be raised
5. Replacing - first remove() and than insert()
6. Searching - index(element) and if not found ValueError will be raised
7. Size - len(list)
'''
import sys
LL = []

LL.append('Mera')
LL.append('Desh')
LL.append('Mahan')

print('The existing list = ', LL)

choice = 0
while choice < 5:
    print('LINKED LIST OPERATION')
    print('1 - Add Element')
    print('2 - Remove Element')
    print('3 - Replace Element')
    print('4 - Search Element')
    print('5 - Exit')

    choice = int(input('Enter Choice = '))

    if choice == 1:
        element = input('Enter element = ')
        position = int(input('Enter position to enter = '))
        LL.insert(position, element)

    elif choice == 2:
        try:
            element = input('Enter element = ')
            LL.remove(element)
        except ValueError as e:
            print('Element not found,sorry!')

    elif choice == 3:
        element = input('Enter new Element = ')
        position = int(input('Enter at which position ='))
        LL.pop(position)
        LL.insert(position, element)

    elif choice == 4:
        element = input('Enter element to be searched = ')
        try:
            position = LL.index(element)
            print('Found at position - ', position)
        except Exception as e:
            print('Not Found')
    else:
        sys.exit()
    print('List = ', LL)
print()
