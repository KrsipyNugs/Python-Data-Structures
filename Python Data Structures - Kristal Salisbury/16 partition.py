def partition(lst, fn):
    true_list = []
    false_list = []
    for val in lst:
        if fn(val):
            true_list.append(val)
        else:
            false_list.append(val)
    return [true_list, false_list]


partition([1, 2, 3, 4], is_even)
partition(["hi", None, 6, "bye"], is_string)