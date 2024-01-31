def is_odd_string(word):
    DIFF = ord("a") - 1
    total = sum((ord(c) - DIFF) for c in word.lower())
    return total % 2 == 1


is_odd_string("a")
is_odd_string("A")
is_odd_string("aaaa")
is_odd_string("AAaa")
is_odd_string("amazing")