def reverse_vowels(s):
    vowels = set("aeiou")
    string = list(s)
    i = 0
    j = len(s) - 1
    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
    return "".join(string)


reverse_vowels("Hello!")
reverse_vowels("Tomatoes")
reverse_vowels("Reverse Vowels In A String")
reverse_vowels("aeiou")
reverse_vowels("why try, shy fly?")