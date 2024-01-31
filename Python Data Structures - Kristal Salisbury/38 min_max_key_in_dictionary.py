def min_max_keys(d):
    keys = d.keys()
    return (min(keys), max(keys))


min_max_keys({2: "a", 7: "b", 1: "c", 10: "d", 4: "e"})
min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})