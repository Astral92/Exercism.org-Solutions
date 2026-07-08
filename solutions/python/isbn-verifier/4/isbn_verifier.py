"""Functions to determine validate an isbn."""

def is_valid(isbn: str):

    processed_isbn =[]
    length = 10
    isbn_sum = 0
    
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
            isbn_sum += digit * length
            length -= 1
    return isbn_sum % 11 == 0