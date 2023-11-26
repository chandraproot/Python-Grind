import matplotlib.pyplot as plt
import numpy as np

# Define the transfer function for a second-order system
def magnitude_response(frequency_ratio, Q):
    return 1 / np.sqrt(1 + (1 / Q)**2 * (frequency_ratio**2))

# Define the frequency ratio range around the resonance
frequency_ratio = np.linspace(0.9, 1.1, 1000)  # Close to the resonant frequency

# Set a very high Q value to observe the approaching infinity of magnification factor
Q_value = 1000  # Change to a high value for approaching infinity
magnification_factor = magnitude_response(frequency_ratio, Q_value)

# Plotting magnification factor vs frequency ratio
plt.figure(figsize=(8, 6))
plt.plot(frequency_ratio, magnification_factor, label=f'Q = {Q_value}')
plt.title('Magnitude Response vs Frequency Ratio')
plt.xlabel('Frequency Ratio')
plt.ylabel('Magnitude Factor')
plt.grid(True)
plt.legend()
plt.show()
