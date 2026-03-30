data = {
    "name": "Janam",
    "age": 21,
    "course": "",
    "address": None,
    "hobbies": [],
    "skills": {}
}
cleaned_data = {k: v for k, v in data.items() if v not in (None, "", [], {})}
print("Dictionary after dropping empty items:")
print(cleaned_data)
