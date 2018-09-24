
import datetime

class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split()[-1]

    def getLastName(self):
        return self.lastName

    def setBirthday(self, year, month, day):
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        if self.birthday == None:
            raise ValueError('Birthday not available')
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name

class MITPerson(Person):
    nextEmpIdNum = 55 # Class variable: Employee counter-

    def __init__(self, name):
        Person.__init__(self, name) # Syntax- Initialize Person constructor
        # Syntax- Call another instance method
        self.empIdNum = self._assignEmpIdNum()

    def _assignEmpIdNum(self): # Leading underscore: This is not part of API.
        empIDNum = MITPerson.nextEmpIdNum # Note syntax- for calling a class variable
        MITPerson.nextEmpIdNum += 1
        return empIDNum

    def getIdNum(self):
        return self.empIdNum

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

class Grad(Student):
    pass

class TransferStudent(Student):
    pass

class Grade(object):
    """ Map students to a list of grades """
    def __init__(self):
        self.students = [] # List of student objects
        self.grades   = {} # Map idNum -> list of grades
        self.isSorted = True

    def addStudent(self, student):
        """ Assumes student is of type Student.  Add student to the grade book """
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """ Grade should be a float.  Add grade to the list of student grades """
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        """ Return a list of grades for student """
        try:
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        """ Return a list of students in the grade book """
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]  # Return a *copy* of list of students

    def __str__(self):
        for s in self.students:
            print s
        return 'Hello'


def gradeReport(course):
    """ Course should be of type Grade """
    report = []
    for student in course.allStudents():
        total = 0.0
        numGrades = 0
        for g in course.getGrades(student):
            total += g
            numGrades += 1
        try:
            average = total/numGrades
            report.append(str(student) + "'s average grade is: " + str(average))
        except ZeroDivisionError:
            report.append(str(student)+ ' has no grades')
    return '\n'.join(report)

def isStudent(obj):
    return isinstance(obj, Student)

# ====================================================

ug1 = UG('Jane Doe'   , 2014)
ug2 = UG('John Doe'   , 2015)
ug3 = UG('David Henry', 2003)
g1  = Grad('John Henry')
g2  = Grad('George Steinbrenner')

six00 = Grade()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)

for s in six00.allStudents():
    six00.addGrade(s, 75)
six00.addGrade(g1, 100)
six00.addGrade(g2, 25)

six00.addStudent(ug3)
print 'Hello, world!'
