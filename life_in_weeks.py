#life in weeks

age = input("What is your current age?")

months = 12 
weeks = 52 
days = 365 

age = int(age)

age_in_months = age * 12 
age_in_weeks = age * 52
age_in_days = age * 365

age_in_months = months * 90 - age_in_months 
age_in_weeks = weeks * 90 - age_in_weeks
age_in_days = days * 90 - age_in_days

print(f"you have {age_in_days} days, {age_in_weeks} weeks, and {age_in_months} months left. ")