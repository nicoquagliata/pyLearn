from flask import Flask, render_template, url_for, redirect, request
import json

#from flask import render_template
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

@app.route("/contacto/")
def contacto():
    return render_template('contacto.html')

@app.route("/enviar", methods=['POST'])
def enviar():
    response = redirect(url_for('welcome'))
    response.set_cookie(json.dumps(dict(request.form.items())))
    return response

@app.route("/resta/<int:num1>/<int:num2>")
def resta(num1,num2):
    context = {'num1':num1,'num2':num2}
    return render_template('resta.html', **context)

    
@app.route('/images')
def view_gallery():
    return 'Image Gallery'


if __name__ == "__main__":
    app.run(debug = True)
