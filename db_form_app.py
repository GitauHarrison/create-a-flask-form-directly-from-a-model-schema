from app import app, db
from app.models import TeacherObjectives


@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db,
        TeacherObjectives=TeacherObjectives
    )
