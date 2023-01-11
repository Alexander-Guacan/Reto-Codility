"""
GitHub: https://github.com/Alexander-Guacan/Reto-Codility.git

Context of problem: https://app.codility.com/programmers/trainings/4/tree_height/
"""

import big_o

def height_tree(tree: list) -> int:
    """_summary_ Returns the number of nodes to traverse to the lowest tree node in a tree. If tree is empty the height is -1. If tree has one node the height is zero.

    Args:
        tree (list): _description_ Tree with the next structure [X, L, R]. X: value of node, L: subtree left, R: subtree right. Empty tree = [None]

    Returns:
        int: _description_ Height of tree
    """
    # Empty tree
    if tree is None or len(tree) == 1:
        return -1

    # Computes the tree height left
    left_height = height_tree(tree[1])
    # Computes the tree height right
    right_height = height_tree(tree[2])

    # Selects the heighest height and returns his value incremented in one
    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1

def test(tree : list) -> None:
    # Prints the parameter to test
    print(f"Tree of test: {tree}")
    # Prints the returns of function
    print(f"Height = {height_tree(tree)}")

def main() -> None:
    # Testing height_tree function
    test([16, [13, None, None], [20, [18, None, None], None]]) # Tree with height = 2
    test([7, [5, None, None], [9, None, None]]) # Tree with height = 1
    test([None]) # Empty tree
    test([25, [23, [20, [19, [7, None, None], None], [22, None, None]], [24, None, None]], [34, [30, [26, None, None], [33, [32, None, None], None]], [38, None, None]]]) # Complex tree

    # Computes algorithmic complexity of height_tree function with the worst case specified in the 'codility' exercise
    tree_sample = lambda n : [25, [23, [20, [19, [7, None, None], None], [22, None, None]], [24, None, None]], [34, [30, [26, None, None], [33, [32, None, None], None]], [38, None, None]]]
    best, others = big_o.big_o(height_tree, tree_sample)

    # Prints algorithmic complexity
    print("Algorithmic complexity")
    print(best)

if __name__ == "__main__":
    main()