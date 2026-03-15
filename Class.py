#Store data in an object = Model
#we are going to create a model class to store data
#Pydantic is a library that allows us to create models and validate data
#The class is applied everywhere in the code, and we can use it as a base class for our models
#pip install pydantic
#Type validation in pydantic  - validating the data types of attributes
#Field validation in pydantic - validating the values of fields
#Ex field validation - <= max length , email validation...etc
#Gt=greater than
#LE=less than or equal to
#lt=less than
#email should contain @masai.com (These customer validation which requires to validate the formatm where it is correct format or not, example PAN entry, aadhar card no entry etc)
#Computed fields



from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator, computed_field

class Student(BaseModel):
    name:str = Field(max_length=50) #max_length is used to validate the length of the string
    email:EmailStr =Field(description="Provide a valid email address of the student")
    age:int = Field(gt=0, le=200)   
    college:str
    marks: float = Field(default=0.0,ge=0, le=100)



    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
      #abc@masai.com

      domain_name = value.split('@')[1] #[abc, masai.com]    
      if domain_name != 'masai.com':    
        raise ValueError('Email must be a valid masai.com email address')
      return value 
    
    @field_validator('college')
    @classmethod
    def trasform_college_name_upper_case(cls, value):
       return value.lower() #it will transform the college name to upper case
    

    @field_validator('age') #default mode is after, it means that the validation will be done after the data is converted to the correct type, but if we want to validate the data before it is converted to the correct type, we can use mode='before'
    @classmethod
    def validate_age(cls, value):
       if value < 0 and value > 100:
            raise ValueError("Invalid age provided")
       return value
    
    @model_validator(mode='after')
    @classmethod
    def validate__contact_number(cls, model):
       if model.age <18 and 'Fathers' not in model.emergency_contact_number:
          raise ValueError("if age of student is less than 18 then fathers contact number is mandatory")
       
       return model

    @computed_field
    @property
    def percentage(self) -> float:
        return self.marks 
    
    @model_validator(mode='after')
    @classmethod
    def validate_marks(cls, model):
        if model.marks < 0 or model.marks > 100:
            raise ValueError("% should be between 0 and 100")
        return model



student_info = {'name' :'Shaffe', 'age' : '18', 'college' : 'MASAI', 'marks' : '89', 'email' : 'Shaffe@masai.com'}

#Using this student_info dictionary, we can create an student
#student object is basically an objet that holds some values related to object
student = Student(**student_info) #** is used to unpack the dictionary and pass it to the Student class
#student becomes pydantic object
print(student.name)
print(student.age)
print(student.college)
print(student.marks)
print(student.email)
print(student.percentage) #computed field

        #By basic all the fields become mandatory in pydantic base model
        #we can also make some default values then use == beside objects of classes ex: College== 'MIT' then it will be default value for that field


