def singleNumber(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num  # XOR each number
    return result

