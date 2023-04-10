def locate_busyb(flowers, xmax, ymax):
    """Takes a list of coordinates (tuples) of flowers and the maximum x and y
    coordinates (integers), go through every square from left to right, upwards
    towards the final square (xmax, ymax), returns the coordinates (tuple) of
    the first chosen location (furthest from the other flowers)."""
    max_val = 0
    # go through x coordinates before y coordinates to eliminate the need to
    # use the x + (y * xmax) equation.
    for y in range(0, ymax + 1):
        for x in range(0, xmax + 1):
            # ensure it is in an empty cell
            if (x, y) not in flowers:
                total = 0
                # use the Manhattan distance equation to find total distance 
                # for each cell
                for i in range(0, len(flowers)):
                    distance = (abs(x - flowers[i][0])
                                + abs(y - flowers[i][1]))
                    total += distance
                # return the first flower with the maximum distance
                if total > max_val:
                    max_val = total
                    closest = (x, y)
    return closest