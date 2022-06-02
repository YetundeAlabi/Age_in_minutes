def age_in_minutes():
    from datetime import datetime
    while True:
        birth_year = (input("Enter year of birth: "))
        current_year = int(datetime.now().year)
        if len(birth_year) == 4:
            if 1900 <= int(birth_year) <= current_year:
                age = current_year - int(birth_year)
                age_in_min = age * 365 * 24 * 60
                return f"You are {age_in_min:,} minutes old."
            else:
                print("Invalid input.\nInput a valid year.")
        else:
            print("invalid input.\nInput a four digit number.")



print(age_in_minutes())
