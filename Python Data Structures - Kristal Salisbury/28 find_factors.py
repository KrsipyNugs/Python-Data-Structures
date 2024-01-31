def find_factors(num):
    n_list = [n for n in range (1, num // 2 + 1) if num % n == 0]
    n_list.append(num)
    return n_list


find_factors(10)
find_factors(11)
find_factors(111)
find_factors(321421)