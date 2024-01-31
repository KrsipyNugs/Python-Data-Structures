def list_manipulation(lst, command, location, value=None):
    if command == "remove":
        if location == "end":
            return lst.pop()
        elif location == "beginning":
            return lst.pop(0)
    elif command == "add":
        if location == "beginning":
            lst.insert(0, value)
            return lst
        elif location == "end":
            lst.append(value)
            return lst


lst = [1, 2, 3]
list_manipulation(lst, 'remove', 'end')
list_manipulation(lst, 'remove', 'beginning')
lst

lst = [1, 2, 3]
list_manipulation(lst, 'add', 'beginning', 20)
list_manipulation(lst, 'add', 'end', 30)
lst

list_manipulation(lst, 'foo', 'end') is None
list_manipulation(lst, 'add', 'dunno') is None