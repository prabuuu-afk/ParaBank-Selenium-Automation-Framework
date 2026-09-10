class Dog:
    def __init__(self, name,age=1):
        self.name = name          # stored on THIS dog
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")
    def year(self):
        print(f"{self.name} is now {self.age}!")
        self.age+=1

my_dog = Dog("Rex")     # instantiation — __init__ runs, self.name = "Rex"
my_dog.bark()             # → "Rex says Woof!"

your_dog = Dog("Max")   # a SEPARATE object, its own self.name = "Max"
your_dog.bark()           # → "Max says Woof!"

a=Dog("Jimmy",2)
a.year()

b=Dog("tom")
b.year()

a.year()
b.year()