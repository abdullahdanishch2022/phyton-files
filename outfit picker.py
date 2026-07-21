temprature=int(input("enter todays temprature in celcius"))

if temprature < 20:
    outfit="jacket"
    print("it is cold today")
    print("wear a outfit",outfit)
else:
    outfit="tshirt"
    print("it is warm today")
    print("wear a ",outfit)

is_raining=input("is it raining today? yes/no")

if is_raining=="yes":
    print("bring an umbrella")

wind_speed=int(input("enter the speed of the wind in km/h"))

if wind_speed > 30:
    needs_windbreaker="yes"
    print("it is windy today")
    print("wear a windbreaker over your",outfit)
else:
    needs_windbreaker="no"
    print("it is calm today")
    print("no windbreaker needed over your",outfit)

has_puddles=input("are there any puddles on the ground? yes/no")
if has_puddles=="yes":
    shoes="boots"
    print("the ground is wet")
    print("wear ",shoes)
else:
    shoes="sneakers"
    print("the ground is dry")
    print("wear ",shoes)

# PART 9: This message always prints, no matter what was chosen above

print("")

print("Weather check complete!")

# PART 10: Print the final outfit summary

print("===== WEATHER OUTFIT PICKER =====")

print("Temperature:", temprature)

print("Outfit Chosen:", outfit)

print("Raining:", is_raining)

print("Windbreaker Needed:", needs_windbreaker)

print("Shoes Chosen:", shoes)

print("===================================")
