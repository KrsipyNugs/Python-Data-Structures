def three_odd_numbers(nums):
    for i in range(len(nums) - 2):
        if (nums[i] + nums[i + 1] + nums[i + 2]) % 2 != 0:
            return True
    return False


three_odd_numbers([1, 2, 3, 4, 5])
three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
three_odd_numbers([5, 2, 1])
three_odd_numbers([1, 2, 3, 3, 2])