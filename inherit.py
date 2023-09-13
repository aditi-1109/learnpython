class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("Hi I Am ",self.name," and I am ",self.age," years old")
    


class Cat(Dog):

    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

    def speak_color(self):
        print("I am of ",self.color, " color")


cat = Cat('Aditi',23,"White")
cat.speak()
cat.speak_color()