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
            return "ON"
        else:
            return "OFF"
    else:
        return "invalid"

@app.route('/main')
#this function renders the html template
def index():
    return render_template("index.html")

@app.route('/postdata')
def postdata():
    key = request.args.get('key')
    value = request.args.get('value')
    print "key = %s, value = %s" % (key, value)
    #writes value to a file
    with open (key+'.txt', 'w') as file:
        file.write(value+"\n")
    return ("written successfully with value %s" %(value))

@app.route('/postdelaydata')
def postDelayData():
    key = request.args.get('key')
    value=request.args.get('value')
    print "key = %s, value = %s" % (key, value)
    #writes value to a file
    with open (key+'.txt', 'a') as file:
        file.write(value+"\n")
    return ("appended successfully with value %s" %(value))



@app.route('/getdata')
def getdata():
    key = request.args.get('key')
    #value = request.args.get('value')
    #print "key = %s, value = %s" % (key, value)

    #checks if the file exists, then reads existing file and returns the value
    if os.path.isfile(key + '.txt'):
        with open (key+'.txt', 'r') as file:
            value = file.read()
        if value == '1':
            return "ON"
        else:
            return "OFF"
    else:
        return 'invalid'

@app.route('/getdelaydata')
def getDelayData():
    key = request.args.get('key')
    #value = request.args.get('value')
    #print "key = %s, value = %s" % (key, value)

    #checks if the file exists, then reads existing file and returns the value
    if os.path.isfile(key + '.txt'):
        with open (key+'.txt', 'r') as file:
            return file.read()
    else:
        return 'invalid'

