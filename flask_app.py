from flask import Flask, request, url_for,render_template
import random, os, os.path, json

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

@app.route('/invert')
def invert():
    key = request.args.get('key')
    #print "key = %s, value = %s" % (key, value)
    if os.path.isfile(key + '.txt'):
        with open (key+'.txt', 'r') as file:
            current_value = file.read()
        if current_value == '1':
            current_value = '0'
        else:
            current_value = '1'
        with open (key+'.txt', 'w') as file:
            file.write(current_value)
        if current_value == '1':
            return "LED ON"
        else:
            return "LED OFF"
    else:
        return "invalid"

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

