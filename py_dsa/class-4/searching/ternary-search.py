def ternary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        # Divide the array into three parts
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Check if the target is present at mid1 or mid2
        if arr[mid1] == target:
            return mid1
        elif arr[mid2] == target:
            return mid2

        # If the target is in the left third
        elif target < arr[mid1]:
            right = mid1 - 1
        # If the target is in the right third
        elif target > arr[mid2]:
            left = mid2 + 1
        # If the target is in the middle third
        else:
            left = mid1 + 1
            right = mid2 - 1

    # If the target is not present in the array
    return -1

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 7

result = ternary_search(sorted_array, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}")
else:
    print(f"Element {target_element} not found in the array")
