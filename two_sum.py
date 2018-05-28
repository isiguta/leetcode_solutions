def two_sum(nums, target):
    for i, n in enumerate(nums):
        for j, m in enumerate(nums):
            if m + n == target and i != j:
                return [i, j]
