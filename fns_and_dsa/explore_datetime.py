from datetime import datetime, timedelta

def display_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculate_future_date(days: int):
    return (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")

def main():
    print(f"Current Date and Time: {display_current_datetime()}")
    
    while True:
        try:
            days_to_add = int(input("Enter the number of days to add: "))
            print(f"Future Date after {days_to_add} days: {calculate_future_date(days_to_add)}")
            break  
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()