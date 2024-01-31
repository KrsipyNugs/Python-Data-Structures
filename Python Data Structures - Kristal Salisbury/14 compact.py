def compact(lst):
    return [val for val in lst if val]


compact([0, 1, 2, "", [], False, (), None, "All done"])