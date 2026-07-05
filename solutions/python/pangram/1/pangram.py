def is_pangram(sentence):
    points = 0
    letters = "abcdefghijklmnopqrstuvwxyz"
    for letter in set(sentence.lower()):
        if letter in letters:
           points += 1 

    return points == 26
