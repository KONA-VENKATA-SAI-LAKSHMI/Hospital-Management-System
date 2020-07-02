from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Length, ValidationError
import datetime
from wtforms.fields.html5 import DateField
from .Models import UserStore, Patient_test, Patient_Medicine, Patient_details, Diagnosis, Medicine

#custom validator to check password while logging in
class pass_val(FlaskForm):
    def __init__(self,message):
        if not message:
            self.message="password criteria not met"
        self.message=message
    def __call__(self,form,field):
        nflag=0
        cflag=0
        upflag=0
        x=str(field.data)
        
        for i in x:
            if i==" ":
                raise ValidationError('Space not allowed in passwords')
                break
            if i.isnumeric():
                nflag+=1
            
            if (not i.isalnum()) and (not i ==' '):
                cflag+=1
            if i.isupper():
                upflag+=1
        if nflag==0 or cflag==0 or upflag==0:
            raise ValidationError(self.message)
        if len(x)!=10:
            raise ValidationError("Password length must be 10 charachters long")


    
# class for login page form
class Login_form(FlaskForm):
    username = StringField('username', validators=[DataRequired(),Length(min=8,message="ID should be atleast 8 characters long")])
    password = PasswordField('password', validators=[DataRequired(),Length(min=10,max=10,message=""),pass_val(message="password should have atleast 1 numeric and 1 special character and 1 uppercase and should be 10 charachters long")])
    submit = SubmitField('login')


#custom validator to check length of integer input fields
class check_length(FlaskForm):
    def __init__(self,message,min=-1,max=-1):
        self.min=min
        self.max=max
        if not message:
            self.message="input length must be between {} and {}".format(min,max)
        self.message=message
    def __call__(self,form,field):
        size=len(str(field.data))
        if Patient_details.query.filter_by(ssn_id=str(field.data)).first() != None:
            raise ValidationError("Patient with that id already exists!")
        if size<self.min or size>self.max:
            raise ValidationError(self.message)


# class for patient registration form
class Patient_create(FlaskForm):
    ssn_id = IntegerField('ssn id', validators=[DataRequired('please enter SSN ID in integer format'), check_length(message="id must be 9 digits long",min=9, max=9)])
    patient_name = StringField('patient name', validators=[ DataRequired('please enter name')])
    patient_age = IntegerField('patient age', validators=[ DataRequired('please enter age'), check_length(min=1, max=3, message="age should be 1-3 digits long")])
    date = DateField('enter date', format="%Y-%m-%d", validators=[ DataRequired('please enter date')], default=datetime.date.today())
    Type_of_bed = SelectField('bed type', choices=[('General ward', 'General ward'), ('Semi sharing', 'Semi sharing'), ('single room', 'single room')], validators=[DataRequired('select ward type')])
    address = StringField('enter address', validators=[DataRequired('enter the address')])
    submit= SubmitField('create')

    
#class for delete patient form
class Patient_delete(FlaskForm):
    patient_id = IntegerField('Patient id', validators=[DataRequired('please enter Patient ID in integer format')])  #check_length(message="id must be 9 digits long",min=9, max=9)])
    submit=SubmitField('Search')

class delete_result(FlaskForm):
    submit=SubmitField('delete')

