def sum_of_multiples(limit, multiples):
    unique_multiples = set()
    for num in multiples:
        multiple = 1
        while num * multiple < limit and num != 0:
            unique_multiples.add(num*multiple)
            multiple += 1
    return sum(unique_multiples)
