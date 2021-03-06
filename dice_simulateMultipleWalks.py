import numpy as np
import matplotlib.pyplot as plt


# Initialize all_walks
all_walks = []

# Simulate random walk 10 times , change value to simulate n number of times
for i in range(500):

    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)

        # Implement clumsiness
        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)


# Print all_walks
print(all_walks)
print(type(all_walks))


# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)


# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# every row in np_all_walks represents the position after 1 throw for the 10 random walks

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()

#print(np_aw_t)


# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :]
print(ends)
# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

# what's the estimated chance that you'll reach 60 steps high
# if you play this Empire State Building game
# To calculate the chance that this end point is greater than or equal to 60,
# you can count the number of integers in ends that are greater than or equal to 60 and divide that number by 500, the total number of simulations

new_end = ends[ends>=60]
print(new_end)
print(type(new_end))
print(np.count_nonzero(new_end)/500)