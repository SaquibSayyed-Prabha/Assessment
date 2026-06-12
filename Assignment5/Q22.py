# Q22: Create a Hospital Management System using inheritance and encapsulation concepts.
print("Q22: Create a Hospital Management System using inheritance and encapsulation concepts.")
class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name


class Patient(Hospital):
    def __init__(self, hospital_name, patient_name, disease):
        super().__init__(hospital_name)
        self.__disease = disease
        self.patient_name = patient_name

    def get_disease(self):
        return self.__disease


p = Patient("City Hospital", "Ahmed", "Fever")

print("Hospital:", p.hospital_name)
print("Patient:", p.patient_name)
print("Disease:", p.get_disease())