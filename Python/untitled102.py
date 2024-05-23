#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:43:34 2024

@author: johnpaulmbagwu
"""

import os
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import pandas as pd

# Read the TXT data file containing information about AIR
df = pd.read_csv('AIR.TXT', delimiter=' ')

# Extract the stopping power and energy columns from the dataframe
stopping_power = df['TotalStp.Pow']
energy = df['KineticEnergy']

# Plotting
plt.figure(figsize=(10, 6))

# Plotting both calculated and experimental stopping power
plt.plot(energy, stopping_power, label='AIR PSTAR Data')

plt.title('AIR')
plt.xlabel('Energy (MeV)')
plt.ylabel('Stopping Power (MeV/(g/cm^2))')

# Set the x and y-axis scales to logarithmic for better visualization
plt.xscale('log')
plt.yscale('log')

# Set the x-axis and y-axis limits for better visibility of data points
plt.xlim(1e-2, 1e4)

plt.grid(True)
plt.legend()

plt.show()