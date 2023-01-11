"""
GitHub: https://github.com/Alexander-Guacan/Reto-Codility.git

Context of problem: https://app.codility.com/programmers/trainings/4/array_inversion_count/
"""

import big_o
import sys

def array_invertion_count(array: list[int]) -> int:
    """_summary_ Returns the amount of valid invertions. An invertion valid is when P < Q and array[Q] < array[P]

    Args:
        array (list[int]): _description_ Any integers list

    Returns:
        int: _description_ Invertions count
    """
    # Invertions count
    invertions = 0

    # Compares each P position with all next elements in the list (Q)
    for P in range(len(array) - 1):
        # All next elements to P
        for Q in range(P + 1, len(array)):
            # Valid invertion
            if array[Q] < array[P]:
                invertions += 1

    return invertions

def test(array : list[int]) -> None:
    # Prints the parameter to test
    print(f"Array of test: {array}")
    # Prints the returns of function
    print(f"Invertions = {array_invertion_count(array)}")

def main() -> None:
    # Testing array_invertion_count function
    test([-1, 6, 3, 4, 7, 4]) # Array with 4 invertions
    test([1, 2, 3, 4]) # Array with 0 invertions
    test([]) # Empty array

    # Computes algorithmic complexity of array_invertion_count function with the worst case specified in the 'codility' exercise
    tree_sample = lambda n : big_o.datagen.integers(1000, -(sys.maxsize - 1), sys.maxsize)
    best, others = big_o.big_o(array_invertion_count, tree_sample)

    # Prints algorithmic complexity
    print("Algorithmic complexity")
    print(best)

if __name__ == "__main__":
    main()