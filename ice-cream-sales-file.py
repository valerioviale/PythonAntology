import numpy as np
import pandas as pd

# Generate temperature data (example - replace with your actual data)
np.random.seed(0)  # for reproducibility
temperatures = np.random.randint(15, 35, size=20)  # Temperatures between 15 and 35 degrees Celsius

# Generate ice cream sales data
ice_cream_sales = np.random.randint(1, 31, size=20)  # Sales between 1 and 30

# Create a Pandas DataFrame
df = pd.DataFrame({'Temperature (X)': temperatures, 'Ice Cream Sales (Y)': ice_cream_sales})

# Save the DataFrame to a CSV file
csv_file_path = 'temperature_icecream_data.csv'  # You can change the filename here
df.to_csv(csv_file_path, index=False)  # index=False prevents writing the DataFrame index to the CSV

print(f"Data saved to {csv_file_path}")