def find_greater_numbers(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                count += 1
    return count


find_greater_numbers([1, 2, 3])
find_greater_numbers([6, 1, 2, 7])
find_greater_numbers([5, 4, 3, 2, 1])
find_greater_numbers([])