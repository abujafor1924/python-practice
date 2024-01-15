from itertools import combinations


def generate_combinations(elements, r):
    """
    Generate combinations of length 'r' from the given list of 'elements'.

    Parameters:
    - elements: List of elements to generate combinations from.
    - r: Length of each combination.

    Returns:
    - List of tuples representing combinations.
    """
    return list(combinations(elements, r))


# Example usage:
elements = [1, 2, 3, 4]
r = 2
result = generate_combinations(elements, r)
print(result)
