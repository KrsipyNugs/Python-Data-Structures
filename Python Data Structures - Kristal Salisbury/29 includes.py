def includes(collection, sought, start=None):
    if isinstance(collection, dict):
        return sought in collection.values()
    if start is None or isinstance(collection, set):
        return sought in collection
    return sought in collection[start:]

    
includes([1, 2, 3], 1)
includes([1, 2, 3], 1, 2)
includes("hello", "o")
includes(("Elmo", 5, "red"), "red", 1)
includes({1, 2, 3}, 1)
includes({1, 2, 3}, 1, 3)
includes({"apple": "red", "berry": "blue"}, "blue")