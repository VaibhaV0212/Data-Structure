def InsertionSort(list1):
    for i in range(1, len(list1)):                          # 1, 2, 3, 4
        current_element = list1[i]                          # current_element = 4
        pos = i                                             # pos = 1
        while current_element < list1[pos-1] and pos > 0:   # 4 < [1-1] --> 4 < 0th element that is 2,
                                                            # so condition becomes false
            list1[pos] = list1[pos-1]
            pos = pos-1
        list1[pos] = current_element                        # 4 will be inserted here


list1 = [2, 4, 3, 5, 1]
InsertionSort(list1)
print(list1)

'''
    for i in range(1, len(list1)):                          # index will be 2 now
        current_element = list1[i]                          # current_element = 3
        pos = i                                             # pos = 2
        while current_element < list1[pos-1] and pos > 0:   # 3 < 4 & pos > 0, while loop will be executed
            list1[pos] = list1[pos-1]                       # it will move 4 towards the right side
            pos = pos-1                                     # now pos will be decremented and it will check 3 < 2 &
                                                            # condition will become false
        list1[pos] = current_element                        # list[pos] = 3

'''