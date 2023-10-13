import matplotlib.pyplot as plt
subjects = ["Math", "Science", "History", "English", "Art"]
marks = [90, 85, 70, 78, 92]
# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=140, colors=['blue', 'green', 'orange', 'red', 'purple'])
plt.title("Subject-wise Marks Distribution")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart
plt.show()
