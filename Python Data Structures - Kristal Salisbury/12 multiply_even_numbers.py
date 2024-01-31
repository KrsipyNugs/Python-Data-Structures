def multiply_even_numbers(nums):
    product = 1
    for num in nums:
        if num % 2 == 0:
            product = product * num
    return product


multiply_even_numbers([2, 3, 4, 5, 6])
multiply_even_numbers([3, 4, 5])
multiply_even_numbers([1, 3, 5])