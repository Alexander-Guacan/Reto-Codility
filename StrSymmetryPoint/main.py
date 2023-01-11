"""
GitHub: https://github.com/Alexander-Guacan/Reto-Codility.git

Context of problem: https://app.codility.com/programmers/trainings/4/str_symmetry_point/
"""

import big_o

def symmetry_index(string: str) -> int:
    """_summary_ Returns the index (counting from 0) of a character such that the part of the string to the left of that character is a reversal of the part of the string to its right. The function returns −1 if no such index exists.

    Args:
        string (str): _description_ Any characters list

    Returns:
        int: _description_ Symmetry index in the string
    """
    # If string is empty or have pair lenght
    if len(string) == 0 or len(string) % 2 == 0:
        return -1

    # If have one character
    if len(string) == 1:
        return 0

    # Asummes the symmetry axis are in the center of the string
    symmetry_axis = int(len(string) / 2)
    # Iterators that verifies symmetry to the left and the right of the center of the string
    left = symmetry_axis - 1
    right = symmetry_axis + 1

    # Iterates until first position on string
    while left >= 0:
        # If not exist symmetry
        if string[left] != string[right]:
            return -1
        
        # Moves a back and forward position respectively
        left -= 1
        right += 1

    return symmetry_axis

def test(string : str) -> None:
    # Prints the parameter to test
    print(f"String of test: {string}")
    # Prints the returns of function
    print(f"Symmetry index = {symmetry_index(string)}")

def main() -> None:
    # Testing symmetry_index function
    test("racecar") # Exist symmetry index
    test("mobabacer") # Not exist symmetry index
    test("x") # Zero is the symmetry index

    # Computes algorithmic complexity of symmetry_index function with the worst case specified in the 'codility' exercise
    string_ascii_lowercase_generator = lambda n : big_o.datagen.strings(2000000, big_o.datagen.string.ascii_lowercase)
    best, others = big_o.big_o(symmetry_index, string_ascii_lowercase_generator, n_measures=10)

    # Prints algorithmic complexity
    print("Algorithmic complexity")
    print(best)

if __name__ == "__main__":
    main()