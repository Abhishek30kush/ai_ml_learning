import numpy as np 
def uniform_dist():
    return np.random.uniform(1, 7, 1000)
def normal_dist():
    return np.random.normal(50, 10, 1000)
def binomial_dist():
    return np.random.uniform(10, 0.5, 1000)
def poisson_dist():
    return np.random.poisson(5, 1000)
def exponential_dist():
    return np.random.exponential(2, 1000)
def multinomial_dist():
    return np.random.multinomial(1000, [0.4, 0.35, 0.25])
def pareto_dist():
    return np.random.pareto(2, 1000)
def zipf_dist():
    return np.random.zipf(2, 1000)