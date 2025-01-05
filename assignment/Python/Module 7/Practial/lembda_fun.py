# Lambda function to compute the sum and product of two numbers
sum_and_product = lambda x, y: (x + y, x * y)

# Example usage
result = sum_and_product(3, 4)
print("Sum:", result[0])
print("Product:", result[1])
