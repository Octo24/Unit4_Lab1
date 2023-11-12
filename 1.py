class Student:
    # self refers to an instance in function 
    # to help python create objects?
    def __init__(self, name, id, address):
        self.name = name
        self.id = id
        self.address = address

# examples
dave = Student("Dave Doe", 1234, "21 houseland street")
me = Student("Octavian Hagi-Memet", 761057, "383 Hidden Ranch PL NW")

while True:
    try:
        # user input
        input_str = input("Input your name, student ID, and address [seperated by comma (,)]: ")
        input_list = input_str.split(",")
        input_list[1] = int(input_list[1])
        break
    except:
        print("Invalid pls input 3 appropriate values")

# asterisk unpacks list so it can be passed as 
# 3 seperate arguements into constructor function
input_student_info = Student(*input_list)

print(me.name)
print(me.id)
print(me.address)

print(input_student_info.name)
print(input_student_info.id)
print(input_student_info.address)