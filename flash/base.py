from flask import Flask, render_template, flash, session, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class SimpleForm(FlaskForm):
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        flash('You just submittted the form!')
        return redirect(url_for('index'))
    
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)