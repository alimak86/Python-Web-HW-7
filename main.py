from sqlalchemy import select, func

from connect_db import session
from models import Groups, Students, Proffessors, Subjects, Marks

import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10

if __name__ == '__main__':
    """
  working with the queries here
  """

    # q = session.execute(select(Groups.id, Groups.group_name)).mappings().all()
    #   print(q)

    #   q = session.execute(select(Proffessors.id,
    #                              Proffessors.proffessor_name)).mappings().all()
    #   print(q)

    #   q = session.execute(
    #       select(Students.id, Students.student_name,
    #              Students.student_group)).mappings().all()
    #   print(q)

    #   q = session.execute(
    #       select(Subjects.id, Subjects.subject_name,
    #              Subjects.proffessor_id)).mappings().all()
    #   print(q)

    # q = session.execute(
    #     select(Marks.id, Marks.student_id, Marks.subject_id,
    #            Marks.mark)).mappings().all()
    # print(q)
    """
    Найти 5 студентов с наибольшим средним баллом по всем предметам
    """
    print(select_1.query)
    """
    Найти студента с наивысшим средним баллом по определенному предмету
    """
    print(select_2.query)
    """
    Найти средний балл в группах по определенному предмету
    """
    print(select_3.query)
    """
    Найти средний балл на потоке (по всей таблице оценок)
    """

    print(select_4.query)

    """
    Найти какие курсы читает определенный преподаватель
    """

    print(select_5.query)
    """
    Найти список студентов в определенной группе
    """


    print(select_6.query)
    """
    Найти оценки студентов в отдельной группе по определенному предмету
    """

    print(select_7.query)
    """
    Найти средний балл, который ставит определенный преподаватель по своим предметам
    """

    print(select_8.query)
    """
    Найти список курсов, которые посещает определенный студент
    """

    print(select_9.query)
    """
    Список курсов, которые определенному студенту читает определенный преподаватель
    """

    print(select_10.query)