def sort(nums):
    for i in range(5):
        minimun_position = i        # since the 'i' will be 0th element
        for j in range(i, 6):       # it will go till 5
            if nums[j] < nums[minimun_position]:
                minimun_position = j

        temp = nums[i]
        nums[i] = nums[minimun_position]
        nums[minimun_position] = temp
       # print(nums)



nums = [9, 3, 6, 7, 8, 1]
sort(nums)
print(nums)
print()