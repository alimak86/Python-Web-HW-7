from sqlalchemy import select, func

from connect_db import session
from models import Groups, Students, Proffessors, Subjects, Marks
"""
Найти средний балл в группах по определенному предмету
"""

query = session.query(
    Groups.group_name,
    func.round(func.avg(Marks.mark), 2).label("avg_grade"),
    Subjects.subject_name).select_from(Students).join(Groups).join(Marks).join(
        Subjects).where(Marks.subject_id == 5).group_by(
            Groups.group_name).order_by(func.avg(Marks.mark).desc()).all()
