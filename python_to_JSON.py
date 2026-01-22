import json
import csv

# File paths
json_file_path = "movies.json"  # input JSON file
csv_file_path = "movies.csv"    # output CSV file

# Load JSON data
with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Open CSV file for writing
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write CSV header
    writer.writerow(['title', 'description', 'genres'])
    
    # Write rows
    for movie in data:
        title = movie.get('title', '')
        description = movie.get('description', '')
        genres = ', '.join(movie.get('genres', []))  # convert list to comma-separated string
        writer.writerow([title, description, genres])

print(f"JSON data has been successfully converted to {csv_file_path}")
