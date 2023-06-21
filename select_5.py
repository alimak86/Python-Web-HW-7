from sqlalchemy import select, func

from connect_db import session
from models import Groups, Students, Proffessors, Subjects, Marks
"""
Найти какие курсы читает определенный преподаватель
"""

query = session.query(
    Subjects.subject_name,
    Proffessors.proffessor_name).select_from(Subjects).join(Proffessors).where(
        Proffessors.id == 3).all()
