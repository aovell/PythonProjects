#Alyn Ovell
#SampleDogKennelFiles

# Prompt user to enter dog information and save records in a text file
filename = "AOvell.txt"  
#open the file to write to it
with open("AOvell.txt", "w") as file:
    for i in range(5):
        dog_name = input("Enter dog name: ")
        owner_last_name = input("Enter owner last name: ")
        dog_age = input("Enter dog age: ")
        dog_weight = input("Enter dog weight: ")
        dog_breed = input("Enter dog breed: ")
        record = f"{dog_name}, {owner_last_name}, {dog_age}, {dog_weight}, {dog_breed}\n"
        file.write(record)

 # Read records from text file and determine dosage for heartworm medication
dosages = {11: 0.25, 15:0.25, 20:0.25, 22: 0.5, 33: 0.75, 44: 1.0, 55: 1.25, 66: 1.5, 77: 1.75, 88: 2.0, 90:2.0, 99: 2.25, 110: 2.5, 120:2.5, 121: 2.75, 132: 3, 149: 3.5, 175: 3.5}

#open text file to read
with open("AOvell.txt", "r") as file:
    records = file.readlines()
    for record in records:
      #splits the strings
        dog_name, owner_last_name, dog_age, dog_weight, dog_breed = record.split(", ")
      #gets the dosage in interger form
        dosage = dosages.get(int(dog_weight), 0)  # Default to 0 if dog weight is not in the dosages dictionary
        print(f"{dog_name}, owned by {owner_last_name}, needs {dosage} mL of heartworm medication.")




