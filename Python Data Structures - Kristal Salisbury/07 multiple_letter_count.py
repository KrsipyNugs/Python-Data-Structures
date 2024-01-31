def multiple_letter_count(phrase):
    counter = {}
    for ltr in phrase:
        counter[ltr] = counter.get(ltr, 0) + 1
    return counter


multiple_letter_count("yay")
multiple_letter_count("Yay")