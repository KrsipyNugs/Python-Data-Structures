def is_palindrome(phrase):
    normalized = phrase.lower().replace(' ', '')
    return normalized == normalized[::-1]


is_palindrome("tacocat")
is_palindrome("noon")
is_palindrome("robert")
is_palindrome("taco cat")
is_palindrome("Noon")