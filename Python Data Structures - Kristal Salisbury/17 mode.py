def mode(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    max_value = max(counts.values())
    for (num, freq) in counts.items():
        if freq == max_value:
            return num
        

mode([1, 2, 1])
mode([2, 2, 3, 3, 2])