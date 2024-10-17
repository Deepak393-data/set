'''
 Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5
'''
# Input the first set of values
set1_values = input().split()
set1 = set(map(int, set1_values))

# Input the second set of values
set2_values = input().split()
set2 = set(map(int, set2_values))

# Update the first set with the second set
set1.update(set2)

# Print the updated set with space separation
print(" ".join(map(str, sorted(set1))))
