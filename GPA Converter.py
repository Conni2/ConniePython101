# 2nd project - GPA Converter
# Description: Convert alphabet scale GPA into 4.5 scale GPA | Purpose: To practice if statements
# Further improvement: Add while and for statement for receiving values and add to the list

def score_converter(str_gpa):

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
    
    return(int_gpa)


gpa_scale = []
gpa = []

while True:
    str_gpa = str(input("GPA in Alphabet scale:"))
    if str_gpa == "DONE":
        break
    gpa_scale.append(str_gpa)

print("GPA in Alphabet scale:" + str(gpa_scale))

for i in range(len(gpa_scale)):
    numbers = score_converter(gpa_scale[i])
    gpa.append(numbers)

print("GPA in total 4.5 scale:"+ str(gpa))