def grades_to_str(grades): 
    result=''
    key_lst,val_lst=[],[]

    for keys_str in grades.keys():
        key_lst.append(keys_str)
    for vals_str in grades.values():
        val_lst.append(vals_str)
    
    for i in range(len(grades)):
        result+=key_lst[i]+': '+str(val_lst[i])+'\n'
    return result

###############################
def projects_weighted_avg(grades):
    grades_project=grades["Projects"]
    project_scr=grades_project[:]
    project_scr.sort()
    low_vals=[]
    sum_low=0

    #adding small values to new list
    for i in range(2):
        low_vals.append(project_scr[i])

    #removing small value(s) and adding small values
    for j in range(len(low_vals)):
        project_scr.remove(low_vals[j])
        sum_low+=low_vals[j]

    avg_low=sum_low/len(low_vals)
    avg_total=(sum(project_scr)+avg_low)/(len(project_scr)+1)

    return avg_total

################################
def homeworks_weighted_avg(grades):
    grades_hw=grades["Homeworks"]
    hw_scr=grades_hw[:]
    hw_scr.sort()

    hw_scr.pop(0)
    avg_total=(sum(hw_scr))/(len(hw_scr))

    return avg_total

################################
def zybooks_weighted_avg(grades):
    grades_zy=grades["zyBooks"]
    zb_scr=grades_zy[:]
    zb_scr.sort()

    for i in range(2):
        zb_scr.pop(0)

    avg_total=(sum(zb_scr))/(len(zb_scr))

    return avg_total

##############################
def quiz_weighted_avg(grades):
    grades_quiz=grades["Quizzes"]
    quiz_scr=grades_quiz[:]
    quiz_scr.sort()

    for i in range(2):
        quiz_scr.pop(0)

    avg_total=(sum(quiz_scr))/(len(quiz_scr))

    return avg_total

############################
def compute_final_grade(grades):
    project_grade=projects_weighted_avg(grades)
    hw_grade=homeworks_weighted_avg(grades)
    zy_grade=zybooks_weighted_avg(grades)
    quiz_grade=quiz_weighted_avg(grades)

    if grades["Midterm"]<=grades["Final"]:
        grades["Midterm"]=grades["Final"]
    
    final_grade= (project_grade*0.4) + (hw_grade*0.07) + (zy_grade*0.05) + (quiz_grade*0.1) + (grades["Midterm"]*0.13) + (grades["Final"]*0.25)

    return final_grade

#################################
def read_grades_file(filename):
    f = open(filename)
    contents=f.readlines()
    category=["Name", "Projects", "Homeworks", "zyBooks","Quizzes","Midterm","Final"]
    grade_frmt={}

    for i in range(len(contents)):
        if i==0:
            contents[i]=contents[i].split('\n')
            contents[i].pop(i+1)
            contents[i]=contents[i][0]
            
        else:
            contents[i]=contents[i].split(' ')
    
    i=0

    for i in range(1,len(contents)):
        if (i!=len(contents)-2) and (i!=(len(contents)-1)):
            for j in range(len(contents[i])):
                if contents[i][j]!='\n':
                    contents[i][j]=float(contents[i][j])
                else:
                    contents[i].pop(j)      
        else:
            contents[i]=float(contents[i][0])

    i=0
    for i in range(len(category)):
        grade_frmt[category[i]]=contents[i]

    return grade_frmt

####################
def write_grades_file(filename, grades):
    val_lst=[]

    for vals_str in grades.values():
        val_lst.append(vals_str)

    x=''
    f = open(filename,'w')
    for i in range(len(val_lst)):
        if type(val_lst[i])!=list:
            if i<len(val_lst)-1:
                x+=str(val_lst[i])+'\n'
            else:
                x+=str(val_lst[i])
        else:
            lst_str=''
            for j in range(len(val_lst[i])):
                lst_str+=str(val_lst[i][j])+' '
            x+=lst_str+'\n'
    f.write(x)
