def max_one(arr):
    max_count = 0
    current_count = 0

    for num in arr:
        if num == 2:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0

    return max_count


if __name__ == "__main__":
    arr = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 2]
    result = max_one(arr)
    print("Max Number of consecutive 2s: ", result)
