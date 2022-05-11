from flask import Flask

app = Flask(__name__)

@app.route('/') #127.0.0.1:5000
def index():
    return '<h1>Hello Puppy</h1>'

@app.route('/information') #127.0.0.1:5000/information
def info():
    return "<h1>Puppies are cute!</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>100th letter: {}</h1>".format(name[100])

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    latin_name = ''
    if name[-1] == 'y':
        latin_name = name[:-1] + 'iful'
    else:
        latin_name = name + 'y'
    return "<h1> Hi {}! Your puppy latin name is {}</h1>".format(name, latin_name)

if __name__ == "__main__":
    app.run(debug=True)