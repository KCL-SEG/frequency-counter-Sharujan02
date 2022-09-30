"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    #adds the keys to the disctionary
    for i in range(len(items)):
        if frequencies.get(items[i]) is None:
            frequencies[str(items[i])] = 0

    #adds the values to the dictionary
    for i in range (len(items)):
        frequencies.update({str(items[i]): frequencies.get(str(items[i])) + 1})

    return frequencies
