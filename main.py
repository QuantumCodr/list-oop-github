# Patient Class

class Patient:
    def __init__(self, patient_id, name, age, gender, diagnosis):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

    def display_info(self):
        print("\n--Patient Information---")
        print(f"Patient_id: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Diagnosis: {self.diagnosis}")


# Hospital Class
class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print("Patient added successfully.")

    def display_patients(self):
        print("\n---- All Hospital Patients ----")
        print(f"\n---- {self.hospital_name} ----")

        if len(self.patients) == 0:
            print("No Patient Record Found.")
        else:
            for patient in self.patients:
                patient.display_info()
                print("----------------------")

# Patient Objects
patient1 = Patient(1, "Sharon", 20, "female", "Warm body")
patient2 = Patient(2, "korto", 20, "Male", "Krio")
patient3 = Patient(3, "Yabom", 20, "female", "Malaria")

# Hospital Object
hospital1 = Hospital("Life Care")

# Add patient to the hospital class
hospital1.add_patient(patient1)
hospital1.add_patient(patient2)
hospital1.add_patient(patient3)

# Display hospital records
hospital1.display_patients()