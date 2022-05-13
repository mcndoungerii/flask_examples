from flask import Flask, render_template,redirect, flash, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    breed = StringField('What breed are you?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET','POST'])
def index():
    form = InfoForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f"You just submitted the form: {session['breed']}")
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
