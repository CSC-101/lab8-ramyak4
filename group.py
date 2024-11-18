
# This function creates consecutive groups of 3 from a given list in a new list
# input: a list of integers
# output: a nested list of integers
def groups_of_3(group: list[int]) -> list[list[int]]:
    new_group = []
    i = 0
    while i < len(group):
        temp_group = []
        if i <= (len(group) -1 ):
            temp_group.append(group[i])
        if i + 1 <= (len(group) -1 ):
            temp_group.append(group[i+1])
        if i + 2 <= (len(group) - 1):
            temp_group.append(group[i + 2])
        new_group.append(temp_group)
        i += 3
    return new_group

