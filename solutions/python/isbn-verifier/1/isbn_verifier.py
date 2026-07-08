def is_valid(isbn: str):

    processed_isbn =[]
    length = 10
    sum = 0
    
    for char in isbn:
        if char.isdigit():
            processed_isbn.append(int(char))
    
        elif char.isalpha() and not isbn.endswith(char):
            return False
    
        elif char.isalpha():
            if char == 'X':
                processed_isbn.append(10)
            else:
                return False
    
    
    if len(processed_isbn) != 10:
        return False
    
    while length >= 1:
        for digit in processed_isbn:
            sum += digit * length
            length -= 1
    return sum % 11 == 0

