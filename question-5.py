from typing import List
def findMinOfSortedArrays(arr1: List[float], arr2: List[float]):
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    l1 = len(arr1)
    l2 = len(arr2)
    low, high = 0, l1
    while low <= high:
        part_x = (low + high)//2
        part_y = (l1 + l2 + 1)//2 - part_x
        max_left_x = float('-inf')
        max_left_y = float('-inf')
        min_right_x = float('inf')
        min_right_y = float('inf')
        if part_x != 0:
            max_left_x = arr1[part_x-1]
        if part_y != 0:
            max_left_y = arr2[part_y-1]
        if part_x != l1:
            max_left_x = arr1[part_x]
        if part_y != l2:
            max_left_y = arr2[part_y]
        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (l1 + l2) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            else:
                return max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:
            high = part_x - 1
        else:
            low = part_x + 1

print(findMinOfSortedArrays([1,3],[2]))
