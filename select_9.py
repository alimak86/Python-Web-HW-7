from sqlalchemy import select, func

from connect_db import session
from models import Groups, Students, Proffessors, Subjects, Marks
"""
Найти список курсов, которые посещает определенный студент
"""

query = session.query(Subjects.subject_name,
                      Students.student_name).select_from(Subjects).join(
                          Marks).join(Students).where(Students.id == 24).all()
