class Parent:
    def print_info(self):
        print("This is the parent class")

class Child(Parent):
    def print_info(self):
        super().print_info()  # Call the print_info method from the Parent class
        print("This is the child class")


child1=Child()
child1.print_info()


class Parent:
    def print_detaills(self):
        print("I am parent")

class Child(Parent):
    def print_detaills(self):
        super().print_detaills()
        print("I am child")

child2=Child()
child2.print_detaills()



class MyParent:
    def __init__(self,name):
        self.name=name
        print("My name {}".format(name))

class MyChild(MyParent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("My name is {}, my age is {}".format(name,age))

child3 = MyChild("alexander",40)









