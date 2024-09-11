def count_distinct_ways_to_climb_stair(n_stairs):
    """
    Function to count distinct ways to climb a staircase with 'n_stairs' steps.
    A person can climb either 1 or 2 steps at a time.
    
    :param n_stairs: Total number of stairs (integer)
    :return: Number of distinct ways to reach the top (integer)
    """
    # Base case: If there are negative stairs, there is no way to climb
    if n_stairs < 0:
        return 0
    
    # Base case: If there are no stairs, there's exactly 1 way to be at the top (doing nothing)
    if n_stairs == 0:
        return 1
    
    # Recursive call: The person can either come from the (n-1)th stair or the (n-2)th stair
    ans = count_distinct_ways_to_climb_stair(n_stairs - 1) + count_distinct_ways_to_climb_stair(n_stairs - 2)
    
    return ans


# Example usage:
n_stairs = 5  # Suppose there are 5 stairs
ways = count_distinct_ways_to_climb_stair(n_stairs)
print(f"Distinct ways to climb {n_stairs} stairs: {ways}")

Distinct ways to climb 5 stairs: 8 #output
