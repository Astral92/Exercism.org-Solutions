"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

cards_values = { 'J' : 10, 'Q' : 10, 'K': 10, 'A': 1, '2' : 2, '3': 3, '4' : 4, '5' : 5, '6': 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10}

def value_of_card(card, ace_as_11 = False):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int:  The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """
    if card == 'A':
        return 11 if ace_as_11 else 1

    return cards_values[card]


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting Tuple contains both cards if they are of equal value.
    """

    card1_value = value_of_card(card_one)
    card2_value = value_of_card(card_two)
    if card1_value > card2_value:
        return card_one
    if card1_value < card2_value:
        return card_two

    return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """

    max_ace_11 = 10

    total = value_of_card(card_one, ace_as_11= True) + value_of_card(card_two, ace_as_11= True)

    return 11 if total <= max_ace_11 else 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """

    return value_of_card(card_one, ace_as_11= True) + value_of_card(card_two, ace_as_11= True) == 21


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    min_double_down = 9
    max_double_down = 11
    total = value_of_card(card_one) + value_of_card(card_two)
    return max_double_down >= total >= min_double_down
