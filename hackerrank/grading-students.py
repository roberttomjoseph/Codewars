def gradingStudents(grades):
    for i, grade in enumerate(grades):
        if grade > 39:
            if str(grade)[1] == '8':
                grades[i] += 2
            elif str(grade)[1] == '9':
                grades[i] += 1
            elif str(grade)[1] == '3':
                grades[i] += 2
            elif str(grade)[1] == '4':
                grades[i] += 1
    return grades
            


gradingStudents([18, 53, 99])