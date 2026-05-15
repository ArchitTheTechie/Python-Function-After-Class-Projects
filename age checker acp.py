try:
    year = int(input("Enter the year of birth : "))
    if year <= 2026:
        age = 2026 - year
        print("Your age is : ", age)
    else:
        print("Year should be lesser than 2026")
except ValueError:
    print("Invalid Input")
finally:
    print("Execution completed successfully")