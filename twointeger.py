def divide(dividend: int, divisor: int) -> int:
    # Define constants for 32-bit signed integer limits
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # Handle edge case for overflow
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    # Determine the sign of the result
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    # Work with absolute values
    dividend, divisor = abs(dividend), abs(divisor)

    # Initialize the quotient
    quotient = 0

    # Subtract divisor multiples from dividend
    while dividend >= divisor:
        current_divisor, num_divisors = divisor, 1
        while dividend >= (current_divisor << 1):
            current_divisor <<= 1
            num_divisors <<= 1
        dividend -= current_divisor
        quotient += num_divisors

    # Apply the sign to the result
    result = sign * quotient

    # Ensure the result is within the 32-bit signed integer range
    return max(INT_MIN, min(INT_MAX, result))

