class Student:
    def __init__(self, name, age, gender, major):
                    self.name = name
                    self.age = age
                    self.gender = gender
                    self.major = major

    def printStudentInfo(self):
        print('name : {0}'.format(self.name))
        print('age : {0}'.format(self.age))
        print('gender : {0}'.format(self.gender))
        print('major : {0}'.format(self.major))


gildong = Student('Hong Gildong',20, 'M', '컴퓨터 공학')
suji = Student('Lee Suji', 20, 'W', '연극 영화')

gildong.printStudentInfo()
suji.printStudentInfo()