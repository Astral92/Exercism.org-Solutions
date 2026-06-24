"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    letters = ('A', 'B', 'C', 'D')
    while number > 0:
        for letter in letters:
            yield letter
            number -= 1
            if number == 0:
                break
    


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    count = 1
    seat_letters_generator = generate_seat_letters(number)
    while number > 0:
        for _ in range(4):
            yield str(count) + next(seat_letters_generator)
            number -= 1
            if number == 0:
                break
        count += 1
        if count == 13:
            count = 14
            

def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seat_map ={}
    seats = generate_seats(len(passengers))
    for passenger in passengers:
        seat_map[passenger] = next(seats)
    return seat_map


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for seat_number in seat_numbers:
        code = seat_number + flight_id
        yield code + '0'* (12 - len(code))
