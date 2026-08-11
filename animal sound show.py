from abc import ABC,abstractmethod



class Animal(ABC):
     def __init__(self,name,habitat):
          self.name=name
          self.habitat=habitat
     def display(self):
          print(f"name : :{self.name}   habitat : {self.habitat}")
     @abstractmethod
     def speak(self):
          pass 


class dog(Animal):
     def __init__(self,name,habitat,breed):
          super().__init__(name,habitat)
          self.breed=breed
     def speak(self):
          print(f"{self.name} ,{self.breed} says: woof woof")

class parrot(Animal):
     def __init__(self,name,habitat,phrase):
          super().__init__(name,habitat)
          self.phrase=phrase
     def speak(self):
          print(f"{self.name} ,says: {self.phrase}")




class lion(Animal):
     def __init__(self,name,habitat,pride):
          super().__init__(name,habitat)
          self.pride=pride
     def speak(self):
          print(f"{self.name} (Pride: {self.pride}) says: ROARRR!")


dog1=dog("bruno","house","labrador")
parrot1=parrot("meethu","jungle","hi how are you")
lion1=lion("simba","jungle","rocks")

print("=== Animal Sound Show ===\n")

for animal in [dog1, parrot1, lion1]:
    animal.display()
    animal.speak()
    print()

