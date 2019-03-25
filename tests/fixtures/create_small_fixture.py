import numpy as np

LIMIT = 1000

# Get indices that don't overlap for activities, flows, CFs
indices = np.unique(np.random.randint(0, 1000, 200))[:75]
np.random.shuffle(indices)

# Create array with 3 columns
# Row index, col index, value
# Can add uncertainty later
data = np.zeros((325, 3))

# Add 25 activities with unit production
activity_indices = indices[:25]
data[:25, 1] = data[:25, 0] = activity_indices
data[:25, 2] = 1

# Add inputs
for i, x in enumerate(range(175)):
    data[25 + i, :] = (np.random.choice(activity_indices), np.random.choice(activity_indices), -np.random.random())

# Add biosphere flows
flow_indices = indices[25:50]
data[200:250, 0] = np.random.choice(activity_indices, size=50)
data[200:250, 1] = np.random.choice(flow_indices, size=50)
data[200:250, 2] = np.random.random(size=50)

data[300:, 0] = flow_indices
data[300:, 1] = flow_indices
data[300:, 2] = 1

# Add CFs
flow_indices = indices[50:75]
data[250:275, 0] = np.random.choice(flow_indices, size=25)
data[250:275, 1] = flow_indices
data[250:275, 2] = np.random.random(size=25)

data[275:300, 0] = flow_indices
data[275:300, 1] = flow_indices
data[275:300, 2] = 1

np.save("small-fixture", data)
