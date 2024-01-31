def two_list_dictionary(keys, values):
    out = {}
    for idx, val in enumerate(keys):
        out[val] = values[idx] if idx < len(values) else None
    return out

    
two_list_dictionary(["x", "y", "z"], [9, 8, 7])
two_list_dictionary(["a", "b", "c", "d"], [1, 2, 3])
two_list_dictionary(["a", "b", "c"], [1, 2, 3, 4])