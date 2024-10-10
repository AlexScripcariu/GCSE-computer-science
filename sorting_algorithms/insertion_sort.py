def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return arr


nums = [5, 1, 3, 4, 7, 9, 8, 6, 2]

nums = insertion_sort(nums)

print(nums)