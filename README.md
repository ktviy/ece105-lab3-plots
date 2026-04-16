# ECE Lab 3: Sensor Data Visualization

Generate publication-quality visualizations of synthetic temperature sensor data using NumPy and Matplotlib.

## Installation

This project requires Python 3.x with NumPy and Matplotlib. The dependencies are already configured in the `ece105` conda environment.

To set up:

1. Activate the conda environment:
   ```bash
   conda activate ece105
   ```

2. Ensure NumPy and Matplotlib are installed:
   ```bash
   conda install numpy matplotlib
   ```
   or with mamba:
   ```bash
   mamba install numpy matplotlib
   ```

## Usage

Run the script from the project directory:

```bash
python generate_plots.py
```

This will generate synthetic temperature data from two sensors and create a composite visualization.

## Example Output

The script generates `sensor_analysis.png`, a composite figure containing three subplots:

1. **Scatter Plot**: Shows temperature readings from both Sensor A (blue) and Sensor B (orange) over a 10-second time span. Each sensor has 200 readings. This visualization helps identify temporal patterns and relative sensor behavior.

2. **Histogram**: Displays the distribution of temperature readings for both sensors using overlaid histograms with 30 bins. Vertical dashed lines indicate the mean temperature for each sensor (Sensor A: ~25°C, Sensor B: ~27°C).

3. **Box Plot**: A side-by-side comparison showing the distribution statistics (median, quartiles, outliers) for each sensor. A horizontal dashed line indicates the overall mean of both sensors combined, providing a reference for comparison.

All visualizations are saved at 150 DPI in a single composite figure suitable for presentations and reports.

## AI Tools Used and Disclosure

[Placeholder: Describe any AI tools, models, or generative AI services used in creating or assisting with this project. Include model names, versions, and the nature of assistance provided.]