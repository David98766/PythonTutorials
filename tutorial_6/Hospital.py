import tkinter as tk
from tutorial_6.model.Mother import Mother
from tutorial_6.model.Pregnancy import Pregnancy

# Create the main GUI window
class Hospital(tk.Tk):

    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.title("Mother and Pregnancy Registration")

        # Create and configure input fields
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.address_label = tk.Label(self, text="Address:")
        self.address_label.pack()
        self.address_entry = tk.Entry(self)
        self.address_entry.pack()

        self.age_label = tk.Label(self, text="Age:")
        self.age_label.pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack()

        self.ssn_label = tk.Label(self, text="SSN:")
        self.ssn_label.pack()
        self.ssn_entry = tk.Entry(self)
        self.ssn_entry.pack()

        # Create and configure buttons for mother registration
        self.register_button = tk.Button(self, text="Register Mother", command=self.register_mother)
        self.register_button.pack()

        # Create and configure mother listbox
        self.mother_listbox = tk.Listbox(self)
        self.mother_listbox.pack()

        # Create and configure input fields for pregnancy details
        self.lmp_label = tk.Label(self, text="Last Known Menstrual Period:")
        self.lmp_label.pack()
        self.lmp_entry = tk.Entry(self)
        self.lmp_entry.pack()

        self.num_babies_label = tk.Label(self, text="Number of Babies Expected:")
        self.num_babies_label.pack()
        self.num_babies_entry = tk.Entry(self)
        self.num_babies_entry.pack()

        self.edd_label = tk.Label(self, text="Expected Date of Delivery:")
        self.edd_label.pack()
        self.edd_entry = tk.Entry(self)
        self.edd_entry.pack()

        self.systolic_bp_label = tk.Label(self, text="Systolic Blood Pressure:")
        self.systolic_bp_label.pack()
        self.systolic_bp_entry = tk.Entry(self)
        self.systolic_bp_entry.pack()

        self.diastolic_bp_label = tk.Label(self, text="Diastolic Blood Pressure:")
        self.diastolic_bp_label.pack()
        self.diastolic_bp_entry = tk.Entry(self)
        self.diastolic_bp_entry.pack()

        # Create and configure buttons for pregnancy details
        self.add_pregnancy_button = tk.Button(self, text="Add Pregnancy Details", command=self.add_pregnancy)
        self.add_pregnancy_button.pack()

        # Create and configure pregnancy listbox
        self.pregnancy_listbox = tk.Listbox(self)
        self.pregnancy_listbox.pack()

        # List to store registered mothers
        self.mothers = []

        # Start the GUI application
        self.mainloop()

    def register_mother(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        age = self.age_entry.get()
        ssn = self.ssn_entry.get()

        mother = Mother(name, address, age, ssn)
        self.mothers.append(mother)
        self.update_mother_listbox()

    def add_pregnancy(self):
        selected_mother = self.mothers[self.mother_listbox.curselection()[0]]
        lmp = self.lmp_entry.get()
        num_babies = self.num_babies_entry.get()
        edd = self.edd_entry.get()
        systolic_bp = self.systolic_bp_entry.get()
        diastolic_bp = self.diastolic_bp_entry.get()

        pregnancy = Pregnancy(lmp, num_babies, edd, systolic_bp, diastolic_bp)
        selected_mother.add_pregnancy(pregnancy)
        self.update_pregnancy_listbox(selected_mother)

    def update_mother_listbox(self):
        self.mother_listbox.delete(0, tk.END)
        for mother in self.mothers:
            self.mother_listbox.insert(tk.END, mother.name)

    def update_pregnancy_listbox(self, mother):
        self.pregnancy_listbox.delete(0, tk.END)
        for pregnancy in mother.pregnancy_details:
            self.pregnancy_listbox.insert(tk.END, f'EDD: {pregnancy.edd}')



# To start the application
if __name__ == "__main__":
    hospital_app = Hospital()
    hospital_app.start()
