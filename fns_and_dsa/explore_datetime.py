# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display current date and time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date

# Part 2: Calculate a future date
def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)

# Main function to run the script
def main():
    current_date = display_current_datetime()

    try:
        days_input = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_input)
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")

if __name__ == "__main__":
    main()