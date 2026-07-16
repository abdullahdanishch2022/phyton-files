name=input ("enter your real name , Agent")
gadet=input("what is your favourite gadet")

agent_num=7
speed_rating=9.5
mission_count=12
height=1.6
is_active=True

print("Name:", name, "-> type:", type(name))

print("gadet:", gadet, "-> type:", type(gadet))
      
print("agent_num:",agent_num , "-> type:", type(agent_num))
      
print("speed_rating:", speed_rating, "-> type:", type(speed_rating))
      
print("mission_count:", mission_count, "-> type:", type(mission_count))
      
print("height:", height, "-> type:", type(height))
      
print("is_active:", is_active, "-> type:", type(is_active))

agent_number_text = str(agent_num)
mission_count_text=str(mission_count)
speed_rating_text=str(speed_rating)
status_text=str(is_active)

print("agent_number_text:", agent_number_text, "-> type:", type(agent_number_text))

print("mission_count_text:", mission_count_text, "-> type:", type(mission_count_text))
      
print("speed_rating_text:",speed_rating_text , "-> type:", type(speed_rating_text))
      
print("status_text:", status_text, "-> type:", type(status_text))

code1=name[0:3]
code2=name[-1]
code_name=code1+code2

reverse_gadet=gadet[::-1]


# PART 7: Join everything together to build the final badge message

badge_line_1 = "AGENT " + code_name.upper()

badge_line_2 = "ID: " + agent_number_text + " | MISSIONS: " + mission_count_text

badge_line_3 = "SPEED: " + speed_rating_text + " | ACTIVE: " + status_text

badge_line_4 = "SECRET GADGET CODE: " + reverse_gadet.upper()


# PART 8: Print the complete secret agent badge

print("")

print("===== SECRET AGENT BADGE =====")

print(badge_line_1)

print(badge_line_2)

print(badge_line_3)

print(badge_line_4)

print("===============================")