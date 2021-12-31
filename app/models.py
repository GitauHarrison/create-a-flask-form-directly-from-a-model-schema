from app import db


class TeacherObjectives(db.Model):
    __tablename__ = 'teacher_objectives'
    id = db.Column(db.Integer, primary_key=True)
    teacher_objective_1 = db.Column(db.String(100))
    teacher_objective_2 = db.Column(db.String(100))

    def __repr__(self):
        return f'TeacherObjectives {self.teacher_objective_1}'
