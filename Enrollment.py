from orm_base import Base
from sqlalchemy import String, Integer, UniqueConstraint
from sqlalchemy import ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Enrollment(Base):
    __tablename__ = "enrollments"

    #no attributes here except for discriminator
    student: Mapped["Student"] = relationship(back_populates="enrollments")
    section: Mapped["Section"] = relationship(back_populates="enrollments")
    #surrogate i think? based off roadmap, coming from student & section
    studentID: Mapped[int] = mapped_column('student_id', ForeignKey("students.student_id"),
                                           primary_key=True)
    sectionID: Mapped[int] = mapped_column('section_id', ForeignKey("sections.section_id"),
                                           primary_key=True)
    '''departmentAbbreviation: Mapped[str] = mapped_column('department_abbreviation',
                                                        ForeignKey("sections.department_abbreviation"),
                                                        primary_key=True)
    courseNumber: Mapped[str] = mapped_column('course_number', ForeignKey("sections.course_number"),
                                              primary_key=True)
    sectionYear: Mapped[int] = mapped_column('section_year', ForeignKey("sections.section_year"),
                                             primary_key=True)
    semester: Mapped[str] = mapped_column('semester', ForeignKey("sections.semester"),
                                          primary_key=True)

    __table_args__ = (UniqueConstraint('department_abbreviation', 'course_number', 'section_year',
                                       #'semester', 'student_id', name="enrollments_uk_01"),)'''

    def __init__(self, student, section):
        self.student = student
        self.section = section
        self.studentID = student.studentID
        self.sectionID = section.sectionID

    def __str__(self):
        return f"Student: {self.student} is enrolled in section: {self.section}"