def binary_search(arr, target):
    low = 0
    high = len(arr)

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
            continue
        
        high = mid - 1
    
    return None # <-- return value if not found.


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6
location = binary_search(arr, target)

print(location)