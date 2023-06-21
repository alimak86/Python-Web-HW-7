from sqlalchemy import select, func

from connect_db import session
from models import Groups, Students, Proffessors, Subjects, Marks

"""
Найти 5 студентов с наибольшим средним баллом по всем предметам
"""

query = session.query(
    Students.student_name,
    func.round(
        func.avg(Marks.mark),
        2).label("avg_grade")).select_from(Marks).join(Students).group_by(
            Students.id).order_by(func.avg(Marks.mark).desc()).limit(5).all()
