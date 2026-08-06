class student:
    grade=10
    name="muhammmad"
    def introduction(self):
        print("i am a student of grade",self.grade)
    def details(self):
        print("my name is",self.name)
        print("i study in grade",self.grade)
    

object1=student()
object1.introduction()
object1.details()
object2=student()
object2.introduction()
object2.details()