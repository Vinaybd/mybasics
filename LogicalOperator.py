#logical opertaor = evaluates multiple conditions(or,and,not)
#      or = at least one condition must be true
#      and = both conditions must be true
#      not = inverts the condition(not false,not true)

# temp = -1
# is_raining = False

# if temp > 35 or temp < 0 or is_raining :
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")


# and

temp = 38
is_sunny = True

if temp <= 28 and is_sunny:
    print("The weather is too hot")
elif temp > 28 and not is_sunny:
    print("The  weather is still hot")
elif temp >= 28 and not is_sunny:
    print("The weather is hot outside")
elif temp <=0 and not is_sunny:
    print("The weather is cool outside")
elif temp>30 and not is_sunny:
    print("The weather is hot and cloudy sometimes")
elif temp>35 and is_sunny:
    print("Defenetly the weather is sunny")
elif 28>temp>0 and not is_sunny:
    print("The weather is cool and sunny")
    print("Its a clody day")
else:
    print("The weather is not suitable for outdoor activities")

