# match - case statement (switch): An alternative to using many 'elif' statements
#                               execute some code if a value matches a 'case'
#                               Benefits:cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
           return "sunday"
        case 2:
           return "monday"
        case 3:
           return "tuesday"
        case 4:
           return "wednesday"
        case 5:
           return "thursday"
        case 6:
           return "friday"
        case 7:
           return "saturday"
        case _:
           return "Invalid day number"
    
print(day_of_week(2))

#checking weekend or not

def is_weekend(day):
    match day:
        case "sunday" |"saturday":
           return True
        case "monday" |"tuesday" | "wednesday" | " thursday" | "friday" :
           return False
        case _:
           return "Invalid day number"
    
print(is_weekend("saturday"))