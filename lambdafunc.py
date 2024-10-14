# return a+b
# lambda functions are anonymous functions, which means they do not require a name. They are defined using the keyword lambda.

add = lambda a,b : a+b

print(add(1,2))

double = lambda a : a*2

print(double(5))


triple = lambda a,b,c : a*b+c

print(triple(1,2,3))


students=[ {"name":"vinay","mark":100},
   {"name":"chethan","mark":70},
   {"name":"virat","mark":80} ]

students.sort(key = lambda x: x["mark"],reverse=True)
print(students,end = "")

candidates = [ {
    "name" : "vade","mark":75},
    {"name" : "kiran","mark":95},
    {"name" : "kamal","mark":85}
]

candidates.sort(key = lambda x: x["mark"],reverse=True)

print(candidates,end = "")




