total_height = 0
list_length = 0

for height in student_heights:
  total_height += height
 
for length in student_heights:
  list_length += 1

average = total_height / list_length
average = round(average)

print(average)