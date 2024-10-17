'''
Write a program to get n number of values in separate line for set and print the values with space separation.
Sample Input:
5
3
1
4
5
2
Sample Output:
1 2 3 4 5 
'''
# Input the number of elements
n = int(input())

# Initialize an empty set to hold the elements
values_set = set()

# Input the elements into the set
for _ in range(n):
    element = int(input())
    values_set.add(element)

# Convert the set to a sorted list
sorted_values = sorted(values_set)

# Print the values with space separation
print(" ".join(map(str, sorted_values)))
