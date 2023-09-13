# class A:
#     x = 10
#     def display(self):
#         print(self.x)

# obj = A()
# obj.display()

class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name," ",self.age)

B = A("Aditi",24)
B.display()