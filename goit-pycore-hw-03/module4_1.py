from datetime import datetime

def get_days_from_today():
    try:
        input_date_str = input("Enter a date (YYYY-MM-DD): ")
        input_date = datetime.strptime(input_date_str, "%Y-%m-%d").date()
        current_date = datetime.now()
        return current_date.toordinal() - input_date.toordinal()
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."
print(f"Difference in days: {get_days_from_today()}") 

