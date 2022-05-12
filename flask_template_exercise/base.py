from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    username = request.args.get('username')
    upper = False
    lower = False
    numb_end = False

    upper = any(char.isupper() for char in username)
    lower = any(char.islower() for char in username)
    numb_end = username[-1].isdigit()
    report = upper and lower and numb_end

    return render_template('report.html',report=report,upper=upper,lower=lower, numb_end=numb_end)

if __name__ == '__main__':
    app.run(debug=True)