from sqlalchemy import select, func

from connect_db import session
from models import Groups, Students, Proffessors, Subjects, Marks
"""
Найти оценки студентов в отдельной группе по определенному предмету
"""

query = session.query(Students.student_name, Marks.mark, Groups.group_name,
                      Subjects.subject_name).select_from(Students).join(
                          Marks).join(Groups).join(Subjects).where(
                              Groups.id == 4 and Subjects.id == 5).all()
