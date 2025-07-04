def product_except_self(nums):
    # Initialize the output array
    n = len(nums)
    output = [1] * n
    
    # Step 1: Calculate left products and store in output array
    left_product = 1
    for i in range(n):
        output[i] = left_product
        left_product *= nums[i]
    
    # Step 2: Calculate right products and multiply with the corresponding left products
    right_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]
    
    return output

# Test case
nums = [10, 3, 5, 6, 2]
result = product_except_self(nums)
print(result)  # Output: [180, 600, 360, 300, 900]


