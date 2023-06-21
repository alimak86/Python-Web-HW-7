from sqlalchemy import select, func

from connect_db import session
from models import Groups, Students, Proffessors, Subjects, Marks
"""
Найти средний балл на потоке (по всей таблице оценок)
"""

query = session.query(func.round(func.avg(
    Marks.mark), 2).label("avg_grade")).select_from(Marks).all()
