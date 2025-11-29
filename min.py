min=int(input("enter your minutes:"))
hours=min // 60 # shows the hours rounding down the minutes
minutes= min % 60 # shows the remaining minutes
print(f"it took {hours} hours and {minutes} minutes")