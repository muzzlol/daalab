def find_min_max(arr, low, high):
    # Base case: If the array has only one element
    if low == high:
        return arr[low], arr[low]

    # Base case: If the array has two elements
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide the array into two halves
    mid = (low + high) // 2

    # Recursively find the minimum and maximum in the left half
    min_left, max_left = find_min_max(arr, low, mid)

    # Recursively find the minimum and maximum in the right half
    min_right, max_right = find_min_max(arr, mid + 1, high)

    # Combine the results to find the overall minimum and maximum
    min_val = min(min_left, min_right)
    max_val = max(max_left, max_right)

    return min_val, max_val

# Example usage
arr = [3, 5, 1, 8, 2, 9, 4]
min_val, max_val = find_min_max(arr, 0, len(arr) - 1)
print(f"Minimum: {min_val}, Maximum: {max_val}")
