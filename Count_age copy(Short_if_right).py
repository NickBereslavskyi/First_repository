from datetime import datetime
from datetime import datetime as dtdt

now = datetime.now() # or datetime.today()
print(now)

now2 = dtdt.now()
print(now2)

while True:
    date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ") # short name - dob
    try:
        dob = datetime.strptime(date_of_birth, "%Y-%m-%d") # the same essential of the name dob
        if dob < now:
            
            a_d = now.year - dob.year # Wrong answer without consedering presice date(month, day)
            print(a_d)

            age_days = (now - dob).days
            print(age_days)
            
            age_years = int(age_days // 365.25)  # Integer division to get whole years
            print(f"You are {age_years} years old.")
            break
        else:
            print("Error: Date of birth is in the future. Please enter a valid date.")
            continue
    except ValueError:
        print("Incorrect format. Please enter the date in YYYY-MM-DD format.")