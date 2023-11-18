import sqlite3


conn = sqlite3.connect("school.db")
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT,
        enrollment_date TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
        teacher_id INTEGER PRIMARY KEY,
        name TEXT,
        hire_date TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        subject_id INTEGER PRIMARY KEY,
        name TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS classrooms (
        classroom_id INTEGER PRIMARY KEY,
        name TEXT,
        capacity INTEGER
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS classes (
        class_id INTEGER PRIMARY KEY,
        name TEXT,
        time TEXT,
        subject_id INTEGER,
        teacher_id INTEGER,
        FOREIGN KEY (subject_id) REFERENCES subjects (subject_id),
        FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        student_id INTEGER,
        class_id INTEGER,
        grade INTEGER,
        FOREIGN KEY (student_id) REFERENCES students (student_id),
        FOREIGN KEY (class_id) REFERENCES classes (class_id)
    )
""")


cursor.execute("INSERT INTO students (name, enrollment_date) VALUES (?, ?)", ("Anna Due", "2023-11-15"))
cursor.execute("INSERT INTO students (name, enrollment_date) VALUES (?, ?)", ("Kate Smith", "2023-10-21"))
cursor.execute("INSERT INTO teachers (name, hire_date) VALUES (?, ?)", ("Alice Johnson", "2023-09-05"))
cursor.execute("INSERT INTO subjects (name) VALUES (?)", ("Math",))
cursor.execute("INSERT INTO classrooms (name, capacity) VALUES (?, ?)", ("Room A101", 30))

conn.commit()


cursor.execute("SELECT student_id, name FROM students WHERE name=?", ("Anna Due",))
anna_student = cursor.fetchone()
cursor.execute("SELECT teacher_id, name FROM teachers WHERE name=?", ("Alice Johnson",))
alice_teacher = cursor.fetchone()
cursor.execute("SELECT subject_id, name FROM subjects WHERE name=?", ("Math",))
math_subject = cursor.fetchone()
cursor.execute("SELECT classroom_id, name FROM classrooms WHERE name=?", ("Room A101",))
room_a101 = cursor.fetchone()


cursor.execute("""
    INSERT INTO classes (name, time, subject_id, teacher_id)
    VALUES (?, ?, ?, ?)
""", ("Math 101", "9:00 AM", math_subject[0], alice_teacher[0]))

cursor.execute("""
    INSERT INTO grades (student_id, class_id, grade)
    VALUES (?, ?, ?)
""", (anna_student[0], 1, 95))

cursor.execute("""
    INSERT INTO grades (student_id, class_id, grade)
    VALUES (?, ?, ?)
""", (anna_student[0], 1, 88))

conn.commit()


print(f"Student: {anna_student[1]}, Enrolled Classes: Math 101")
print(f"Teacher: {alice_teacher[1]}, Teaches Class: Math 101")
print(f"Class: Math 101, Subject: {math_subject[1]}, Students: Anna Due")


cursor.close()
conn.close()
