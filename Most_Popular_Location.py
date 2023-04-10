def popular_busyb(flowers, visits, hive):
    """Takes a dictionary including flower types and coordinates, a set of
    visits (strings), hive coordinates (tuple), finds the type of flower with 
    the highest total distance (weight) to the hive, returns the most popular 
    type of flower."""
    flower_dict = {}
    # create key values for the flower dictionary (no duplicates)
    for visit in visits:
        key = flowers[visit][0]
        if key not in flower_dict:
            flower_dict[key] = 0
    # use Manhattan distance equation to find each flower's weight and tally
    # them up in the dictionary
    for visit in visits:
        key = flowers[visit][0]
        flower_dict[key] += (abs(hive[0] - flowers[visit][1]) 
                             + abs(hive[1] - flowers[visit][2]))
    max_weight = 0
    popular = []
    # find the maximum weight
    for flower in flower_dict:
        if flower_dict[flower] > max_weight:
            max_weight = flower_dict[flower]
    # find the flower(s) with the maximum weight and put it/them in a list
    for flower in flower_dict:
        if flower_dict[flower] == max_weight:
            popular.append(flower)
    # sort the list according to Unicode, the answer is the first value
    popular.sort()
    most_popular = popular[0]
    return most_popular