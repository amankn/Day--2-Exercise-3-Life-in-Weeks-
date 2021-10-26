# 🚨 Don't change the code below 👇
age = input("What is your current age? : ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(type(age))

age_as_int = int(age)

current_lived_days = 365 * age_as_int

current_lived_months = 12 * age_as_int

current_lived_weeks = 52 * age_as_int

rem_days = 365 * 90 - current_lived_days

rem_months = 12 * 90 - current_lived_months

rem_weeks = 52 * 90 - current_lived_weeks

print(f"You have {rem_days} days, {rem_weeks} weeks, and {rem_months} months left. ")








