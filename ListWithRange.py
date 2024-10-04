
l=[1,24,56,78,98,99]
D=[]

for num in l:
    if num % 2 ==0:

      D.append(num*2)
    else:
      print(D)
    print(D)


#using dictionary
student_marks ={"Anand":85,"Geetha":90,"kumar":78}
student_marks ={"Anand":85,"Geetha":90,"kumar":78}
marks =[25,30,45]

for name , marks in student_marks.items():
    print(f"{name} scored {marks}")

#using lists

student =["Anand","Geetha","kumar"]

marks =[85,90,78]

student_marks={} #we r displaying the index position with element using dictionary

#one method
for index,student in enumerate(student):
    student_marks[student] = marks[index]

#another method

for i in range(len(student)):
    student_marks[student[i]] = marks[i]

print(student_marks)