# importing .txt file
f = open('puzzle_input.txt', 'r')
# Converting to a list and splitting (to remove the \n)
depths_list = f.read().splitlines()
# Converting the strings to integers
depths_list = [int(i) for i in depths_list]
f.close()

# Iterating thru the depths, adding the first three depths together, then the next three,
# and so on. Then comparing both to see if the sum increased.
def sliding_count(depths):
    """ Count the number of times the sum of the depth of three measurements is greater than
    the previous sum of three depth measurements.

    Args:
        depths (list): list of strings that contains the recorded depths

    Returns:
        count (int): The total count of the number of times the three measurements increased.
    """
    # created empty list to store the added measurements
    sliding_sum = []

    # Adding three measurements using the window sliding technique.
    for i in range(len(depths) - 3 + 1):
        sliding_sum.append(sum(depths[i:i + 3]))

    # Variable to count the number of times the measurements increased
    count = 0
    # Variable to store the prior total of the three measurements, initially set to the first sum,
    # so that the count will not include the first comparison.
    prior_sum = sliding_sum[0]

    # Iterating thru the measurement list to compare the measurements.
    for sum_measure in sliding_sum:
        # Comparing the current and prior measurements.
        if sum_measure > prior_sum:
            # Adding one to the count if true
            count += 1
        # Resetting the prior_sum amount
        prior_sum = sum_measure
    return count


print(sliding_count(depths_list))
