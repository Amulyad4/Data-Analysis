def calculate_average(marks):
    return round(sum(marks) / len(marks), 2)

def performance_tracker(students):
    averages = {name: calculate_average(scores) for name, scores in students.items()}
    top_student = max(averages, key=averages.get)
    return averages, top_student

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
avg, top = performance_tracker(students)
print("Average Marks:", avg)
print("Top Performer:", top)
