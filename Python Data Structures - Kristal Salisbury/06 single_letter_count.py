def single_letter_count(word, letter):
    return word.lower().count(letter.lower())


single_letter_count("Hello World!", "h")
single_letter_count("Hello World!", "z")
single_letter_count("Hello World!", "l")