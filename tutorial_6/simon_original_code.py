import tkinter as tk


class Mother:
    def __init__(self, name, address, age, ssn):
        self.name = name
        self.address = address
        self.age = age
        self.ssn = ssn
        self.pregnancy_details = []

    def add_pregnancy(self, pregnancy):
        self.pregnancy_details.append(pregnancy)


class Pregnancy:
    def __init__(self, lmp, num_babies, edd, systolic_bp, diastolic_bp):
        self.lmp = lmp
        self.num_babies = num_babies
        self.edd = edd
        self.systolic_bp = systolic_bp
        self.diastolic_bp = diastolic_bp


def register_mother():
    name = name_entry.get()
    address = address_entry.get()
    age = age_entry.get()
    ssn = ssn_entry.get()

    mother = Mother(name, address, age, ssn)
    mothers.append(mother)
    update_mother_listbox()


def add_pregnancy():
    selected_mother = mothers[mother_listbox.curselection()[0]]
    lmp = lmp_entry.get()
    num_babies = num_babies_entry.get()
    edd = edd_entry.get()
    systolic_bp = systolic_bp_entry.get()
    diastolic_bp = diastolic_bp_entry.get()

    pregnancy = Pregnancy(lmp, num_babies, edd, systolic_bp, diastolic_bp)
    selected_mother.add_pregnancy(pregnancy)
    update_pregnancy_listbox(selected_mother)


def update_mother_listbox():
    mother_listbox.delete(0, tk.END)
    for mother in mothers:
        mother_listbox.insert(tk.END, mother.name)


def update_pregnancy_listbox(mother):
    pregnancy_listbox.delete(0, tk.END)
    for pregnancy in mother.pregnancy_details:
        pregnancy_listbox.insert(tk.END, f'EDD: {pregnancy.edd}')


# Create the main GUI window
root = tk.Tk()
root.title("Mother and Pregnancy Registration")

# Create and configure input fields
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

ssn_label = tk.Label(root, text="SSN:")
ssn_label.pack()
ssn_entry = tk.Entry(root)
ssn_entry.pack()

# Create and configure buttons for mother registration
register_button = tk.Button(root, text="Register Mother", command=register_mother)
register_button.pack()

# Create and configure mother listbox
mother_listbox = tk.Listbox(root)
mother_listbox.pack()

# Create and configure input fields for pregnancy details
lmp_label = tk.Label(root, text="Last Known Menstrual Period:")
lmp_label.pack()
lmp_entry = tk.Entry(root)
lmp_entry.pack()

num_babies_label = tk.Label(root, text="Number of Babies Expected:")
num_babies_label.pack()
num_babies_entry = tk.Entry(root)
num_babies_entry.pack()

edd_label = tk.Label(root, text="Expected Date of Delivery:")
edd_label.pack()
edd_entry = tk.Entry(root)
edd_entry.pack()

systolic_bp_label = tk.Label(root, text="Systolic Blood Pressure:")
systolic_bp_label.pack()
systolic_bp_entry = tk.Entry(root)
systolic_bp_entry.pack()

diastolic_bp_label = tk.Label(root, text="Diastolic Blood Pressure:")
diastolic_bp_label.pack()
diastolic_bp_entry = tk.Entry(root)
diastolic_bp_entry.pack()

# Create and configure buttons for pregnancy details
add_pregnancy_button = tk.Button(root, text="Add Pregnancy Details", command=add_pregnancy)
add_pregnancy_button.pack()

# Create and configure pregnancy listbox
pregnancy_listbox = tk.Listbox(root)
pregnancy_listbox.pack()

# List to store registered mothers
mothers = []

# Start the GUI application
root.mainloop()
