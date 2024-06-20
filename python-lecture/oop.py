# 클래스에는 속성과 기능이 있음.
class Bike:

    #속성
    def __init__(self):
        self.color = 'black'
        self.weight = 3

    #기능(메서드)
    def drive(self):
        print('drive')

    def brake(self):
        print('brake')

    def gear(self):
        print('gear')

myBike = Bike()
friendBike = Bike()
hisBike = Bike()

print(myBike.color)
print(friendBike.color)

myBike.color = 'red'

print(myBike.color)
print(friendBike.color)




