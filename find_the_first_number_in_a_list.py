nums = [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
        9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
target = 5
start = 0
end = len(nums) - 1

while len(nums[start:end + 1]) != 2:
    mid = (start + end) // 2

    if nums[mid] == target:
        end = mid
        continue
    elif nums[mid] < target:
        start = mid
    else:
        end = mid
counter = start
for i in nums[start:end + 1]:
    if i != target:
        counter += 1
    else:
        print(counter)
        break