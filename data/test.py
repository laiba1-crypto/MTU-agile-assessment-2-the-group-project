import pandas as pd
import matplotlib.pyplot as plt

def analyze_weather_data(file_path):
        # Read the weather data from the CSV file
    weather_data = pd.read_csv(file_path)

            # Task 1: Find the number of unique locations present in the dataset
    unique_locations = weather_data['Location'].nunique()
    print("Number of unique locations:", unique_locations)

            # Task 2: Display the five locations with the fewest records or rows
    location_counts = weather_data['Location'].value_counts().sort_values()
    top_5_locations = location_counts.head(5)

            # Visualize the five locations with the fewest records
    plt.bar(top_5_locations.index, top_5_locations.values)
    plt.xlabel('Location')
    plt.ylabel('Number of Records')
    plt.title('Locations with the Fewest Records')
    plt.show()

            # Calculate and display the percentage for each section
    total_records = len(weather_data)
    percentages = (top_5_locations / total_records) * 100
    print("Percentage for each section:")
    print(percentages)

    """# Data Cleaning
    # Drop rows with missing values in relevant columns
    relevant_columns = ['Location', 'OtherRelevantColumn1', 'OtherRelevantColumn2']
    weather_data_cleaned = weather_data.dropna(subset=relevant_columns)
    
    # Drop duplicate rows
     weather_data_cleaned = weather_data_cleaned.drop_duplicates()
    
    # Additional cleaning steps as needed...
    
     # Display cleaned data summary
    cleaned_records = len(weather_data_cleaned)
    print(f"\nAfter cleaning, the dataset has {cleaned_records} records.")"""

        # Usage example
    file_path = r'C:\Users\asifl\OneDrive\Desktop\pthon\weather.csv'
    analyze_weather_data(file_path)
