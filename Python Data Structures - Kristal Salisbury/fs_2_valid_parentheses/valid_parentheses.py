def valid_parentheses(parens):
    count = 0
    for p in parens:
        if p == '(':
            count += 1
        elif p == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


valid_parentheses("()")
valid_parentheses("()()")
valid_parentheses("(()())")
valid_parentheses(")()")
valid_parentheses("())")
valid_parentheses("((())")
valid_parentheses(")()(")