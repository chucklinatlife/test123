from flask import Flask, request, url_for,render_template
import random, os, os.path, json

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

@app.route('/')
def hello_person():
    return """
        <p>Who do you want me to say "Hi" to?</p>
        <form method="POST" action="%s"><input name="person" /><input type="submit" value="Go!" /></form>
        """ % (url_for('greet'),)

@app.route('/tem')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index.html")


@app.route('/greet', methods=['POST'])
def greet():
    greeting = random.choice(["Hiya", "Hallo", "Hola", "Ola", "Salut", "Privet", "Konnichiwa", "Ni hao"])
    return """
        <p>%s, %s!</p>
        <p><a href="%s">Back to start</a></p>
        """ % (greeting, request.form["person"], url_for('hello_person'))

@app.route('/testparams')
def showparams():
    param1 = request.args.get('param1', '0-100')
    return "param1 = %s" % (str(param1),)

@app.route('/postdata')
def postdata():
    key = request.args.get('key')
    value = request.args.get('value')
    print "key = %s, value = %s" % (key, value)
    with open (key+'.txt', 'w') as file:
        file.write(value)
    return "gotya"

@app.route('/getdata')
def getdata():
    key = request.args.get('key')
    #value = request.args.get('value')
    #print "key = %s, value = %s" % (key, value)
    if os.path.isfile(key + '.txt'):
        with open (key+'.txt', 'r') as file:
            value = file.read()
        return value
    else:
        return 'invalid'


@app.route('/hello')
def hello():
    return json.dumps(
        {
            "siteName": "JQUERY4U",
            "domainName": "http://www.jquery4u.com",
            "description": "#1 jQuery Blog for your Daily News, Plugins, Tuts/Tips &amp; Code Snippets."
        })