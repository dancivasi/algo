# tldr: gasesti primu numar duplicat
def solution(nums):
    duplicates = set()
    for number in nums:
        if number in duplicates:
            return number
        duplicates.add(number)
    return -1

if __name__ == "__main__":
    assert solution([2, 1, 3, 5, 3, 2]) == 3
    assert solution([2, 2]) == 2
    assert solution([2, 4, 3, 5, 1]) == -1