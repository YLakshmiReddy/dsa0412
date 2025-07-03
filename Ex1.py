import numpy as np


student_scores = np.array([
    [85, 90, 78, 92],  
    [76, 88, 84, 80],   
    [90, 92, 85, 88],   
    [70, 75, 80, 85]    
])

# Subject labels (order matters)
subjects = ['Math', 'Science', 'English', 'History']

# 1. Calculate average for each subject (i.e., column-wise mean)
subject_averages = np.mean(student_scores, axis=0)

# 2. Identify the subject with the highest average
max_avg_index = np.argmax(subject_averages)
highest_avg_subject = subjects[max_avg_index]

# 3. Print the results
print("Average scores per subject:")
for subject, avg in zip(subjects, subject_averages):
    print(f"{subject}: {avg:.2f}")

print(f"\nSubject with the highest average score: {highest_avg_subject}")
