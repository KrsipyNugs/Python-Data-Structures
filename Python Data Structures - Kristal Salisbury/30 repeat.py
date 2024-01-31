def repeat(phrase, num):
    if not isinstance(num, int) or num < 0:
        return None
    return phrase * num


repeat("*", 3)
repeat("abc", 2)
repeat("abc", 0)