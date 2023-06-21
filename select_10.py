from sqlalchemy import select, func

from connect_db import session
from models import Groups, Students, Proffessors, Subjects, Marks
"""
Список курсов, которые определенному студенту читает определенный преподаватель
"""

query = session.query(
Subjects.subject_name,Students.student_name, Proffessors.proffessor_name).select_from(Subjects).join(Marks).join(Students).join(Proffessors).where(Students.id == 24 and Proffessors.id == 3).all()