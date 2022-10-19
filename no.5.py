'''at_list = [1, 2, 3, 4, 5] # This is an existing list of numbers hidden in the hat.
print(at_list[-1])# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
at_list.remove("5")# Step 2: write a line of code that removes the last element from the list.
print(len(at_list))# Step 3: write a line of code that prints the length of the existing list.
 #print(at_list)
'''

hat=[1,2,3,4,5]

print(hat)
hat[2]=78

hat.pop()
print(hat)

hat.pop(1)
print(hat)

print(len(hat))