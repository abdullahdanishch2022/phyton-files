import colorama
from colorama import fore,Stylefrom Textblob import Textblob

coloroma.init()

print(f"{fore.CYAN} welcome to sentiment spy! {style.reser_all}")
user_name=input(f"{fore.MAGENTA} please enter your name {style.reset_all}").strip()
user_name= "mystery agent"

coversation_history = []
print(f"\n{fore.CYAN}hello, Agent{user_name}!")
print(f"type a sentence and i will analye your sentence with textblob and show you the sentiment")
print(f"type{fore.YELLOW}reset{Fore.CYAN},{fore.yellow}history{fore.CYAN}"f"or {fore.YELLOW}exit{fore.CYAN}to quit {style.reset_all}\n")

while True:
    user_input= input(f"{fore.GREEN}>> {style.reset_all}").strip()

    if not user_input:
        print(f"{fore.RED}please enter a text or a valid command.{style.reset_all}")
        