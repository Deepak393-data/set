'''
Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
'''
# Input the number of elements
n = int(input())

# Initialize an empty list to hold the values
values = []

# Input the elements
for _ in range(n):
    element = int(input())
    values.append(element)

# Create a set from the list to remove duplicates
unique_values = set(values)

# Count the number of duplicate values
duplicate_count = len(values) - len(unique_values)

# Print the results
print("Duplicate Values:", duplicate_count)
print(" ".join(map(str, sorted(unique_values))))
