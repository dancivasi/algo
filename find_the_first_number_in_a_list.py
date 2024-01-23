nums = [1, 2, 3, 4, 5]
target = 5
start = 0
end = len(nums) - 1

while len(nums[start:end + 1]) != 2:
    mid = (start + end) // 2

    if nums[mid] == target:
        end = mid
        continue
    elif nums[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
counter = start
for i in nums[start:end + 1]:
    if i != target:
        counter += 1
    else:
        print(counter)
        break