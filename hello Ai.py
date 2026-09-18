# Greet the user
print ("Hello! i am AI bot.What's your name? : ")

# Get user input
name = input()

#Respond to user
print("nice to meet you, {name}!")

#Ask user a question
print("How are you feelings today? {good/bad} : ")
mood = input().lower()

if mood == 'good':
    print("im glad to hear that!")
elif mood == "bad":
    print("i'm sorry to hear that i hope everything gets better soon.")
else:
    print("i see sometimes it's hard to put feelings into words.")

# end the conversation 
print("it was nice chatting with you {name}. Goodbye!")
