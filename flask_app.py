from flask import Flask, request, url_for,render_template
import random, os, os.path, json
import matplotlib.pyplot as plt



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
    updatedelay()
    return render_template("index.html")

@app.route('/imgsw')
#this function renders the image switch html
def switchindex():
    return render_template("rgbtest.html")

@app.route('/lamp')
#this function renders the LAMP html
def lampcontrol():
    return render_template("lamp.html")

@app.route('/combo')
#this function renders the image switch html
def combo():
    return render_template("combined.html")

@app.route('/updatedelay')
def updatedelay():
    #read delay data
    with open ('delay.txt','r') as file:
        delay_array = file.readlines()
    for idx,delay in enumerate(delay_array):
        delay_array[idx] = int(delay)

    plot_delay(delay_array, 'mysite/static/delay_plot.jpeg')
    return ""

@app.route('/getlatestdelay')
def getlatestdelay():
    #read delay data
    with open ('delay.txt','r') as file:
        delay_array = file.readlines()
    print "getlatestdelay: " + str(delay_array[-1])
    return delay_array[-1].strip()

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
def plot_delay(data, output):
    plt.plot(data)
    plt.ylabel('Delay')
    plt.savefig(output)