def countStudents(students, sandwiches):
    count_0 = students.count(0)
    count_1 = students.count(1)
  
  for s in sandwiches:
    if s == 0:
        if count_0 > 0:
            count_0 -= 1
        else :
            return count_0 + count_1   
    elif s == 1:
        if count_1 > 0:
            count_1 -= 1
        else:
            return count_0 + count_1

return count_0 + count_1

# Example test run ke liye:
print(countStudents([1,1,0,0], [0,1,0,1]))
