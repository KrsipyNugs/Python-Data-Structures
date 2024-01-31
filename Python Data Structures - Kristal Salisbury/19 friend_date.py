def friend_date(a, b):
    if set(a[2]) & set(b[2]):
        return True
    else:
        return False


elmo = ("Elmo", 5, ["hugging", "being nice"])
sauron = ("Sauron", 5000, ["killing hobbits", "chess"])
gandalf = ("Gandalf", 10000, ["waving wands", "chess"])

friend_date(elmo, sauron)
friend_date(sauron, gandalf)