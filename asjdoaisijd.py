arr = [1,2,3,4,4,4,4,5,6,7,8,9,10]
target = 4
left, right = 0, len(arr) - 1
while left <= right:
    ans = 10
    mid = (left + right) // 2
    if arr[mid] == target:
        ans = mid
        right = mid - 1
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
print(ans)
