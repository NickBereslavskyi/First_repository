from datetime import datetime
from dateutil.relativedelta import relativedelta

now = datetime.now()
while True:
    date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        dob = datetime.strptime(date_of_birth, "%Y-%m-%d")
        if dob > now:
            print("Error: Date of birth is in the future. Please enter a valid date.")
            continue
        age = relativedelta(now, dob)
        print(f"You are {age.years} years, {age.months} months, and {age.days} days old.")
        break
    except ValueError:
        print("Incorrect format. Please enter the date in YYYY-MM-DD format.")