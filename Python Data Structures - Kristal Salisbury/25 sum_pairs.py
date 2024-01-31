def sum_pairs(nums, goal):
    already_visited = set()
    for i in nums:
        difference = goal - i
        if difference in already_visited:
            return (difference, i)
        already_visited.add(i)
    return ()


sum_pairs([1, 2, 2, 10], 4)
sum_pairs([4, 2, 10, 5, 1], 6)
sum_pairs([5, 1, 4, 8, 3, 2], 7)
sum_pairs([11, 20, 4, 2, 1, 5], 100)