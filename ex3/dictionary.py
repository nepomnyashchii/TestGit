# ages = {"Dave": 24, "Mary": 42, "John": 58}
# print(ages["Dave"])
# print(ages["Mary"])


# student={"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(student)

# student={"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(student["name"])

# student={"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(student["age"])

# student={"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(student["courses"])

# student={1: "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(student[1])

# student={1: "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(student.get("name"))

# student={1: "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(student.get(1))

# student={1: "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(student.get(1))

# student={"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(student.get("phone", "Not Found"))

# student={"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# student["phone"]= "555-55-55"
# print(student.get("phone", "Not Found"))


# student={"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# student["phone"]= "555-55-55"
# print(student)

# student={"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# student["phone"]= "555-55-55"
# print(student)

# student={"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# student.update({"name": "Jane", "age":26, "phone":"555-55-55"})
# print(student)

# student={"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# del student["name"]
# print(student)

# student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# age = student.pop("age")
# print(student)
# print("age")

# student={"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(len(student))

# student={"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(student.keys)

# student={"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(student.values())

# student={"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(student.items())

# student={"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# for key in student:
#     print(key)

student={"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
for key, value in student.items():
    print(key, value)
