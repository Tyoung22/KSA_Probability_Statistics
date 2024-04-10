import numpy as np
import matplotlib.pyplot as plt
import statistics

n = 10000  # num of sampling
a = 10; b = 7
mean = 0; sd = 25**0.5

visualize_mode = True # True or False 

a_hats1 = a + np.random.normal(mean, sd, n)
b_hats1 = b + np.random.normal(mean, sd, n)

a_plus_b_hats = a + b + np.random.normal(mean, sd, n)
a_minus_b_hats = a - b + np.random.normal(mean, sd, n)
a_hats2 = (a_plus_b_hats + a_minus_b_hats) / 2
b_hats2 = (a_plus_b_hats - a_minus_b_hats) / 2


#log
print(f"a:{a}, b:{b}")
print(f"Mean:{mean}")
print(f"Variance:{sd**2}")
print()
print("a_hats1:")
print(f"Mean:{statistics.mean(a_hats1)}")
print(f"Variance:{statistics.variance(a_hats1)}")
print()
print("b_hats1:")
print(f"Mean:{statistics.mean(b_hats1)}")
print(f"Variance:{statistics.variance(b_hats1)}")
print()
print("a_hats2:")
print(f"Mean:{statistics.mean(a_hats2)}")
print(f"Variance:{statistics.variance(a_hats2)}")
print()
print("b_hats2:")
print(f"Mean:{statistics.mean(b_hats2)}")
print(f"Variance:{statistics.variance(b_hats2)}")

#visualizing
if visualize_mode:
    plt.figure(figsize=(10, 6))

    min_val = min(np.min(a_hats1), np.min(b_hats1), np.min(a_hats2), np.min(b_hats2))
    max_val = max(np.max(a_hats1), np.max(b_hats1), np.max(a_hats2), np.max(b_hats2))

    bins = np.linspace(min_val, max_val, 50) 
    for data, label, color in [(a_hats1, 'a_hats1', 'salmon'), (b_hats1, 'b_hats1', 'lightblue'), (a_hats2, 'a_hats2', 'darkred'), (b_hats2, 'b_hats2', 'royalblue')]:
        hist, edges = np.histogram(data, bins=bins)
        plt.plot((edges[1:] + edges[:-1])/2, hist, label=label, color=color)

    plt.title('Sample Value Frequencies')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()


import numpy as np
import matplotlib.pyplot as plt
import statistics

n = 10000  # num of sampling
a = 10; b = 7
mean = 0; sd = 25**0.5

visualize_mode = True # True or False 

a_hats1 = a + np.random.normal(mean, sd, n)
b_hats1 = b + np.random.normal(mean, sd, n)

a_plus_b_hats = a + b + np.random.normal(mean, sd, n)
a_minus_b_hats = a - b + np.random.normal(mean, sd, n)
a_hats2 = (a_plus_b_hats + a_minus_b_hats) / 2
b_hats2 = (a_plus_b_hats - a_minus_b_hats) / 2


#log
print(f"a:{a}, b:{b}")
print(f"Mean:{mean}")
print(f"Variance:{sd**2}")
print()
print("a_hats1:")
print(f"Mean:{statistics.mean(a_hats1)}")
print(f"Variance:{statistics.variance(a_hats1)}")
print()
print("b_hats1:")
print(f"Mean:{statistics.mean(b_hats1)}")
print(f"Variance:{statistics.variance(b_hats1)}")
print()
print("a_hats2:")
print(f"Mean:{statistics.mean(a_hats2)}")
print(f"Variance:{statistics.variance(a_hats2)}")
print()
print("b_hats2:")
print(f"Mean:{statistics.mean(b_hats2)}")
print(f"Variance:{statistics.variance(b_hats2)}")

#visualizing
if visualize_mode:
    plt.figure(figsize=(10, 6))

    min_val = min(np.min(a_hats1), np.min(b_hats1), np.min(a_hats2), np.min(b_hats2))
    max_val = max(np.max(a_hats1), np.max(b_hats1), np.max(a_hats2), np.max(b_hats2))

    bins = np.linspace(min_val, max_val, 50) 
    for data, label, color in [(a_hats1, 'a_hats1', 'salmon'), (b_hats1, 'b_hats1', 'lightblue'), (a_hats2, 'a_hats2', 'darkred'), (b_hats2, 'b_hats2', 'royalblue')]:
        hist, edges = np.histogram(data, bins=bins)
        plt.plot((edges[1:] + edges[:-1])/2, hist, label=label, color=color)

    plt.title('Sample Value Frequencies')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

