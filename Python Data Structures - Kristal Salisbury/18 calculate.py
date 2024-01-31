def calculate(operation, a, b, make_int=False, message='The result is'):
    if operation == "add":
        res = a + b
    elif operation == "subtract":
        res = a - b
    elif operation == "multiply":
        res = a * b
    elif operation == "divide":
        res = a / b
    else:
        return
    if make_int:
        res = int(res)
    return f"{message} {res}"


calculate("add", 2.5, 4)
calculate("subtract", 4, 1.5, make_int=True)
calculate("multiply", 1.5, 2)
calculate("divide", 10, 4, message="I got")
calculate("foo", 2, 3)