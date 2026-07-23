print("=== Smart School Day Planner ===")

print("Answer 3 quick questions and I will plan your day!\n")

day=input("what day is it? (Monday to sunday) : ").strip().lower()
weather=input("what is the weather?(sunny,rainy,cloudy)  : ").strip().lower()
homework=input("is your homework done?(yes/no)  : ").strip().lower()


print("")
print("")
print(f"=== Your Plan for {day} ===")

print("-" * 35)

if day in("saturday","sunday"):
    print("day type :weekend-enjoy your free time")
elif day=="monday":
    print("day type :first day of the week.pack your weekly planner")
elif day=="friday":
    print("day type :last school day. return library books today")
elif day in("tuesday","wednesday","thursday"):
    print("regular school day, stay focused")
else:
    print("day type: day is not recognized,check spelling")

if weather=="sunny" and homework=="yes":
    print("after school head to the park,great weather and homework is done")
if weather=="rainy" or weather=="cloudy":
    print("weather tip: pack your umbrella it may rain outside")
if not(homework=="yes"):
    print("homework:not done finish it before going out")

if weather=="rainy" and not(homework=="yes"):
    print("best plan:stay in,finish homework")
elif weather=="sunny" and homework=="yes" and not(day in("saturday","sunday")):
    print("best plan:all set for school day")
elif day in("saturday","sunday") and weather=="sunny":
    print("best plan: perfect weather lets head outside")
else:

    print("Best plan : Take it one step at a time - you have got this!")

print()

print("Plan complete! Have a wonderful day!")