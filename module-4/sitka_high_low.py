# Lea Trueworthy
# November 8, 2024
# CSD 325 - Module 4.2 Assignment: High/Low Temperatures
# Description: Modify the sitka_highs.py program and add a menu that lets users choose to view high temps, low temps, or to exit.
# The program should loop until exit is selected, and an exit message should appear.

import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Function to plot high or low temperatures
# dates = x, temps = y, title, label for y, color of graph
def plot_temperatures(dates, temps, title, ylabel, color):
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    # Format plot
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel(ylabel, fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

# Function to read the weather data from the CSV file
def read_temp_file(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

    # Get dates and high and low temperatures from this file
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6])
            lows.append(low)
    return dates, highs, lows

# Main program
def main():
    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = read_temp_file(filename)

    while True:
        # Display menu
        print("\nMenu:")
        print("1 - View High Temperatures")
        print("2 - View Low Temperatures")
        print("3 - Exit")

        choice = input('Please select 1, 2 or 3: ')
        
        if choice == '1':
            # Plot high temperatures
            print("You select 1 - High Temperatures")
            plot_temperatures(dates, highs, "Daily High Temperatures - 2018", "Temperature (F)", 'red')
        elif choice == '2':
            # Plot low temperatures
            print("You selected 2 - Low Temperatures")
            plot_temperatures(dates, lows, "Daily Low Temperatures - 2018", "Temperature (F)", 'blue')
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid, try again")

# Run the program
if __name__ == "__main__":
    main()