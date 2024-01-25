nums = [1,1,1,1,1,1,1,1,1,1,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,9,9,9,9,99,99,99]
target = 5


def find_middle(nums, target):
    start = 0
    end = len(nums) - 1

    while start < end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1


def find_first_or_last(nums, side, mid):
    if side == "first":
        start = 0
        end = mid
        while start < end:
            middle = (start + end) // 2
            if nums[middle] == target:
                end = middle
                if nums[end - 1] != target:
                    return middle
            elif nums[middle] < target:
                start = middle
        return middle

    if side == "last":
        start = mid
        end = len(nums) - 1
        while end > start:
            middle = (start + end + 1) // 2
            if nums[middle] == target:
                start = middle
                if start == len(nums) - 1 and nums[start] == target:
                    return middle
                elif nums[start + 1] != target:
                    return middle
            elif nums[middle] > target:
                end = middle
        return middle


mid = find_middle(nums, target)
print(find_first_or_last(nums, "first", mid))
print(find_first_or_last(nums, "last", mid))