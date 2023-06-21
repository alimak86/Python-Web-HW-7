from sqlalchemy import select, func

from connect_db import session
from models import Groups, Students, Proffessors, Subjects, Marks
"""
Найти список студентов в определенной группе
"""

query = session.query(
    Students.student_name,
    Groups.group_name).select_from(Students).join(Groups).where(
        Groups.id == 2).all()