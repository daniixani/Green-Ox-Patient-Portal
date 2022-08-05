from datetime import datetime, date
from patient import Patient


print("Welcome to The Green Ox Portal!\n")

patient = Patient(name=input("Please type your full name to get started: "))

try:  # attempt to read pation from file
    patient.read()
except:  # if reading patient from files fails, ask to create account
    should_create_account_input = input(
        "Patient not found. Would you like to create an account? (y/n): ")
    should_create_account = should_create_account_input == "Y" or should_create_account_input == "y"

    if should_create_account:
        patient.birthday = input("Please type your birthday (mm/dd/yyyy): ")

        patient.save()
    else:
        exit()


print("Here is your data:")
print(patient)
