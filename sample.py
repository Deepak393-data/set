'''
Write a program to get the set values in a single line separated by space (including duplicate values) and print the number of elements in the given set.
Sample Input:
1 2 3 4 5 1 2 3
Sample Output:
5
'''
# Input the values in a single line
input_values = input().split()

# Convert the list to a set to remove duplicates
unique_values = set(input_values)

# Print the number of unique elements in the set
print(len(unique_values))
