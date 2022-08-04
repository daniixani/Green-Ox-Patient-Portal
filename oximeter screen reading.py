from datetime import datetime, date
from tkinter import Y
#This program is to have a health profile for oximeter readings and basic info
print ("Welcome to The Green Ox Portal!\n")
check_patient_exist = input("Are you registered with us? Y/N ")
#Quick loop to check if patient has profile to pull up their information or create new account
# Prompting for username and password
if check_patient_exist == 'Y' or check_patient_exist == 'y':
    patient_name = input("Enter your full name: ")
    password = input("Enter your birthday dd/mm/yyy: ")
# read in the file data
    filename = "patient_data.txt"
    with open('patient_data.txt') as f:
        data = f.read()

# while username exists in file
    while patient_name and password in data:
    #patient_name= input ("Please enter your full name: ")
        print (data)
        break
#while user does not exist
if check_patient_exist == 'N' or check_patient_exist == 'n':
    print ("We need to collect some basic information from you first. This will help us customize your file.")

#This will calculate age from birthday using date time
    birthday =  datetime.strptime(input("Enter your birthday dd/mm/yyyy: "), "%m/%d/%Y")
    def calculate_age(birth):
        today = date.today()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    age = calculate_age(birthday)

#This collects height and weight which will then be used to calculate BMI

    patient_height = float(input("How tall are you? cm: "))

    patient_weight = float(input("How much do you weigh? kg: "))

    patient_BMI = round(patient_weight / (patient_height/100)**2)

#We will save our patient information to a new file if not created
    #filename = "patient_data.txt"

    with open('patient_data.txt', "w") as filename:
        patient_data = [patient_name, birthday, age, patient_height, patient_weight, patient_BMI]
    f = open("patient_data.txt", "w")
    for d in patient_data:
        f.write(f"{d}\n")

    f.close()
else:
    exit
#Displays health data that was collected from user
view_data = input("Thanks for being so helpful! Would you like to see your health data? Y/N ")
if view_data == 'Y' or 'y':
    
    print ("Here is your health information: \n")
    print ("Name: " + patient_name)
    print ("\nAge: ", age)
    print ("\nHeight: " ,patient_height ,"cm")
    print ("\nWeight: ", patient_weight , " kg")
    print ("\nBody Mass Index: " , patient_BMI)
elif view_data == 'N' or 'n':
    print ("See you again, " + patient_name)
else:
    exit