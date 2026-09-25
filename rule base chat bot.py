import re,random
from colorama import fore,random

init(autoreset='true') 

destinations = {"beaches": ["bali","maldives","phuket"],
                "mountain":["swiss alps","rocky mountains","himalayas"],
                "cities": ["tokyo","Paris","new york"] }
jokes = ["why dont programmer like nature Too many bugs!",
         "why did the computer go to the doctor because it had a virus!",
         "why do travelers feel warm be cause of all their hot spots"]

def normalize_input(text):
    return re.sub(r"/s+", " ",text.strip().lower())

def recommend():
    print(Fore.CYAN + "travelbot: beaches,mountaion,cities?")
    prefrence = input(fore.Yellow + "you: ")
    prefrence = normalize_input(prefrence)

if __name__ == "__main__":
    chat()
