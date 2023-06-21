from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

# -- Table: groups
# DROP TABLE IF EXISTS groups;
# CREATE TABLE groups (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     group_name VARCHAR(255) UNIQUE NOT NULL
# );


class Groups(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(255), nullable=False, unique=True)


# -- Table: students
# DROP TABLE IF EXISTS students;
# CREATE TABLE students (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     student_name VARCHAR(255) UNIQUE NOT NULL,
#     student_group INTEGER,
#     FOREIGN KEY (student_group) REFERENCES groups(id)
#       ON UPDATE CASCADE
# );


class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String(255), nullable=False, unique=True)
    student_group = Column(Integer, ForeignKey(Groups.id, onupdate="CASCADE"))


# -- Table: proffessors
# DROP TABLE IF EXISTS proffessors;
# CREATE TABLE proffessors (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     proffessor_name VARCHAR(255) UNIQUE NOT NULL
# );


class Proffessors(Base):
    __tablename__ = "proffessors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    proffessor_name = Column(String(255), nullable=False, unique=True)


# -- Table: subjects
# DROP TABLE IF EXISTS subjects;
# CREATE TABLE subjects (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     subject_name VARCHAR(255) UNIQUE NOT NULL,
#     proffessor_id INTEGER,
#     FOREIGN KEY(proffessor_id) REFERENCES proffessors (id)
# );


class Subjects(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(String(255), nullable=False, unique=True)
    proffessor_id = Column(Integer, ForeignKey(Proffessors.id))


# -- Table: marks
# DROP TABLE IF EXISTS marks;
# CREATE TABLE marks (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     student_id INTEGER,
#     subject_id INTEGER,
#     mark INTEGER,
#     FOREIGN KEY(student_id) REFERENCES students (id)
#     FOREIGN KEY(subject_id) REFERENCES subjects (id)
# );


class Marks(Base):
    __tablename__ = "marks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey(Students.id))
    subject_id = Column(Integer, ForeignKey(Subjects.id))
    mark = Column(Integer)
