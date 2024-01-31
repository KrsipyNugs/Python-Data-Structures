def find_the_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)


find_the_duplicate([1, 2, 1, 4, 3, 12])
find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
find_the_duplicate([2, 1, 3, 4]) is None