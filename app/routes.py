from app import app, db
from flask import render_template, request, redirect, url_for, flash
from wtforms_sqlalchemy.orm import model_form
from app.models import TeacherObjectives


@app.route('/', methods=['GET', 'POST'])
def index():
    # TEACHER OBJECTIVES FORM

    # Create a form from the model
    TeacherObjectivesForm = model_form(TeacherObjectives)

    # Create an instance of the model
    teacher_objectives = TeacherObjectives()

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = TeacherObjectivesForm(request.form, obj=teacher_objectives)
        if form.validate():
            form.populate_obj(teacher_objectives)
            db.session.add(teacher_objectives)
            db.session.commit()
            flash('Teacher Objective Added!')
            return redirect(url_for('index'))
    else:
        form = TeacherObjectivesForm(obj=teacher_objectives)
    return render_template(
        'index.html',
        form=form
        )
