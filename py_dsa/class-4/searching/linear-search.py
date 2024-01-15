def linear_search(arr, target):
    """
    Perform linear search on a list to find the target element.

    Parameters:
    - arr: List in which the search is performed.
    - target: Element to be searched.

    Returns:
    - If target is found, return the index of the target in the list.
    - If target is not found, return -1.
    """
    n=len(arr)
    for i in range(0,n):
        if arr[i] == target:
            return i  # Target found, return the index
    return -1  # Target not found in the list

# Example usage:
my_list = [2, 5, 8, 12, 16, 23, 38, 42, 51]

target_element = 23
result = linear_search(my_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")
