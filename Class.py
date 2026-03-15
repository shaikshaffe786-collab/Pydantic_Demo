#Store data in an object = Model
#we are going to create a model class to store data
#Pydantic is a library that allows us to create models and validate data
#The class is applied everywhere in the code, and we can use it as a base class for our models
#pip install pydantic

from pydantic import BaseModel, Field

class Student(BaseModel):
    name:str
    age:int = Field(gt=0, le=200)
    college:str
    marks: float = Field(default=10.0,ge=0, le=100)

student_info = {'name' :'Shaffe', 'age' : '20', 'college' : 'MIT', 'marks' : '99.5'}

#Using this student_info dictionary, we can create an student
#student object is basically an objet that holds some values related to object
student = Student(**student_info) #** is used to unpack the dictionary and pass it to the Student class
#student becomes pydantic object
print(student.name)
print(student.age)
print(student.college)
print(student.marks)
        #By basic all the fields become mandatory in pydantic base model
        #we can also make some default values then use == beside objects of classes ex: College== 'MIT' then it will be default value for that field


