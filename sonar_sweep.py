# importing .txt file
f = open('puzzle_input.txt', 'r')
# converting to a list and splitting (to remove the \n)
depths_list = f.read().splitlines()
# Converting the strings to integers
depths_list = [int(i) for i in depths_list]
f.close()

# Next, creating a function to iterate thru each depth and compare it to the previous depth to
# see if the depth increased or not. If true one will be added to the count variable.
def sonar_count(depths):
    """ Count the number of times the depth increased from the prior recorded depth.

    Args:
        depths (list): list of strings that contains the recorded depths

    Returns:
        count (int): total count of the number of times the depth increased from the prior depth
    """
    # Creating a variable to count how many times the depth increases within the function.
    count = 0
    # Created a variable to store the previous depth. Set it equal to the first number in the list
    # so that the count does not include the first comparison.
    prior_depth = depths[0]

    # Iterating thru the depths
    for depth in depths:
        # Comparing the current depth to the previous depth.
        if depth > prior_depth:
            # adding to the count if true.
            count += 1
        # Resetting the prior_depth variable for the comparison.
        prior_depth = depth

    return count


print(sonar_count(depths_list))
