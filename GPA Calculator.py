def score_converter():

    str_gpa = str(input("Please input your GPA:"))

    if str_gpa == "A+":
        int_gpa = float(4.5)
    elif str_gpa == "A":
        int_gpa = float(4)
    elif str_gpa == "B+":
        int_gpa = float(3.5)
    elif str_gpa == "B":
        int_gpa = float(3.0)
    elif str_gpa == "C+":
        int_gpa = float(2.5)
    elif str_gpa == "C":
        int_gpa = float(2.0)
    elif str_gpa == "D+":
        int_gpa = float(1.5)
    elif str_gpa == "D":
        int_gpa = float(1.0)    
    else:
        int_gpa = float(0)
    
    print(int_gpa)

# Test
score_converter()
