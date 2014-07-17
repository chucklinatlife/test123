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
    return render_template("index.html")

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

