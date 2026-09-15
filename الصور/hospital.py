class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def view_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Patient(Person):
    def __init__(self, name, age, medical_record):
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self):
        print(f"Patient Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Medical Record: {self.medical_record}")


class Staff(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def view_info(self):
        print(f"Staff Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")


class Department:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.staff_members = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_staff(self, staff_member):
        self.staff_members.append(staff_member)

    def show_department(self):
        print(f"\nDepartment: {self.name}")

        print("\nPatients:")
        for patient in self.patients:
            patient.view_record()

        print("\nStaff:")
        for staff_member in self.staff_members:
            staff_member.view_info()


class Hospital:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def show_hospital(self):
        print("================================")
        print(f"Hospital: {self.name}")
        print(f"Location: {self.location}")

        for department in self.departments:
            department.show_department()

        print("================================")


# Main Program

hospital = Hospital("Al-Shifa Hospital", "Cairo, Egypt")

emergency = Department("Emergency")
cardiology = Department("Cardiology")

patient1 = Patient(
    "Ahmed Ali",
    30,
    "High fever and fatigue"
)

patient2 = Patient(
    "Mariam George",
    25,
    "Chest pain"
)

doctor = Staff(
    "Dr. John Samir",
    45,
    "Doctor"
)

nurse = Staff(
    "Sara Adel",
    29,
    "Nurse"
)

emergency.add_patient(patient1)
emergency.add_staff(doctor)

cardiology.add_patient(patient2)
cardiology.add_staff(doctor)
cardiology.add_staff(nurse)

hospital.add_department(emergency)
hospital.add_department(cardiology)

hospital.show_hospital()