"""
Define function w/2 arguments
    List of integers
    Single integer (index point)

    Add up all numbers in the list
    up to one past the index point provided
"""


# Function defitions
def list_sum(int_list, index):
    if index == 0:
        return int_list[index]

    return int_list[index] + list_sum(int_list, index - 1)


print(f"Sum: {list_sum([1, 4, 5, 3, 12, 16], 4)}")
print(f"Sum: {list_sum([4, 3, 1, 5], 1)}")
