def length_busyb(flowers, hive):
    """Takes a list of coordinates (tuples) of the flowers and the coordinates
    (tuple) of the bee hive, calculates the total Manhattan distance (integer),
    returns the total distance travelled by the bee"""
    # first the bees will start at the hive
    location = hive
    total = 0
    for count in range(0, len(flowers)):
        # use the given formula to calculate Manhattan distance
        distance = (abs(location[0] - flowers[count][0])
                    + abs(location[1] - flowers[count][1]))
        # update the total distance and current location
        total += distance
        location = flowers[count]
    # include the final step back to the hive in the total
    total += (abs(location[0] - hive[0]) 
              + abs(location[1] - hive[1]))
    return total