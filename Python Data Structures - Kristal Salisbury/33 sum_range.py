def sum_range(nums, start=0, end=None):
    if end is None:
        end = len(nums)
    return sum(nums[start:end + 1])


nums = [1, 2, 3, 4]
sum_range(nums)
sum_range(nums, 1)
sum_range(nums, end=2)
sum_range(nums, 1, 3)
sum_range(nums, 1, 99)