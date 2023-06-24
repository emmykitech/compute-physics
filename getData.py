import requests
import csv


#url = "https://psl.noaa.gov/data/correlation/amon.us.data"

# Longer amount of data
url = "https://psl.noaa.gov/data/correlation/amon.us.long.data"

filename = "amon_data_long.csv"

# Fetch the content from the URL
response = requests.get(url)
content = response.text

# Split the content into lines
lines = content.split("\n")

# Open the CSV file in write mode
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Iterate over each line and write it to the CSV file
    for line in lines:
        # Skip empty lines or lines starting with '#' (comments)
        if line.strip() == "" or line.startswith("#"):
            continue

        # Split the line by whitespace and write it as a row in the CSV file
        row = line.split()
        writer.writerow(row)

print(f"CSV file '{filename}' has been created successfully.")
