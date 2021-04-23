def grades_to_str(grades): 
    f = open("F:\\School\\SEM6\\testerP5\\testerP5\\")
    z=f.readlines()
    print(z)
    str_dict={}
    for i in range(len(z)):
        if i==0:
            str_dict["Name"]=z[i]
        if i==1:
            str_dict["Projects"]=z[i]
        if i==2:
            str_dict["Homeworks"]=z[i]
        if i==3:
            str_dict["zyBooks"]=z[i]
        if i==4:
            str_dict["Quizzes"]=z[i]
        if i==5:
            str_dict["Midterm"]=z[i]
        if i==6:
            str_dict["Final"]=z[i]
    return str_dict
# def projects_weighted_avg(grades):
# def homeworks_weighted_avg(grades):
# def zybooks_weighted_avg(grades):
# def quiz_weighted_avg(grades):
# def compute_final_grade(grades):
# def read_grades_file(filename):
# def write_grades_file(filename, grades):