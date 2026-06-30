import json
import glob
import numpy as np

# ---------------------------------------------------------
# Snoozr ML — Sleep Data Loader + Linear Regression Report
# ---------------------------------------------------------

def load_sleep_files(pattern):
    """Load all JSON files matching a pattern."""
    data = []
    for file in glob.glob(pattern):
        with open(file, "r") as f:
            content = json.load(f)
            # Extract the first (and only) top-level key
            month_key = list(content.keys())[0]
            data.extend(content[month_key])
    return data


def generate_report(sleep_data):
    """Generate a simple text report from sleep data."""
    hours = [entry["hours_slept"] for entry in sleep_data]
    ratings = [entry["sleep_rating"] for entry in sleep_data]

    avg_hours = sum(hours) / len(hours)
    avg_rating = sum(ratings) / len(ratings)

    print("----- Snoozr ML Sleep Report -----")
    print(f"Total nights recorded: {len(hours)}")
    print(f"Average hours slept: {avg_hours:.2f}")
    print(f"Average sleep rating: {avg_rating:.2f}")
    print("----------------------------------")


def run_linear_regression(sleep_data):
    """Run a simple linear regression predicting next night's sleep."""
    hours = np.array([entry["hours_slept"] for entry in sleep_data])
    days = np.arange(len(hours))

    # Fit line: y = m*x + b
    m, b = np.polyfit(days, hours, 1)

    next_day = len(hours)
    predicted = m * next_day + b

    print("----- Linear Regression -----")
    print(f"Slope (m): {m:.3f}")
    print(f"Intercept (b): {b:.3f}")
    print(f"Predicted next sleep duration: {predicted:.2f} hours")
    print("----------------------------------")


# ---------------------------------------------------------
# Main Execution
# ---------------------------------------------------------

# Load all months for one user
sleep_data = load_sleep_files("user01_2026-*_sleep.json")

# Generate report
generate_report(sleep_data)

# Run regression
run_linear_regression(sleep_data)
