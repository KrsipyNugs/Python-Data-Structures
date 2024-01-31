def sum_floats(nums):
    return sum([num for num in nums if isinstance(num, float)])


sum_floats([1.5, 2.4, "awesome", [], 1])
sum_floats([1, 2, 3])