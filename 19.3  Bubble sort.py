'''
Bubble sort is the easiest technique to sort the list.
In this we normally compare the first 2 no.s and if 1st is greater than the 2nd one, we swap them and this approach is
done for the whole list.

for i in range(len(nums)-1, 0, -1) : we are taking the outer loop from 5 to 0, so for 5 we are taking the length of the
                                     list and subtracting 1 from it so that the largest element could come in the last &
                                     since we are moving from 5 to 0 so that's why -1 because we going in reverse order
"temp" is a temporary variable.
We made a function named 'sort' and passed "nums" that is the list in it as arguments.
'''

def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [2, 3, 6, 7, 8, 1]
sort(nums)
print(nums)

'''
Demerit - In each iteration we do multiple swapping and thus requires a lot of memory and computer power.
'''

def bubble(num):
    for i in range(len(num)-1, 0, -1):
        for j in range(i):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp


num = [2, 8, 4, 9, 1, 0]
bubble(num)
print(num)