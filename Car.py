# class Car:
#
#     def __init__(self,color,price,type_car):
#         self.color=color
#         self.price=price
#         self.type_car=type_car
#
#     def display_car_details(self):
#         print("colos: {},price: {}, type of car: {} ".format(self.color,self.price,self.type_car))
#
# car01=Car("green","100","BMV")
# car02=Car("grey","200","Jeep")
# car03=Car("red","200","Jeep")
#
#
# car01.display_car_details()





class Car:
    def __init__(self,color,type,price):
        self.color=color
        self.type = type
        self.price=price


    def print_d(self):
        print("color is: {} type is: {} price is {}".format(self.color,self.type,self.price))




car1=Car('green','BMV',1000)
car2=Car('red','Jeep',2000)
car3=Car('black','scoda',3000)


car1.print_d()
car2.print_d()
car3.print_d()





























