from datetime import date # Importing Library
todays_date = date.today() # Creating a date variable that is Todays Date
todays_date.weekday() # Using weekday function to return the weekday value of todays date
today = todays_date.weekday() # Creating a variable of the weekday variable that will be used to query key value pairs
print(today) # Validating Output

day_of_week = {
    '0': 'Weekday', #Monday
    '1': 'Weekday', #Tuesday
    '2': 'Weekday', #Wednesday
    '3': 'Weekday', #Thursday
    '4': 'Weekday', #Friday
    '5': 'Weekend', #Saturday
    '6': 'Weekend', #Sunday
} # Creating Key Value Pairs of of the weekday value and if its a weekend/ weekday
todays_weekday_is = day_of_week[str(today)] # Creating a variable that reads if its a weekday/weekend
print(todays_weekday_is) # Validating Output
if today < 4: # Printing validation statement
    print(f"Yes, unfortunately today is a {todays_weekday_is}. ") # Using an if statement, where if the day value is less then 4 it prints this statement
else: # Using an Else Statement
    print(f"It is the {todays_weekday_is}, yay!. ") # If the value is greater than 4 it prints this statement