print ("Welcome!, please enter the project score out of 72, and the exam score out of 112 in the spaces provided")
x = int(input("project_score:"))
y = int(input("exam_score:"))
project_percentage = x/72*100
exam_percentage = y/112*100
overall_average = x/100*60+y/100*40


print ("percentage score for project:", project_percentage)
print ("percentage score for exam:", exam_percentage)
print ("overall percentage:", overall_average)


if overall_average <= 49: print ("final grade: fail")
elif overall_average >=50 and overall_average <= 59: print ("final grade: D")
elif overall_average >=60 and overall_average <= 69: print ("final grade: C")
elif overall_average >=70 and overall_average <= 79: print ("final grade: B")
elif overall_average >=80: print ("final grade: A")