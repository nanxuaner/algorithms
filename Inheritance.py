# class SchoolMember:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('(Initialized SchoolMember: {self.name})'.format(self = self))
#
#     def tell(self):
#         print ('Name: {self.name},  Age: {self.age}'.format(self = self))
#
# class Teacher(SchoolMember):
#     def __init__(self, name, age, salary):
#         SchoolMember.__init__(self, name, age)
#         self.salary = salary
#         print ('Initialized Teacher: {self.name}'.format(self = self))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print ('Salary: {self.salary}'.format(self = self))
#
# class Student(SchoolMember):
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.marks = marks
#         print ('Initialized: %s' %(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print ('Marks: %d' %(self.marks))
#
# t = Teacher("Xin", 30, 30000)
# s = Student("Anna", 3, 100)
#
# members = [t, s]
# for member in members:
#     member.tell()


# class SchoolMember:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("Initialized School Member: %s" %(self.name))
#
#     def tell(self):
#         print ("Name: %s, Age: %d" %(self.name, self.age))
#
# class Teacher(SchoolMember):
#     def __init__(self, name, age, salary):
#         SchoolMember.__init__(self, name, age)
#         self.salary = salary
#         print ("Initialized Teacher: %s" %(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print ("Salary: %d" %(self.salary))
#
# class Student(SchoolMember):
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.marks = marks
#         print ("Initialized Student: %s" %(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print ("Mark is %d" %(self.marks))
#
# t = Teacher("Xin", 30, 30000)
# s = Student("Yuan", 29, 80)
#
# # m = SchoolMember("Xin", 30)
# # m = t
# members = [t, s]
# for member in members:
#     member.tell()

class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print ("Initialized School Member: %s" %(self.name))

    def tell(self):
        print ("Name: %s, Age: %d." %(self.name, self.age))

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print ("Initialized Teacher: %s" %(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print ("Salary: %d" %(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print ("Initialized Student: %s" %(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print ("Mark is: %d" %(self.marks))

t = Teacher("Xin", 30, 50000)
s = Student("Anna", 29, 80)

members = [t,s]
for member in members:
    member.tell()