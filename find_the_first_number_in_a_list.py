def middle_target(nums):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            print(mid)
            break
        elif nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
    return mid

def find_index(side):

    if side == 'stanga':
        mid = middle_target(nums)
        start = 0
        end = mid
        while len(nums[start:end+1]) != 2:
            middle =  middle_target(nums[start:end+1])

            if nums[middle] == target:
                end = mid
                continue
            elif nums[mid] < target:
                start = mid
            else:
                end = mid


    elif side == 'dreapta':
        start = 0
        end = mid
        while len(nums[start:end + 1]) != 2:
            middle = middle_target(nums[start:end + 1])

            if nums[middle] == target:
                end = mid
                continue
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

nums = [1, 2, 3, 4, 5, 5, 5, 6]
target = 5
mid = middle_target(nums)
find_index('stanga')
find_index('dreapta')