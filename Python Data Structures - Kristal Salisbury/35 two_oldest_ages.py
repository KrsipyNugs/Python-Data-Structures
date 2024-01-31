def two_oldest_ages(ages):
    uniq_ages = set(ages)
    oldest = sorted(uniq_ages)[-2:]
    return tuple(oldest)


two_oldest_ages([1, 2, 10, 8])
two_oldest_ages([6, 1, 9, 10, 4])
two_oldest_ages([1, 5, 5, 2])