class cricket:
    def __init__(self,player,score):
        self.__player=player
        self.__score=score
    def info(self):
        print(f"cricket - player :{self.__player}, score: {self.__score}")
    def play(self):
        print(f"{self.__player} hits a 6")
    def get_score(self):
        return self.__score
    def set_score(self,new_score):
        if new_score>=0:
            self.__score=new_score
            print(f"score updated to {self.__score}")
        else:
            print("score cannot be negative")



class football:
    def __init__(self,player,score):
        self.__player=player
        self.__score=score
    def info(self):
        print(f"football - player :{self.__player}, score: {self.__score}")
    def play(self):
        print(f"{self.__player} scores a goal")
    def get_score(self):
        return self.__score
    def set_score(self,new_score):
        if new_score>=0:
            self.__score=new_score
            print(f"score updated to {self.__score}")
        else:
            print("score cannot be negative")


cricket1=cricket("imran khan",105)
football1=football("kaka",3)
print(" sports scoreboard \n")
for sport in(cricket1,football1):
    sport.info()
    sport.play()
    print()


print("direct change attenmpt")
cricket1.__score=300
print(f"score still shows : {cricket1.get_score()}")
cricket1.set_score(200)
print(cricket1.__score,"updated value using setter method")