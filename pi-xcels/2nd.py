def product_except_self(nums):
    n = len(nums)
    
    # Initialize output array
    output = [1] * n
    
    # Left product calculation (excluding self)
    left = 1
    for i in range(n):
        output[i] = left
        left *= nums[i]
    
    # Right product calculation (excluding self)
    right = 1
    for i in range(n-1, -1, -1):
        output[i] *= right
        right *= nums[i]
    
    return output

# Test cases
print(product_except_self([10, 3, 5, 6, 2]))  # Output: [180, 600, 360, 300, 900]
print(product_except_self([12, 0]))            # Output: [0, 12]
