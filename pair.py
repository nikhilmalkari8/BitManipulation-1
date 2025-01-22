def singleNumber(nums: list[int]) -> list[int]:
    # Step 1: Find XOR of all numbers
    xor_xy = 0
    for num in nums:
        xor_xy ^= num

    # Step 2: Find the rightmost set bit
    rightmost_bit = xor_xy & -xor_xy

    # Step 3: Partition numbers into two groups and compute XOR for each
    num1, num2 = 0, 0
    for num in nums:
        if num & rightmost_bit:
            num1 ^= num  # Group where the set bit is 1
        else:
            num2 ^= num  # Group where the set bit is 0

    return [num1, num2]
