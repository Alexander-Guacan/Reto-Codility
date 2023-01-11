"""
GitHub: https://github.com/Alexander-Guacan/Reto-Codility.git

Context of problem: https://app.codility.com/programmers/trainings/4/disappearing_pairs/
"""

import big_o
import random

def dissapearing_pairs(string: str) -> str:
    """_summary_ Returns a new string where has benn to delete the consecutively pairs of letters. Assume the string have only 'A', 'B' and 'C' characters.

    Args:
        string (str): _description_ String that have only 'A', 'B' and 'C' characters in any order.

    Returns:
        str: _description_ Strings without consecutively pairs
    """
    # Iterator of string
    i = 1

    # Scrolls through string from 1 position
    while i >= 1 and i < len(string):
        # Verify consecutively pairs
        if string[i] == string[i - 1]:
            # Deletes equals consecutively characters
            string = string[:i-1] + string[i+1:]
            # Backs one position
            i -= 1
        else:
            # Forwards one position
            i += 1

    return string

def test(string : str) -> None:
    # Prints the parameter to test
    print(f"String of test: {string}")
    # Prints the returns of function
    print(f"String without pairs = {dissapearing_pairs(string)}")

def generate_random_strings(lenght: int, chars: str) -> str:
    """_summary_ Returns a string with N characters choose randomically of 'chars'

    Args:
        lenght (int): _description_ Number of characters in random string
        chars (str): _description_ Characters that will contain random string

    Returns:
        str: _description_
    """
    # Random string
    random_string = str()

    # Generate a random string with 'lenght' characters
    for i in range(lenght):
        # Select a random character of chars string
        random_string += chars[random.randint(0, len(chars) - 1)]

    return random_string

def main() -> None:
    # Testing dissapearing_pairs function
    test("ACCBBAC") # String result = C
    test("ABCBBCBA") # String result = ""
    test("BABA") # String result = BABA

    # Computes algorithmic complexity of dissapearing_pairs function with the worst case specified in the 'codility' exercise
    string_sample = lambda n : generate_random_strings(50000, "ABC")
    best, others = big_o.big_o(dissapearing_pairs, string_sample)

    # Prints algorithmic complexity
    print("Algorithmic complexity")
    print(best)

if __name__ == "__main__":
    main()