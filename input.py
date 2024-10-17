'''
Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
'''
# Input the set values
set_values = input().split()
my_set = set(map(int, set_values))

# Input the element to delete
element_to_delete = int(input())

# Attempt to remove the element
if element_to_delete in my_set:
    my_set.remove(element_to_delete)
    # Print the updated set
    print(" ".join(map(str, sorted(my_set))))
else:
    print("Given value is not present in the set list.")
