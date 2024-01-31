def intersection(l1, l2):
    set2 = set(l2)
    return [val for val in l1 if val in set2]


intersection([1, 2, 3], [2, 3, 4])
intersection([1, 2, 3], [1, 2, 3, 4])
intersection([1, 2, 3], [3, 4])
intersection([1, 2, 3], [3, 5, 6])