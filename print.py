'''
Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
'''
# Input the first set of values
set1_values = input().split()
set1 = set(map(int, set1_values))

# Input the second set of values
set2_values = input().split()
set2 = set(map(int, set2_values))

# Find the different values (in set1 but not in set2)
different_values = set1 - set2

# Convert the result to a sorted list
sorted_different_values = sorted(different_values)

# Print the different values with space separation
print(" ".join(map(str, sorted_different_values)))
