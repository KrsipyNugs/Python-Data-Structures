def truncate(phrase, n):
    if n < 3:
        return "Truncation must be at least 3 characters."
    if n > len(phrase) + 2:
        return phrase
    return phrase[:n - 3] + "..."


truncate("Hello World", 6)
truncate("Problem solving is the best!", 10)
truncate("Yo", 100)

truncate("Cool", 1)
truncate("Woah", 4)
truncate("woah", 3)