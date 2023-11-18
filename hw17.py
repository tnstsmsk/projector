from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import sqlalchemy.ext.declarative


engine = create_engine("sqlite:///school.db")
Session = sessionmaker(bind=engine)
session = Session()


Base = sqlalchemy.orm.declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    subjects = relationship("Subject", secondary="student_subject", back_populates="students")


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship("Student", secondary="student_subject", back_populates="subjects")


class StudentSubject(Base):
    __tablename__ = "student_subject"

    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"), primary_key=True)


Base.metadata.create_all(engine)


student1 = Student(name="Alice")
student2 = Student(name="Bob")
student3 = Student(name="Charlie")

math_subject = Subject(name="Math")
english_subject = Subject(name="English")
science_subject = Subject(name="Science")

session.add_all([student1, student2, student3, math_subject, english_subject, science_subject])

english_subject.students.append(student1)
english_subject.students.append(student2)

session.commit()


english_students = session.query(Student).join(Student.subjects).filter(Subject.name == "English").all()
english_student_names = [student.name for student in english_students]
print("Students who visited 'English' classes:", english_student_names)
