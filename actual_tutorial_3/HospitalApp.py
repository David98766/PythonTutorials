import tkinter as tk
from model.patient import Patient

# Create a list to store the patient has global access to the rest of the file
patients = []

def addPatient():
    # get the data from text fields, no seperate method for get data like last tutorial because we only need it for this function
     name = entry_name.get()
     age = entry_age.get()
     gender = entry_gender.get()
     condition = entry_condition.get()

    # generate an id for the patient just length of array add 1
     patient_id = len(patients) + 1
    # create a patient object to be stored
     new_patient = Patient(patient_id, name, age, gender, condition)
    #add the object to the array
     patients.append(new_patient)


def admitPatient():
    # get room number from the text field
    room_number = entry_room_number.get()

    # access the patient object in array position 0 which is first and only object in array
    first_patient = patients[0]
    # call the admit function for the patient from patient class
    first_patient.admit(room_number)

        # Clear room number field
    entry_room_number.delete(0, tk.END)

def dischargePatient():
    # access the one and only patient in the patient array
     first_patient = patients[0]
    # call discharge on the patient object
     first_patient.discharge()

def retrievePatient():
    # Show details of the first patient
      first_patient = patients[0]
     # Call the sho_details function from patient class
      details = first_patient.show_details()

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_condition.delete(0, tk.END)



window = tk.Tk()
window.geometry("500x500")
window.title("Python Hospital App")

# Labels and Entry fields
tk.Label(window, text="Patient Name:").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Age:").pack()
entry_age = tk.Entry(window)
entry_age.pack()

tk.Label(window, text="Gender:").pack()
entry_gender = tk.Entry(window)
entry_gender.pack()

tk.Label(window, text="Condition:").pack()
entry_condition = tk.Entry(window)
entry_condition.pack()

tk.Label(window, text="Room Number:").pack()
entry_room_number = tk.Entry(window)
entry_room_number.pack()

# Create Buttons and assign them functions from above
tk.Button(window, text="Add Patient", command=addPatient).pack()
tk.Button(window, text="Admit Patient", command=admitPatient).pack()
tk.Button(window, text="Discharge Patient", command=dischargePatient).pack()
tk.Button(window, text="Show Patient Details", command=retrievePatient).pack()
tk.Button(window, text="Clear all", command=clear_fields).pack()


# Run the application
window.mainloop()