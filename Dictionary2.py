capitals ={"USA":"WAshigton D.C",
           "India":"New Delhi",
           "CHina":"Beijing",
           "Russia":"Moscow"}

print(dir(capitals))
print(help(capitals))
print(capitals.get("USA"))

if capitals.get("Japan"):
    print("That capital exist")
else:
    print("That capital does not exist")

capitals.update({"Germany":"Berlin"})
capitals.pop("China")

print(capitals)


keys = capitals.keys()
for key in capitals.keys():
    print(key)

values = capitals.values()
for value in values:
    print(value)

items = capitals.items()
for key,value in capitals.items():
    print(f"{key} : {value}")