# ----------------------------------------------------
# Description:
# This program demonstrates object composition,
# validation, and relationships between multiple
# classes using a hospital management system.
# ----------------------------------------------------


class Patient:

    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age


class Doctor:

    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization


class Appointment:

    def __init__(self, patient, doctor, time):
        self.patient = patient
        self.doctor = doctor
        self.time = time

    def display(self):

        print(f"Patient: {self.patient.name}")
        print(f"Doctor: {self.doctor.name}")
        print(f"Specialization: {self.doctor.specialization}")
        print(f"Time: {self.time}")
        print("------------------------")


class Hospital:

    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):

        self.patients.append(patient)
        print("Patient registered successfully.")

    def add_doctor(self, doctor):

        self.doctors.append(doctor)
        print("Doctor added successfully.")

    def find_patient(self, patient_id):

        for patient in self.patients:

            if patient.patient_id == patient_id:
                return patient

        return None

    def find_doctor(self, doctor_id):

        for doctor in self.doctors:

            if doctor.doctor_id == doctor_id:
                return doctor

        return None

    def book_appointment(self, patient_id, doctor_id, time):

        patient = self.find_patient(patient_id)
        doctor = self.find_doctor(doctor_id)

        if patient is None:
            print("Patient not found.")
            return

        if doctor is None:
            print("Doctor not found.")
            return

        for appointment in self.appointments:

            if (
                    appointment.doctor.doctor_id == doctor_id
                    and appointment.time == time
            ):
                print("Doctor is already booked at this time.")
                return

        appointment = Appointment(
            patient,
            doctor,
            time
        )

        self.appointments.append(appointment)

        print("Appointment booked successfully.")

    def display_appointments(self):

        if not self.appointments:
            print("No appointments available.")
            return

        print("\n====== Appointments ======")

        for appointment in self.appointments:
            appointment.display()


hospital = Hospital()


while True:

    print("\n====== Hospital Management ======")
    print("1. Register Patient")
    print("2. Add Doctor")
    print("3. Book Appointment")
    print("4. Display Appointments")
    print("5. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:

        patient_id = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))

        if age > 0:

            patient = Patient(
                patient_id,
                name,
                age
            )

            hospital.add_patient(patient)

        else:

            print("Age must be greater than zero.")

    elif choice == 2:

        doctor_id = input("Enter doctor ID: ")
        name = input("Enter doctor name: ")
        specialization = input("Enter specialization: ")

        doctor = Doctor(
            doctor_id,
            name,
            specialization
        )

        hospital.add_doctor(doctor)

    elif choice == 3:

        patient_id = input("Enter patient ID: ")
        doctor_id = input("Enter doctor ID: ")
        time = input("Enter appointment time: ")

        hospital.book_appointment(
            patient_id,
            doctor_id,
            time
        )

    elif choice == 4:

        hospital.display_appointments()

    elif choice == 5:

        print("Exiting hospital management system.")
        break

    else:

        print("Invalid choice.")