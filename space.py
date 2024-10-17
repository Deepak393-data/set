'''
Write a program to get input in a single line separated by space and print the values of set in single line separated by space.
Sample Input:
3 1 5 4 2
Sample Output:
1 2 3 4 5
'''
# Input the values in a single line
input_values = input().split()

# Convert the list of strings to a set of integers
unique_values = set(map(int, input_values))

# Convert the set to a sorted list
sorted_values = sorted(unique_values)

# Print the values with space separation
print(" ".join(map(str, sorted_values)))
