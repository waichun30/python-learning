# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(height)
print(np_height)
print(type(height))
print(type(np_height))

bmi = np_weight/np_height **2
print(bmi)

print(bmi>25)

print(bmi[bmi>25])

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]


# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
lbs = np_weight_kg * 2.2


# Print out np_weight_lbs
print(lbs)