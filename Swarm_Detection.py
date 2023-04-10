def swarm_busyb(trajectories, duration):
    """Takes a list of trajectories (lists) indicating the locations (tuples)
    each bee visits and the minimum duration (integer) to form a swarm,
    calculates the longest distance travelled by the at least two bees, returns 
    whether they have formed a swarm."""
    distance = 0
    max_distance = 0
    # compare the path of two different bees
    for alpha_bee in trajectories:
        for beta_bee in trajectories:
            if beta_bee != alpha_bee:
                # increase distance travelled by 1 for every square together
                for i in range(0, len(beta_bee)):
                    if alpha_bee[i] == beta_bee[i]:
                        distance += 1
                        # find the longest distance travelled by the two bees
                        if distance > max_distance:
                            max_distance = distance
                    # when the bees separate, count resets and will restart
                    # when they meet again
                    if distance >= 1 and alpha_bee[i] != beta_bee[i]:
                        distance = 0
                if max_distance >= duration:
                    return True
                # reset count and max if the current pair cannot form a swarm
                else:
                    distance = 0
                    max_distance = 0
    return False