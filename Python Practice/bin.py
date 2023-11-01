def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid  # Found the target; return its index
        elif arr[mid] < target:
            left = mid + 1  # Adjust the search range to the right half
        else:
            right = mid - 1  # Adjust the search range to the left half

    return -1  # Target not found in the list

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = binary_search(my_list, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
