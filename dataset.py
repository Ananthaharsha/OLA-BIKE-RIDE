import pandas as pd
import numpy as np

# Provided dataset
data = {
    'Priceperweek': [15, 15, 15, 25, 25, 25, 25, 30, 30, 30, 30, 40, 40, 40, 40, 40, 65, 102, 75, 75, 75, 80, 86, 98, 87, 77, 63],
    'Population': [1800000, 1790000, 1780000, 1778000, 1750000, 1740000, 1725000, 1725000, 1720000, 1705000, 1710000, 1700000, 1695000, 1695000, 1690000, 1630000, 1640000, 1635000, 1630000, 1620000, 1615000, 1605000, 1590000, 1595000, 1590000, 1600000, 1610000],
    'Monthlyincome': [5800, 6200, 6400, 6500, 6550, 6580, 8200, 8600, 8800, 9200, 9630, 10570, 11330, 11600, 11800, 11830, 12650, 13000, 13224, 13766, 14010, 14468, 15000, 15200, 15600, 16000, 16200],
    'Averageparkingpermonth': [50, 50, 60, 60, 60, 70, 75, 75, 75, 80, 80, 80, 85, 100, 105, 105, 105, 110, 125, 130, 150, 155, 165, 175, 175, 190, 200],
    'Numberofweeklyriders': [192000, 190400, 191200, 177600, 176800, 178400, 180800, 175200, 174400, 173920, 172800, 163200, 161600, 161600, 160800, 159200, 148800, 115696, 147200, 150400, 152000, 136000, 126240, 123888, 126080, 151680, 152800]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Define ranges based on the given data
price_range = (15, 102)
population_range = (1590000, 1800000)
income_range = (5800, 16200)
parking_range = (50, 200)
riders_range = (115696, 192000)

# Number of rows to generate
num_rows_to_generate = 10000 - len(df)

# Function to generate new rows with complex trends
def generate_row():
    # Randomly select a price based on a normal distribution to reflect higher prices being less common
    price = int(np.clip(np.random.normal(50, 20), price_range[0], price_range[1]))
    
    # Monthly income increases with price
    income = int(np.clip(np.random.normal(price * 150, 1000), income_range[0], income_range[1]))
    
    # Average parking per month increases with price
    parking = int(np.clip(np.random.normal(price * 2, 20), parking_range[0], parking_range[1]))
    
    # Population slightly decreases with price but with some randomness
    population = int(np.clip(1800000 - np.random.normal(price * 1000, 5000), population_range[0], population_range[1]))
    
    # Number of weekly riders decreases with price
    riders = int(np.clip(192000 - np.random.normal(price * 1000, 5000), riders_range[0], riders_range[1]))
    
    return [price, population, income, parking, riders]

# Generate new rows
new_rows = [generate_row() for _ in range(num_rows_to_generate)]

# Convert new data to DataFrame
new_df = pd.DataFrame(new_rows, columns=['Priceperweek', 'Population', 'Monthlyincome', 'Averageparkingpermonth', 'Numberofweeklyriders'])

# Combine with the original dataset
extended_df = pd.concat([df, new_df], ignore_index=True)

# Ensure uniqueness by dropping duplicates
extended_df.drop_duplicates(inplace=True)

# If duplicates are dropped, regenerate rows to maintain 1000 total rows
while len(extended_df) < 10000:
    new_rows = [generate_row() for _ in range(10000 - len(extended_df))]
    new_df = pd.DataFrame(new_rows, columns=['Priceperweek', 'Population', 'Monthlyincome', 'Averageparkingpermonth', 'Numberofweeklyriders'])
    extended_df = pd.concat([extended_df, new_df], ignore_index=True)
    extended_df.drop_duplicates(inplace=True)

# Verify the size of the dataset
extended_df.shape

# Display the first 10 rows of the extended dataset to verify
extended_df.head(10)

# Save the dataset to a CSV file
extended_df.to_csv('extended_dataset.csv', index=False)

extended_df.head(10), extended_df.shape
