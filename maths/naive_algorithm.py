"""algorithm for calculating the variance of an entire population."""
from typing import List

import numpy as np


# Numpy implementation
def naive_algorithm(observations: List[int]) -> int:
    """
    Naive algorithm that calculates variance of an entire population.

    Parameters
    ----------
    observations : array_like
    the 1st param name `first`

    Returns
    -------
    int
    the calculated variance of population N (count of observations passed as
    @param:observations)
    """
    # Get the mean of all observations
    population_size: int = len(observations)
    # Get sum of all observations
    sum_of_observations: int = np.sum(observations)
    # Square the above total
    sum_of_observations_squared: int = np.square(sum_of_observations)
    # Divde the above total by the total population size
    obs_squared_div_population_size: int = np.divide(
        sum_of_observations_squared, population_size
    )
    # Square each observation
    square_of_each_observation: int = [np.square(x) for x in observations]
    # Get sum of all squared observations
    sum_of_square_of_each_observation: int = np.sum(square_of_each_observation)
    # Subtract the value of the first set of operations from the above total
    difference: int = np.subtract(
        sum_of_square_of_each_observation, obs_squared_div_population_size
    )
    # Divide the result of all operations above by the total population size
    difference_div_population: int = np.divide(difference, population_size)

    return difference_div_population


if __name__ == "__main__":
    # Insert doc test here
    print(naive_algorithm([28, 290, 12, 37]))
