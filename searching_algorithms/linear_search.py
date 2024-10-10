def linear_search(arr: list, target) -> list:
    for item in arr:
        if item == target:
            return item
    return -1   # return if the item is not found


shopping_list = ["birthday cake", "noodles", "fried chicken", "watermelon"]

print(linear_search(shopping_list, "noodles"))