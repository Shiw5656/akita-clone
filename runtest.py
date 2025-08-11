import sys
import os


# Add student_workspace to Python path
sys.path.append(os.path.abspath('../student_workspace'))

import Student_worksapce.solution as a

# Define paths to CSV files
employees_path = os.path.abspath('./data/employees.csv')
attendance_path = os.path.abspath('./data/attendance.csv')

# Load data
employees_df = a.load_employees(employees_path)
attendance_df = a.load_attendance(attendance_path)

# Merge data
merged_df = a.merge_employees_attendance(employees_df, attendance_df)

# Run assessments
print("🏢 Total Hours Worked per Department:")
print(a.total_hours_per_department(merged_df), end="\n\n")

print("📊 Attendance Rate per Employee:")
print(a.attendance_rate(merged_df), end="\n\n")

print("📈 Hours Aggregation per Employee:")
print(a.hours_agg_per_employee(merged_df), end="\n\n")

print("🎓 Average Age by Job Role:")
print(a.avg_age_by_role(employees_df), end="\n\n")

print("🧾 Total Attendance Entries per Employee:")
print(a.total_attendance_entries(attendance_df), end="\n\n")

print("🏅 Top Performers by Hours Worked:")
print(a.top_performers(merged_df), end="\n\n")

print("📋 Average Attendance Rate per Department:")
print(a.avg_attendance_rate_per_department(merged_df), end="\n\n")

print("⏰ Late Arrival Ratio per Employee:")
print(a.late_arrival_ratio(merged_df), end="\n\n")