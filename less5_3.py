students = {
    'Alice': {'Math', 'History'},
    'Bob': {'Physics', 'Math', 'Biology'},
    'Katya': {'Physics', 'Biology', 'Geography'},
    'Anna': {'Biology', 'History', 'Math', 'Geography'},
    'Mykyta': {'Biology', 'Math', 'History'},
}


def database_query(student1, student2):
    courses1 = None
    courses2 = None

    for k, v in students.items():
        if k == student1:
            courses1 = v

        elif k == student2:
            courses2 = v

    result = list(courses1.intersection(courses2))

    print(f'A list of courses that {student1} and {student2} are taking: {result}')


database_query('Bob', 'Anna')
