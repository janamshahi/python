student_courses = {
    "Alice": ["Math", "Physics", "Math"],
    "janam": ["English", "Math", "English", "Physics"],
    "Charlie": ["Math", "Physics", "Biology"]
}
key = "janam"
value_to_count = "English"
if key in student_courses:
    count = student_courses[key].count(value_to_count)
    print(f"The value '{value_to_count}' appears {count} times for key '{key}'.")
else:
    print(f"Key '{key}' not found.")
