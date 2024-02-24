import os
import numpy as np


def duplicate_and_shift(dictionary):
    max_x_coord = max(dictionary.keys())
    duplicate_dict = dictionary.copy()

    for key in duplicate_dict:
        duplicate_dict[key] += max_x_coord

    for key, value in duplicate_dict.items():
        dictionary[key] = value


def save_to_text_file(dictionary, filename):
    # Open the file in write mode
    with open(filename, 'w') as file:
        # Iterate through the dictionary items
        for key, value in dictionary.items():
            # Write each key-value pair as a line in the file in the specified format
            file.write(f"{key} {value}\n")


n_concentration = {}
p_concentration = {}

# number of times to repeat doping concentration
num_diodes = 4

with open('profiles/New_LOT18_N.txt', 'r') as file:
    lines = file.readlines()

    # Iterate through each line
    for line in lines:
        depth, doping_conc = line.split()
        n_concentration[float(depth)] = float(doping_conc)

with open('profiles/New_LOT18_N.txt', 'r') as file:
    lines = file.readlines()

    # Iterate through each line
    for line in lines:
        depth, doping_conc = line.split()
        p_concentration[float(depth)] = float(doping_conc)

for _ in range(num_diodes):
    duplicate_and_shift(n_concentration)
    duplicate_and_shift(p_concentration)

save_to_text_file(n_concentration, 'LOT18_N_extended')
save_to_text_file(p_concentration, 'LOT18_P_extended')
