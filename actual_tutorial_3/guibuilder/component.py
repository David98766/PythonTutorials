import os

_location = os.path.dirname(__file__)
import tkinter as tk
from actual_tutorial_3.model.patient import Patient

from actual_tutorial_3 import hospital

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black'
_tabfg2 = 'white'
_bgmode = 'light'
_tabbg1 = '#d9d9d9'
_tabbg2 = 'gray40'

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.patients = []  # Initialize as a list to store Patient instances

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.0, rely=0.0, height=31, width=604)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#ff0000")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(padx="200")
        self.Label1.configure(text='''Welcome to IS2208 Hospital''')

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.017, rely=0.111, relheight=0.856
                , relwidth=0.958)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#000000")

        self.Labelframe1 = tk.LabelFrame(self.Frame1)
        self.Labelframe1.place(relx=0.017, rely=0.026, relheight=0.273
                , relwidth=0.974)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="#000000")
        self.Labelframe1.configure(text='''Patient Input Form''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="#000000")

        self.Label2 = tk.Label(self.Labelframe1)
        self.Label2.place(relx=0.036, rely=0.476, height=21, width=84
                , bordermode='ignore')
        self.Label2.configure(activebackground="#d9d9d9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="#000000")
        self.Label2.configure(text='''Date of Birth:''')

        self.txtPatientGender = tk.Entry(self.Labelframe1)
        self.txtPatientGender.place(relx=0.661, rely=0.19, height=20
                , relwidth=0.15, bordermode='ignore')
        self.txtPatientGender.configure(background="white")
        self.txtPatientGender.configure(disabledforeground="#a3a3a3")
        self.txtPatientGender.configure(font="TkFixedFont")
        self.txtPatientGender.configure(foreground="#000000")
        self.txtPatientGender.configure(highlightbackground="#d9d9d9")
        self.txtPatientGender.configure(highlightcolor="#000000")
        self.txtPatientGender.configure(insertbackground="#000000")
        self.txtPatientGender.configure(selectbackground="#d9d9d9")
        self.txtPatientGender.configure(selectforeground="black")

        self.lblPatientGender = tk.Label(self.Labelframe1)
        self.lblPatientGender.place(relx=0.482, rely=0.19, height=21, width=94
                , bordermode='ignore')
        self.lblPatientGender.configure(activebackground="#d9d9d9")
        self.lblPatientGender.configure(activeforeground="black")
        self.lblPatientGender.configure(anchor='w')
        self.lblPatientGender.configure(background="#d9d9d9")
        self.lblPatientGender.configure(compound='left')
        self.lblPatientGender.configure(disabledforeground="#a3a3a3")
        self.lblPatientGender.configure(foreground="#000000")
        self.lblPatientGender.configure(highlightbackground="#d9d9d9")
        self.lblPatientGender.configure(highlightcolor="#000000")
        self.lblPatientGender.configure(text='''Patient Gender:''')

        self.Label3 = tk.Label(self.Labelframe1)
        self.Label3.place(relx=0.5, rely=0.476, height=21, width=64
                , bordermode='ignore')
        self.Label3.configure(activebackground="#d9d9d9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="#000000")
        self.Label3.configure(text='''Condition:''')

        self.txtCondition = tk.Entry(self.Labelframe1)
        self.txtCondition.place(relx=0.661, rely=0.476, height=20, relwidth=0.15
                , bordermode='ignore')
        self.txtCondition.configure(background="white")
        self.txtCondition.configure(disabledforeground="#a3a3a3")
        self.txtCondition.configure(font="TkFixedFont")
        self.txtCondition.configure(foreground="#000000")
        self.txtCondition.configure(highlightbackground="#d9d9d9")
        self.txtCondition.configure(highlightcolor="#000000")
        self.txtCondition.configure(insertbackground="#000000")
        self.txtCondition.configure(selectbackground="#d9d9d9")
        self.txtCondition.configure(selectforeground="black")

        self.lblPatientName = tk.Label(self.Labelframe1)
        self.lblPatientName.place(relx=0.036, rely=0.19, height=21, width=94
                , bordermode='ignore')
        self.lblPatientName.configure(activebackground="#d9d9d9")
        self.lblPatientName.configure(activeforeground="black")
        self.lblPatientName.configure(anchor='w')
        self.lblPatientName.configure(background="#d9d9d9")
        self.lblPatientName.configure(compound='left')
        self.lblPatientName.configure(disabledforeground="#a3a3a3")
        self.lblPatientName.configure(foreground="#000000")
        self.lblPatientName.configure(highlightbackground="#d9d9d9")
        self.lblPatientName.configure(highlightcolor="#000000")
        self.lblPatientName.configure(text='''Patient Name:''')

        self.txtPatientName = tk.Entry(self.Labelframe1)
        self.txtPatientName.place(relx=0.232, rely=0.19, height=20, relwidth=0.15
                , bordermode='ignore')
        self.txtPatientName.configure(background="white")
        self.txtPatientName.configure(disabledforeground="#a3a3a3")
        self.txtPatientName.configure(font="TkFixedFont")
        self.txtPatientName.configure(foreground="#000000")
        self.txtPatientName.configure(highlightbackground="#d9d9d9")
        self.txtPatientName.configure(highlightcolor="#000000")
        self.txtPatientName.configure(insertbackground="#000000")
        self.txtPatientName.configure(selectbackground="#d9d9d9")
        self.txtPatientName.configure(selectforeground="black")

        self.txtDateOfBirth = tk.Entry(self.Labelframe1)
        self.txtDateOfBirth.place(relx=0.232, rely=0.476, height=20
                , relwidth=0.15, bordermode='ignore')
        self.txtDateOfBirth.configure(background="white")
        self.txtDateOfBirth.configure(disabledforeground="#a3a3a3")
        self.txtDateOfBirth.configure(font="TkFixedFont")
        self.txtDateOfBirth.configure(foreground="#000000")
        self.txtDateOfBirth.configure(highlightbackground="#d9d9d9")
        self.txtDateOfBirth.configure(highlightcolor="#000000")
        self.txtDateOfBirth.configure(insertbackground="#000000")
        self.txtDateOfBirth.configure(selectbackground="#d9d9d9")
        self.txtDateOfBirth.configure(selectforeground="black")

        self.Button1 = tk.Button(self.Labelframe1)
        self.Button1 = tk.Button(self.Labelframe1, command=self.addPatient)  # Link to addPatient method
        self.Button1.place(relx=0.339, rely=0.762, height=26, width=147
                , bordermode='ignore')
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(text='''Add Patient''')

        self.Labelframe2 = tk.LabelFrame(self.Frame1)
        self.Labelframe2.place(relx=0.017, rely=0.312, relheight=0.221
                , relwidth=0.974)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="#000000")
        self.Labelframe2.configure(text='''Admission Form''')
        self.Labelframe2.configure(background="#d9d9d9")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="#000000")



        self.Label4 = tk.Label(self.Labelframe2)
        self.Label4.place(relx=0.464, rely=0.353, height=21, width=94
                , bordermode='ignore')
        self.Label4.configure(activebackground="#d9d9d9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="#000000")
        self.Label4.configure(text='''Room Number:''')

        self.txtRoomNumber = tk.Entry(self.Labelframe2)
        self.txtRoomNumber.place(relx=0.661, rely=0.353, height=20, relwidth=0.15
                , bordermode='ignore')
        self.txtRoomNumber.configure(background="white")
        self.txtRoomNumber.configure(disabledforeground="#a3a3a3")
        self.txtRoomNumber.configure(font="TkFixedFont")
        self.txtRoomNumber.configure(foreground="#000000")
        self.txtRoomNumber.configure(highlightbackground="#d9d9d9")
        self.txtRoomNumber.configure(highlightcolor="#000000")
        self.txtRoomNumber.configure(insertbackground="#000000")
        self.txtRoomNumber.configure(selectbackground="#d9d9d9")
        self.txtRoomNumber.configure(selectforeground="black")

        self.Button2 = tk.Button(self.Labelframe2)
        self.Button2 = tk.Button(self.Labelframe2, command=self.admitPatient)  # Link to addPatient method

        self.Button2.place(relx=0.339, rely=0.706, height=26, width=147
                , bordermode='ignore')
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="#000000")
        self.Button2.configure(text='''Admit Patient''')

        self.Labelframe3 = tk.LabelFrame(self.Frame1)
        self.Labelframe3.place(relx=0.017, rely=0.545, relheight=0.195
                , relwidth=0.974)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="#000000")
        self.Labelframe3.configure(text='''Discharge Form''')
        self.Labelframe3.configure(background="#d9d9d9")
        self.Labelframe3.configure(highlightbackground="#d9d9d9")
        self.Labelframe3.configure(highlightcolor="#000000")


        self.Button3 = tk.Button(self.Labelframe3)
        self.Button3 = tk.Button(self.Labelframe3, command=self.dischargePatient)  # Link to addPatient method
        self.Button3.place(relx=0.339, rely=0.667, height=26, width=137
                , bordermode='ignore')
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="black")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="#000000")
        self.Button3.configure(text='''Discharge Patient''')

        self.Labelframe4 = tk.LabelFrame(self.Frame1)
        self.Labelframe4.place(relx=0.017, rely=0.753, relheight=0.221
                , relwidth=0.974)
        self.Labelframe4.configure(relief='groove')
        self.Labelframe4.configure(foreground="#000000")
        self.Labelframe4.configure(text='''Patient Details Form''')
        self.Labelframe4.configure(background="#d9d9d9")
        self.Labelframe4.configure(highlightbackground="#d9d9d9")
        self.Labelframe4.configure(highlightcolor="#000000")


        self.Button4 = tk.Button(self.Labelframe4)
        self.Button4 = tk.Button(self.Labelframe4, command=self.retrievePatient)  # Link to addPatient method
        self.Button4.place(relx=0.339, rely=0.706, height=26, width=127
                , bordermode='ignore')
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="black")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="#000000")
        self.Button4.configure(text='''Search Patient''')

        self.lblPatientNameSearch = tk.Label(self.Labelframe4)
        self.lblPatientNameSearch.place(relx=0.607, rely=0.235, height=21
                , width=34, bordermode='ignore')
        self.lblPatientNameSearch.configure(activebackground="#d9d9d9")
        self.lblPatientNameSearch.configure(activeforeground="black")
        self.lblPatientNameSearch.configure(anchor='w')
        self.lblPatientNameSearch.configure(background="#d9d9d9")
        self.lblPatientNameSearch.configure(compound='left')
        self.lblPatientNameSearch.configure(disabledforeground="#a3a3a3")
        self.lblPatientNameSearch.configure(foreground="#000000")
        self.lblPatientNameSearch.configure(highlightbackground="#d9d9d9")
        self.lblPatientNameSearch.configure(highlightcolor="#000000")
        self.lblPatientNameSearch.configure(text='''Label''')

        self.lblDateOfBirthSearch = tk.Label(self.Labelframe4)
        self.lblDateOfBirthSearch.place(relx=0.607, rely=0.588, height=21
                , width=34, bordermode='ignore')
        self.lblDateOfBirthSearch.configure(activebackground="#d9d9d9")
        self.lblDateOfBirthSearch.configure(activeforeground="black")
        self.lblDateOfBirthSearch.configure(anchor='w')
        self.lblDateOfBirthSearch.configure(background="#d9d9d9")
        self.lblDateOfBirthSearch.configure(compound='left')
        self.lblDateOfBirthSearch.configure(disabledforeground="#a3a3a3")
        self.lblDateOfBirthSearch.configure(foreground="#000000")
        self.lblDateOfBirthSearch.configure(highlightbackground="#d9d9d9")
        self.lblDateOfBirthSearch.configure(highlightcolor="#000000")
        self.lblDateOfBirthSearch.configure(text='''Label''')

        self.lblGenderSearch = tk.Label(self.Labelframe4)
        self.lblGenderSearch.place(relx=0.804, rely=0.235, height=21, width=34
                , bordermode='ignore')
        self.lblGenderSearch.configure(activebackground="#d9d9d9")
        self.lblGenderSearch.configure(activeforeground="black")
        self.lblGenderSearch.configure(anchor='w')
        self.lblGenderSearch.configure(background="#d9d9d9")
        self.lblGenderSearch.configure(compound='left')
        self.lblGenderSearch.configure(disabledforeground="#a3a3a3")
        self.lblGenderSearch.configure(foreground="#000000")
        self.lblGenderSearch.configure(highlightbackground="#d9d9d9")
        self.lblGenderSearch.configure(highlightcolor="#000000")
        self.lblGenderSearch.configure(text='''Label''')

        self.lblConditionSearch = tk.Label(self.Labelframe4)
        self.lblConditionSearch.place(relx=0.804, rely=0.588, height=21, width=34
                , bordermode='ignore')
        self.lblConditionSearch.configure(activebackground="#d9d9d9")
        self.lblConditionSearch.configure(activeforeground="black")
        self.lblConditionSearch.configure(anchor='w')
        self.lblConditionSearch.configure(background="#d9d9d9")
        self.lblConditionSearch.configure(compound='left')
        self.lblConditionSearch.configure(disabledforeground="#a3a3a3")
        self.lblConditionSearch.configure(foreground="#000000")
        self.lblConditionSearch.configure(highlightbackground="#d9d9d9")
        self.lblConditionSearch.configure(highlightcolor="#000000")
        self.lblConditionSearch.configure(text='''Label''')

    def getPatientDetails(self):
        """Retrieve patient details from input fields and create a Patient instance."""
        name = self.txtPatientName.get()
        birthDate = self.txtDateOfBirth.get()  # Assuming this is a string for simplicity
        gender = self.txtPatientGender.get()
        condition = self.txtCondition.get()

        patientId = len(self.patients) + 1  # Simple ID generation
        newPatient = Patient(patientId, name, birthDate, gender, condition)

        self.patients.append(newPatient)
        print(f"Added Patient: {newPatient}")  # Optional logging

    def addPatient(self):
        """Method called when the Add Patient button is pressed."""
        self.getPatientDetails()  # Call the method to get patient details


    def admitPatient(self):
        roomNumber = self.txtRoomNumber.get()
        patientFirst = self.patients[0]
        Patient.admit(patientFirst, roomNumber)

    def dischargePatient(self):
        patientDischarge = self.patients[0]
        Patient.discharge(patientDischarge)

    def retrievePatient(self):
        patientSearch = self.patients[0]

        patientName = patientSearch.name
        patientBirthDate = patientSearch.age
        patientGender = patientSearch.gender
        patientCondition = patientSearch.condition

        self.lblPatientNameSearch.configure(text=patientName)
        self.lblDateOfBirthSearch.configure(text=patientBirthDate)
        self.lblGenderSearch.configure(text=patientGender)
        self.lblConditionSearch.configure(text=patientCondition)


def start_up():
    hospital.main()

if __name__ == '__main__':
    hospital.main()


