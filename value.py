'''
Write a program to print the values which are similar in both given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
2 4 
'''
# Input the first set of values
set1_values = input().split()
set1 = set(map(int, set1_values))

# Input the second set of values
set2_values = input().split()
set2 = set(map(int, set2_values))

# Find the common values between the two sets
common_values = set1.intersection(set2)

# Convert the result to a sorted list
sorted_common_values = sorted(common_values)

# Print the common values with space separation
print(" ".join(map(str, sorted_common_values)))
