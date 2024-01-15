def generate_permutations(elements, current=[]):
    if not elements:
        # If there are no more elements to permute, yield the current permutation
        yield tuple(current)
    else:
        for i in range(len(elements)):
            # Choose an element to add to the current permutation
            new_element = elements[i]

            # Exclude the chosen element from the remaining elements
            remaining_elements = elements[:i] + elements[i + 1:]

            # Recursively generate permutations with the chosen element
            yield from generate_permutations(remaining_elements, current + [new_element])


# Example usage
elements = [1, 2, 3]
perms_generator = generate_permutations(elements)

# Print the generated permutations
for perm in perms_generator:
    print(perm)



# =====================================================================


# from itertools import permutations
#
# # Define a list of elements
# elements = [1, 2, 3]
#
# # Generate permutations
# perms = permutations(elements)
#
# # Convert the permutations to a list
# perms_list = list(perms)
#
# # Print the generated permutations
# print(perms_list)
