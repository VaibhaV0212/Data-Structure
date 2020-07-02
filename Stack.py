'''
Stack works on LIFO (Last in First out)
1. Push = list.append(element)
2. Pop = list.pop()  , will remove the topmost element
3. Peep = Returning the topmost element without deleting it
4. Search = list.index(element)
5. Empty stack or not = 'return list == []'
'''

class Stack:
    def __init__(self):
        self.list = []
    def isempty(self):
        return self.list = []
    def push(self, element):
        self.list.append(element)
    def pop(self):
        if self.isempty():
            return -1
        else:
            return self.list.pop()
    def peep(self):
        n = len(self.list)
        return self.list[n-1]
    def search(self, element):
        if self.isempty():
            return -1
        else:
            try:
                n = self.list.index(element)
                return len(self.list)-n
            except Exception as e:
                return -2
    def display(self):
        return self.list
