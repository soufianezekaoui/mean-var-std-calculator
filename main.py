import mean_var_std

# Test with the example from the project
result = mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])

print("Result for [0,1,2,3,4,5,6,7,8]:")
print(result)
print()

# Test the error handling
print("Testing error handling (list with 8 elements):")
try:
    mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7])
except ValueError as e:
    print(f"Error caught: {e}")
print()

# Another test case
print("Result for [1,2,3,4,5,6,7,8,9]:")
result2 = mean_var_std.calculate([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(result2)
