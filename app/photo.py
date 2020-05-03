import os
from app import app
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename


class PhotoForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

# https://flask-wtf.readthedocs.io/en/stable/form.html
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = PhotoForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.instance_path, 'photos', filename
        ))
        return redirect(url_for('index'))

    return render_template('upload.html', form=form)
