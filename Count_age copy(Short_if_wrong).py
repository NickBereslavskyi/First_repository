from datetime import datetime

now = datetime.now()
while True:
    date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        dob = datetime.strptime(date_of_birth, "%Y-%m-%d")
        if dob > now:
            print("Error: Date of birth is in the future. Please enter a valid date.")
            continue
        age_in_days = (now - dob).days
        age_years = age_in_days // 365  # Integer division to get whole years
        print(f"You are {age_years} years old.")
        break
    except ValueError:
        print("Incorrect format. Please enter the date in YYYY-MM-DD format.")