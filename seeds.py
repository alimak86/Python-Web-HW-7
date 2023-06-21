from connect_db import session
from models import Groups, Students, Proffessors, Subjects, Marks
import fill_data

if __name__ == '__main__':
    """ fill up the tables here for the database"""

    for num in range(fill_data.NUMBER_GROUPS):
        group_name_ = "G-" + str(num + 1)
        group = Groups(group_name=group_name_)
        session.add(group)
        session.commit()

    gen = fill_data.DataGenerator(fill_data.NUMBER_PROFS, fill_data.NAME)
    names = gen.generate()
    for name in names:
        proffessor = Proffessors(proffessor_name=name)
        session.add(proffessor)
        session.commit()

    gen = fill_data.DataGenerator(fill_data.NUMBER_STUDENTS, fill_data.NAME)
    names = gen.generate()
    for name in names:
        group_id = gen.group_generator()
        student = Students(student_name=name, student_group=group_id)
        session.add(student)
        session.commit()

    gen = fill_data.DataGenerator(fill_data.NUMBER_STUDENTS, fill_data.NAME)
    for name in fill_data.SUBJECTS:
        proff_id = gen.proff_generator()
        subject = Subjects(subject_name=name, proffessor_id=proff_id)
        session.add(subject)
        session.commit()

    gen = fill_data.DataGenerator(fill_data.NUMBER_STUDENTS, fill_data.NAME)
    for num in range(fill_data.MAX_MARKS):
        for student_id1 in range(1, fill_data.NUMBER_STUDENTS):
            mark1 = gen.mark_generator()
            subject_id1 = gen.subject_generator()
            mark_obj = Marks(student_id=student_id1,
                             subject_id=subject_id1,
                             mark=mark1)
            session.add(mark_obj)
            session.commit()
