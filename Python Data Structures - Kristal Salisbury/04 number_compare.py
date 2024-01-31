def number_compare(a, b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    else:
        return "Numbers are equal"


number_compare(1, 1)
number_compare(-1, 1)
number_compare(1, -2)