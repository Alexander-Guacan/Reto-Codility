"""
GitHub: https://github.com/Alexander-Guacan/Reto-Codility.git

Context of problem: https://app.codility.com/programmers/trainings/4/first_unique/
"""

import big_o

def find_unique_value(elements: list[int]) -> int:
    """_summary_ Returns the value that not repeat in elements list and that his index position is the less of all

    Args:
        elements (list[int]): _description_ List of integers numbers between 0 and 1000000000 with a lenght in the range [1 ... 100000]

    Returns:
        int: _description_ First ocurrence of value that don't repeat
    """

    # If elements list is empty
    if len(elements) == 0:
        return -1

    # Dictionary that contains each value of elements list(key), one time, and his repetitions(value)
    dictionary = dict[int, int]()
    # Preview last unique value before to update unique_value
    last_unique = 0
    # Unique value in the elements list
    unique_value = elements[-1]

    # Scrolls through the elements list from end to begin
    for element in range(len(elements) - 1, -1, -1):
        
        # Verifies if each element doesn't exist in dictionary
        if elements[element] not in dictionary:
            # Adds element to dictionary
            dictionary[elements[element]] = 1
            # Saves the preview unique value
            last_unique = unique_value
            # Updates unique value to the new element added to dictionary
            unique_value = elements[element]
        # If element exist yet in dictionary
        else:
            # Increment the repetitions count of element
            dictionary[elements[element]] += 1

            # if the unique value is repeated twice in a row
            if unique_value == elements[element]:
                unique_value = last_unique

    # If last update to unique value has more than one repetion
    if dictionary[unique_value] > 1:
        return -1

    return unique_value

def test(elements : list[int]) -> None:
    """_summary_ Testing the find_unique_value function with specified list of elements

    Args:
        elements (list[int]): _description_
    """
    # Prints the list to test
    print(f"Array of test: {elements}")
    # Prints the returns of function
    print(f"Unique value = {find_unique_value(elements)}")

def main() -> None:
    # Testing find_unique_value function
    test([4, 10, 5, 4, 2, 10]) # Two unique values
    test([1, 4, 3, 3, 1, 2]) # Two unique values
    test([6, 4, 4, 6]) # None unique value

    # Computes algorithmic complexity of find_unique_value function with the worst case specified in the 'codility' exercise
    positive_integer_generator = lambda n : big_o.datagen.integers(100000, 0, 1000000000)
    best, others = big_o.big_o(find_unique_value, positive_integer_generator)

    # Prints algorithmic complexity
    print("Algorithmic complexity")
    print(best)

if __name__ == "__main__":
    main()