VOWELS = set("aeiou")


def vowel_count(phrase):
    phrase = phrase.lower()
    counter = {}
    for ltr in phrase:
        if ltr in VOWELS:
            counter[ltr] = counter.get(ltr, 0) + 1
    return counter


vowel_count("rithm school")
vowel_count("HOW ARE YOU? i am great!")