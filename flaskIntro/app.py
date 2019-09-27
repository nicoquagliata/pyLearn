from flask import Flask
from flask import render_template
#from flask import request

app = Flask(__name__)


@app.route("/")
@app.route("/<string:username>")
def welcome(username="invitado"):

    context = {'nombre':username}

    return render_template('index.html', **context)



@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1,num2):
    return render_template('suma.html', num1=num1, num2=num2)


@app.route("/resta/<int:num1>/<int:num2>")
def resta(num1,num2):
    context = {'num1':num1,'num2':num2}
    return render_template('resta.html', **context)

    
@app.route('/images')
def view_gallery():
    return 'Image Gallery'


if __name__ == "__main__":
    app.run(debug = True)
