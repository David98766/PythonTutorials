class Patient:
    def __init__(self, patient_id, name, age, gender, condition):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition
        self.admitted = False
        self.room_number = None

    def admit(self, room_number):
        if not self.admitted:
            self.admitted = True
            self.room_number = room_number
            print(f"{self.name} (ID: {self.patient_id}) has been admitted to room {self.room_number}.")
        else:
            print(f"{self.name} is already admitted.")

    def discharge(self):
        if self.admitted:
            self.admitted = False
            print(f"{self.name} (ID: {self.patient_id}) has been discharged.")
            self.room_number = None
        else:
            print(f"{self.name} is not currently admitted.")

    def show_details(self):
        status = "Admitted" if self.admitted else "Not Admitted"
        room_info = f"Room {self.room_number}" if self.admitted else "N/A"
        print(f"Patient Details:\n"
              f"ID: {self.patient_id}\n"
              f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Gender: {self.gender}\n"
              f"Condition: {self.condition}\n"
              f"Status: {status}\n"
              f"Room: {room_info}")

    def __str__(self):
        """Returns a user-friendly string representation of the patient."""
        status = "Admitted" if self.admitted else "Not Admitted"
        room_info = f"Room {self.room_number}" if self.admitted else "N/A"
        return (f"Patient {self.name} (ID: {self.patient_id}):\n"
                f"Age: {self.age}, Gender: {self.gender}, Condition: {self.condition}\n"
                f"Status: {status}, Room: {room_info}")

    def __repr__(self):
        """Returns a formal string representation of the patient, useful for debugging."""
        return (f"Patient(patient_id={self.patient_id}, name='{self.name}', age={self.age}, "
                f"gender='{self.gender}', condition='{self.condition}', "
                f"admitted={self.admitted}, room_number={self.room_number})")