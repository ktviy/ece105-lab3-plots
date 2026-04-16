"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_data(seed):
    """Generate synthetic temperature sensor data.
    
    Creates synthetic temperature readings from two sensors and corresponding
    timestamps. Sensor A has a mean of 25°C with std of 3°C, and Sensor B
    has a mean of 27°C with std of 4.5°C. Both sensors collect 200 readings
    over a 10-second time span.
    
    Parameters
    ----------
    seed : int
        Random seed for reproducibility of the synthetic data.
    
    Returns
    -------
    sensor_a : ndarray
        Shape (200,), float64. Temperature readings from Sensor A in Celsius.
    sensor_b : ndarray
        Shape (200,), float64. Temperature readings from Sensor B in Celsius.
    timestamps : ndarray
        Shape (200,), float64. Time values uniformly spaced from 0 to 10 seconds.
    """
    rng = np.random.default_rng(seed=seed)
    
    # Sensor A: mean 25°C, std 3°C, 200 readings
    sensor_a = rng.normal(loc=25, scale=3, size=200)
    
    # Sensor B: mean 27°C, std 4.5°C, 200 readings
    sensor_b = rng.normal(loc=27, scale=4.5, size=200)
    
    # Timestamps: 200 values uniformly spaced from 0 to 10 seconds
    timestamps = np.linspace(0, 10, 200)
    
    return sensor_a, sensor_b, timestamps


# Generate synthetic data for two sensors and timestamps
sensor_a, sensor_b, timestamps = generate_data(seed=6942)

# Generate and save scatter plot over time
plt.figure(figsize=(10, 6))
plt.scatter(timestamps, sensor_a, color='blue', label='Sensor A', alpha=0.6, s=30)
plt.scatter(timestamps, sensor_b, color='orange', label='Sensor B', alpha=0.6, s=30)
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Readings from Two Sensors')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
plt.close()

# Generate and save histogram of sensor readings
plt.figure(figsize=(10, 6))
plt.hist(sensor_a, bins=30, alpha=0.5, label='Sensor A', color='blue')
plt.hist(sensor_b, bins=30, alpha=0.5, label='Sensor B', color='orange')
plt.axvline(sensor_a.mean(), color='blue', linestyle='--', linewidth=2, label=f'Sensor A Mean: {sensor_a.mean():.2f}°C')
plt.axvline(sensor_b.mean(), color='orange', linestyle='--', linewidth=2, label=f'Sensor B Mean: {sensor_b.mean():.2f}°C')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.title('Temperature Distribution Comparison')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('histogram.png', dpi=300, bbox_inches='tight')
plt.close()

# Generate and save box plot comparing the two sensors distributions
plt.figure(figsize=(10, 6))
plt.boxplot([sensor_a, sensor_b], labels=['Sensor A', 'Sensor B'])
overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
plt.axhline(overall_mean, color='red', linestyle='--', linewidth=2, label=f'Overall Mean: {overall_mean:.2f}°C')
plt.xlabel('Sensor')
plt.ylabel('Temperature (deg C)')
plt.title('Temperature Distribution Comparison: Box Plot')
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.savefig('box_plot.png', dpi=300, bbox_inches='tight')
plt.close()

print("Plots generated and saved successfully!") 
