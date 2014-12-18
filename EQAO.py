
class Studentsorter(object):

    def __init__(self):

        self.fullst = []


    def class_adder(self, stulst):
        self.fullst.append(stulst)

    def data_adder(self, studata, year):
        for stuclass in self.fullst:
            if stuclass.grade == year:
                for student in stuclass.stulst:
                    for line in studata:
                        if student.OENnum == line[0]:
                            student.grd3mark = line[-1]

            else:
                gradelst = StudentList("Grade 9")

                for line in studata:
                    newstu = Student(line[0])

                    newstu.grd6set(line[-1])

                    gradelst.stuadd(newstu)

                self.fullst.append(gradelst)

    def lstsort(self):
        newlst = sorted(self.stulist)

    def table_format(self, table):

        for line in data6:

            line = line.split(",")
            sub = line[-1][:-1]
            line = line[:-1]
            line.append(sub)
            templst.append(line)

        data6 = templst[:-1]

        return(data6)

class StudentList(object):

    def __init__(self, grade):

        self.grade = grade

        self.stulst = []


    def stuadd(self, student):

        self.stulst.append(student)



class Student(object):

    def __init__(self, OENnum):

        self.OENnum = OENnum

        self.grd3mark = 0
        self.grd6mark = 0
        self.grd9diag = 0

    def grd3set(self, mark):

        self.grd3mark = mark


    def grd6set(self, mark):

        self.grd6mark = mark


    def grd9set(self, mark):

        self.grd9mark = mark


# Ask user for file input


#grd3 = str(input("Enter the filename for Grade 3 EQAO data:   "))
#grd6 = str(input("Enter the filename for Grade 6 EQAO data:   "))
#grd9diag = str(input("Enter the filename for Grade 9 diagnostic data:   "))

classlst = Studentsorter()

grd6 = "Fake_EQAO_gr6.csv"


# Open data file

#infile3 = open(grd3, "r")
infile6 = open(grd6, "r")
#infile9diag = open(grd9diag, "r")




# Import data from files

#data3 = infile3.readlines()
data6 = infile6.readlines()
data6 = sorted(data6)

templst= []


for line in data6:

    line = line.split(",")
    sub = line[-1][:-1]
    line = line[:-1]
    line.append(sub)
    templst.append(line)

data6 = templst[:-1]

gradelst = StudentList("Grade 9")

for line in data6:
    newstu = Student(line[0])

    newstu.grd6set(line[-1])

    gradelst.stuadd(newstu)


classlst.class_adder(gradelst)



data3 = infile6.readlines()
grade = "Grade 9"

for line in data3:

    line = line.split(",")
    sub = line[-1][:-1]
    line = line[:-1]
    line.append(sub)
    templst.append(line)

data3 = (templst[:-1])


classlst.data_adder(data3, grade)

"""for x in classlst.fullst:
    for y in x.stulst:
        print(y.grd6mark)
        print(y.grd3mark)"""

for x in range(0, len(data3)):
    print(data3[x][-1])
    print(data6[x][-1])
