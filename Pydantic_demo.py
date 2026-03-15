#Students management system
#Python is dynamically typed landuage
def create_student(name:str, age:int, college:str):
    if type(name)==str and type(age)==int and type(college)==str:
        print(name)
        print(age)
        print(college)
        print("Student created successfully")
    else:
        raise TypeError("Invalid input data")
create_student('Shaffe','40','MIT')
