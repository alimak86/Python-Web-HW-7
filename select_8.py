from sqlalchemy import select, func

from connect_db import session
from models import Groups, Students, Proffessors, Subjects, Marks
"""
Найти средний балл, который ставит определенный преподаватель по своим предметам
"""

query = session.query(
    Proffessors.proffessor_name,
    func.round(func.avg(Marks.mark),
               2).label("avg_grade")).select_from(Proffessors).join(
                   Subjects).join(Marks).where(Proffessors.id == 4).all()
