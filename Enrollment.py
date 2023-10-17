from orm_base import Base
from sqlalchemy import String, Integer, UniqueConstraint
from sqlalchemy import ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Enrollment(Base):
    __tablename__ = "enrollments"

    #no attributes here except for discriminator
    student: Mapped["Student"] = relationship(back_populates="sections")
    section: Mapped["Section"] = relationship(back_populates="students")
    studentID: Mapped[int] = mapped_column('student_id', ForeignKey("students.student_id"),
                                           primary_key=True)
    sectionID: Mapped[int] = mapped_column('section_id', ForeignKey("sections.section_id"),
                                           primary_key=True)

    def __init__(self, student, section):
        self.student = student
        self.section = section
        self.studentID = student.studentID
        self.sectionID = section.sectionID

    def __str__(self):
        return f"Student: {self.student} is enrolled in section: {self.section}"