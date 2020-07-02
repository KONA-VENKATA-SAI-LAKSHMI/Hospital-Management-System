from .Config import db
from datetime import datetime

#UserStore
class UserStore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)

    def __repr__(self):
        return 'User ' + str(self.id)

#PatientDetails
class Patient_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    ssn_id = db.Column(db.String(45), nullable=False, unique=True)
    admission_date = db.Column(db.Date, nullable=False)
    bed_type = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(45), nullable=False)
    city = db.Column(db.String(45), nullable=False)
    state = db.Column(db.String(45), nullable=False)
    status = db.Column(db.String(45), nullable=False)
    #patient_test_id = db.Column(db.Integer, nullable=False)

    def __init__(self,name, age, ssn_id, admission_date, bed_type, address, city, state, status):
    
        self.name = name
        self.age = age
        self.ssn_id = ssn_id
        self.admission_date = admission_date
        self.bed_type = bed_type
        self.address = address
        self.city = city
        self.state = state
        self.status = status

    def __repr__(self):
        return 'Patient ' + str(self.id)

#Medicie
class Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medicine_name = db.Column(db.String(45), nullable=False)
    medicine_amount = db.Column(db.Integer, nullable=False)
    medicine_quantity = db.Column(db.Integer, nullable=False)
    #patient_medicine_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'Medicine ' + str(self.id)

#Patient_Medicine
class Patient_Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    medicine_id = db.Column(db.Integer, nullable=False)
    medicine_quantity = db.Column(db.Integer, nullable=False)
    #patient_details_ssn_id = db.Column(db.String(45), nullable=False)

#Diagnosis
class Diagnosis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String(45), nullable=False)
    test_amount = db.Column(db.Integer, nullable=False)
    #patient_test_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'Diagnosis ' + str(self.id)

#Patient_Test
class Patient_test(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   patient_id = db.Column(db.Integer, nullable=False)
   test_id =  db.Column(db.Integer, nullable=False)
   
