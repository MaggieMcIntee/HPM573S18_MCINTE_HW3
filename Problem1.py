
class Patient:
    """base class"""
    def __init__(self, name):
        self.name = name

    def discharge(self):
        """
        :returns #abstract method to be overridden in derived classes expected cost of this patient """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

class EmergencyPatient (Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
        self.cost=1000 # cost of all emergency patients

    def discharge(self):
        """
        :return: the cost of a patient being discharged after being in the ER
        """
        print(self.name, 'EmergencyPatient')

class HospitalizedPatient (Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
        self.cost = 2000 #cost of all hospitalized patients

    def discharge(self):
        """
        :return: # cost of a patient being discharged after being hospitalized
        """
        print(self.name, 'HospitalizedPatient')

class Hospital:
    def __init__(self): #creates a brand new hospital
        self.patients = []
        self.cost=0

    def admit(self, patients):
        self.patients.append(patients) #allows us to add patients 1 by 1 to the intital list

    def discharge_all (self):
        for patients in self.patients:
            patients.discharge() #call on the discharge function of the object patient in this list from the previous classes
            self.cost += patients.cost

    def get_total_cost (self):
        """ returns the total costs of the hospital for that day"""
        return self.cost

# create Patients
P1 = EmergencyPatient('P1')
P2 = EmergencyPatient('P2')
P3 = EmergencyPatient('P3')
P4 = HospitalizedPatient ('P4')
P5 = HospitalizedPatient ('P5')

#create our hospital
H1 = Hospital()
H1.admit(P1) # admits our first patient to out hospital
H1.admit(P2)
H1.admit(P3)
H1.admit(P4)
H1.admit(P5)
H1.discharge_all()

# return the total operating cost of the hospital for this day
print(H1.get_total_cost())