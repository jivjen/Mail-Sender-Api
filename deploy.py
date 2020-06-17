from flask import Flask, request, render_template, redirect, url_for, Response, send_file
from flask import json,jsonify
import smtplib
import sys
from email.message import Message
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return "HELLLLLL"

@app.route('/sendMailOTP', methods=['POST'])
def sendMail():
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    s.login("jival.jenson@btech.christuniversity.in", "20259857")
    # otp = request.args.get('otp')
    # email = request.args.get('email')
    # otp = request.form['otp']
    # email = request.form['email']
    content = request.get_json()
    
    otp = content['otp']
    email = content['email']
    email_cont = """
        <html>
          <head>  
          <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
          <title>Open Elective OTP</title>
          </head>
          <body>
          <h1>Your Open Elective authentication OTP is <strong>"""+ otp +"""</strong></h1>
          </body>
        </html>
        """

    msg = Message()
    msg['Subject'] = "Open Elective OTP"
    msg['From'] = 'CHRIST (Deemed to be University)'
    msg['To'] = 'You'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_cont)
    # sending the mail
    s.sendmail("jival.jenson@btech.christuniversity.in", email, msg.as_string())

    s.quit()
    resp = jsonify(success=True)
    return resp

@app.route('/sendMailConfirmation', methods=['POST'])
def sendConfirmMail():
    s = smtplib.SMTP('smtp.gmail.com', 587)
 
    # start TLS for security
    s.starttls()

    s.login("jival.jenson@btech.christuniversity.in", "20259857")
    content = request.get_json()
    # email = request.args.get('email')
    # first_pref = request.args.get('first')
    # second_pref = request.args.get('second')
    # third_pref = request.args.get('third')
    email = content['email']
    first_pref = content['first']
    second_pref = content['second']
    third_pref = content['third']

    dictionary = {
    "CE636OE1" : "Solid Waste Management",
    "CE636OE2" : "Environmental Impact Assessment",
    "CE636OE4" : "Disaster Management",
    "CH63OE02" : "CATALYST TECHNOLOGY",
    "EC636OE1" : "Embedded Boards for IOT Applications",
    "EC636OE3" : "Virtual Instrumentation",
    "EC636OE7" : "E-WASTE MANAGEMENT AND RADIATION",
    "CS636OE01" : "WEB PROGRAMMING CONCEPTS",
    "CS636OE06" : "USER INTERFACE DESIGN CONCEPTS",
    "CS636OE08" : "PYTHON PROGRAMMING FOR ENGINEERS",
    "ME63OE01" : "Green Belt Practice",
    "ME63OE03" : "Basic Automobile Engineering",
    "ME63OE04" : "Project Management",
    "ME63OE05" : "Basic Aerospace Engineering",
    "PH63OE01" : "TECHNICAL CERAMICS",
    "CH63OE02" : "CATALYST TECHNOLOGY",
    "MA63OE03" : "NUMERICAL SOLUTION OF DIFFERENTIAL EQUATIONS",
    "EE636OE03" : "Introduction to Hybrid Electric Vehicles",
    "EE636OE06" : "Robotics and Automation",
    "EE636OE08" : "Matrix Computations",
    "PHE03" : "Advances In Materials Science and Engineering"

    }

    ffirst = dictionary[first_pref]
    ssecond = dictionary[second_pref]
    tthird = dictionary[third_pref]
    email_cont = """
            <html>
  <head>  
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Open Elective OTP</title>
  </head>
  <body>
  <h1>We have received your request as follows:</strong></h1>
  <ol>
    <li>First Preference: """+ ffirst+"""</li>
    <li>Second Preference: """+ ssecond+"""</li>
    <li>Third Preference: """+ tthird +"""</li>
  </ol>
  </body>
</html>
        """

    msg = Message()
    msg['Subject'] = "Open Elective Confirmation"
    msg['From'] = 'CHRIST (Deemed to be University)'
    msg['To'] = 'You'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_cont)
    # sending the mail
    s.sendmail("jival.jenson@btech.christuniversity.in", email, msg.as_string())
    s.quit()
    resp = jsonify(success=True)
    return resp
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_reloader=False)

