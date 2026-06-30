import numpy as np

# ---------------------------------------------
# Snoozr ML — Simple Linear Regression Example
# ---------------------------------------------
# This script predicts expected hours of sleep
# based on recent sleep logs using basic linear
# regression (least squares method).
# ---------------------------------------------

# Example sleep durations (in hours)
# Replace these with real user logs
sleep_hours = np.array([6.5, 7.0, 6.0, 7.5, 8.0, 7.2, 6.8])

# Create x-values representing each day index
days = np.arange(len(sleep_hours))

# Linear regression calculation
# Fit a line: y = m*x + b
m, b = np.polyfit(days, sleep_hours, 1)

# Predict next day's sleep duration
next_day = len(sleep_hours)
predicted_sleep = m * next_day + b

print("Recent sleep logs:", sleep_hours)
print("Slope (m):", round(m, 3))
print("Intercept (b):", round(b, 3))
print("Predicted sleep for next day:", round(predicted_sleep, 2), "hours")
