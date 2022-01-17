import cProfile
import re
offset = 5

while offset != 0:
    grade=int(input("Write the grade obtained by the student:"))
    offset = offset - 1
    if(grade >= 75):
        print("Grade 0")
    elif(grade >= 60 and grade <= 75):
        print("Grade A")
    elif(grade >= 50 and grade <= 59):
        print("Grade B")
    elif(grade >= 40 and grade <= 49):
        print("Grade C")
    else:
        print("Grade D")
        
cProfile.run('re.compile("foo|bar")')