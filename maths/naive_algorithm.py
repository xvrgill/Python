"""
Algorithm for calculating the variance of an entire population of a given size.
"""

from typing import List

# Sample variance pseudo code - general reference for basic variance calculation:

# Get the mean of all observations
# Get the result of a single value of an observation minus the mean of all observations
# Square the result of the above
# Get the summ of the above for every observation
# Divide the above by the number of observations minus 1

# Naïve algorithm pseudo code:

# Get sum of all observations
# Square the above total
# Divde the above total by the total population size

# Square each observation
# Get sum of all squared observations
# Subtract the value of the first set of operations from the above total

# Divide the result of all operations above by the total population size

# Implementation definition
def naive_algorithm(observations: List[int]) -> int:
    pass


if __name__ == "__main__":
    # Insert doc test here
    pass
