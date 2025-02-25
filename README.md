# ChaosMaps

A Python package for exploring chaos theory through the logistic map.

## Installation

```bash
pip install chaos
```

## Usage

### Command Line Interface

After installation, you can use the package from the command line:

```bash
# Generate a time series plot
chaos time -r 3.7 -x 0.2 -n 300

# Save the plot to a file
chaos time -r 3.5 -o logistic_plot.png

# Generate a bifurcation diagram
chaos bifurcation --rmin 3.4 --rmax 4.0

# Save a high-resolution bifurcation diagram
chaos bifurcation -p 2000 -o bifurcation.png
```

### Python API Example

```python
import matplotlib.pyplot as plt
import chaos as cm

# Plot the time series for the logistic map
cm.plot_time_series(n=200, r=3.7, x0=0.2)
plt.show()

# Create a bifurcation diagram
cm.plot_bifurcation_map(r_min=2.9, r_max=4.0)
plt.show()
```

### Advanced Usage

```python
import numpy as np
import matplotlib.pyplot as plt
import chaos as cm

# Calculate values directly
r = 3.9
x0 = 0.1
values = cm.iterate_logistic(n=500, r=r, x0=x0)

# Analyze the results
print(f"Min: {values.min()}")
print(f"Max: {values.max()}")
print(f"Mean: {values.mean()}")

# Create a custom plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Time series
ax1.plot(values[-100:])
ax1.set_title(f"Last 100 iterations (r={r})")

# Histogram
ax2.hist(values, bins=30, alpha=0.7)
ax2.set_title("Distribution of values")

plt.tight_layout()
plt.show()
```

## Features

- Compute and iterate the logistic map equation
- Create time series plots showing system evolution
- Generate bifurcation diagrams to visualize chaotic behavior
- Customizable plotting options

## License

MIT