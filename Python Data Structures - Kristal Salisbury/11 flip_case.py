def flip_case(phrase, to_swap):
    to_swap = to_swap.lower()
    out = ""
    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        out += ltr
    return out


flip_case("Aaaahhh", "a")
flip_case("Aaaahhh", "A")
flip_case("Aaaahhh", "h")