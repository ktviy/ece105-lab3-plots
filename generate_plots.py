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


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Draw scatter plot of sensor readings over time on an Axes object.
    
    Creates a scatter plot showing temperature readings from two sensors
    as a function of time. Sensor A is colored blue and Sensor B is colored
    orange. The plot includes axis labels, legend, and grid.
    
    Parameters
    ----------
    sensor_a : ndarray
        Shape (200,), float64. Temperature readings from Sensor A in Celsius.
    sensor_b : ndarray
        Shape (200,), float64. Temperature readings from Sensor B in Celsius.
    timestamps : ndarray
        Shape (200,), float64. Time values in seconds.
    ax : matplotlib.axes.Axes
        The Axes object to draw on. Modified in place.
    
    Returns
    -------
    None
    """
    ax.scatter(timestamps, sensor_a, color='blue', label='Sensor A', alpha=0.6, s=30)
    ax.scatter(timestamps, sensor_b, color='orange', label='Sensor B', alpha=0.6, s=30)
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Temperature Readings from Two Sensors')
    ax.legend()
    ax.grid(True, alpha=0.3)


def plot_histogram(sensor_a, sensor_b, ax):
    """Draw overlaid histogram of sensor temperature distributions on an Axes object.
    
    Creates histograms comparing the temperature distributions of two sensors.
    Sensor A is colored blue and Sensor B is colored orange with 50% transparency.
    Vertical dashed lines indicate the mean of each sensor.
    
    Parameters
    ----------
    sensor_a : ndarray
        Shape (200,), float64. Temperature readings from Sensor A in Celsius.
    sensor_b : ndarray
        Shape (200,), float64. Temperature readings from Sensor B in Celsius.
    ax : matplotlib.axes.Axes
        The Axes object to draw on. Modified in place.
    
    Returns
    -------
    None
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, label='Sensor A', color='blue')
    ax.hist(sensor_b, bins=30, alpha=0.5, label='Sensor B', color='orange')
    ax.axvline(sensor_a.mean(), color='blue', linestyle='--', linewidth=2, 
               label=f'Sensor A Mean: {sensor_a.mean():.2f}°C')
    ax.axvline(sensor_b.mean(), color='orange', linestyle='--', linewidth=2, 
               label=f'Sensor B Mean: {sensor_b.mean():.2f}°C')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Temperature Distribution Comparison')
    ax.legend()
    ax.grid(True, alpha=0.3)


def plot_boxplot(sensor_a, sensor_b, ax):
    """Draw side-by-side box plot comparing sensor distributions on an Axes object.
    
    Creates a box plot showing the distribution statistics (median, quartiles,
    range) for each sensor. A horizontal dashed line indicates the overall mean
    of both sensors combined.
    
    Parameters
    ----------
    sensor_a : ndarray
        Shape (200,), float64. Temperature readings from Sensor A in Celsius.
    sensor_b : ndarray
        Shape (200,), float64. Temperature readings from Sensor B in Celsius.
    ax : matplotlib.axes.Axes
        The Axes object to draw on. Modified in place.
    
    Returns
    -------
    None
    """
    ax.boxplot([sensor_a, sensor_b], labels=['Sensor A', 'Sensor B'])
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.axhline(overall_mean, color='red', linestyle='--', linewidth=2, 
               label=f'Overall Mean: {overall_mean:.2f}°C')
    ax.set_xlabel('Sensor')
    ax.set_ylabel('Temperature (deg C)')
    ax.set_title('Temperature Distribution Comparison: Box Plot')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')


# Generate synthetic data for two sensors and timestamps
sensor_a, sensor_b, timestamps = generate_data(seed=6942)

# Generate and save scatter plot over time
fig, ax = plt.subplots(figsize=(10, 6))
plot_scatter(sensor_a, sensor_b, timestamps, ax)
plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
plt.close()

# Generate and save histogram of sensor readings
fig, ax = plt.subplots(figsize=(10, 6))
plot_histogram(sensor_a, sensor_b, ax)
plt.savefig('histogram.png', dpi=300, bbox_inches='tight')
plt.close()

# Generate and save box plot comparing the two sensors distributions
fig, ax = plt.subplots(figsize=(10, 6))
plot_boxplot(sensor_a, sensor_b, ax)
plt.savefig('box_plot.png', dpi=300, bbox_inches='tight')
plt.close()

print("Plots generated and saved successfully!")
