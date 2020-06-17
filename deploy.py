from flask import Flask, request, render_template, redirect, url_for, Response, send_file
from flask import json,jsonify
import smtplib
import sys
from email.message import Message
from flask_cors import CORS



app = Flask(__name__)

# Enables CORS requests for the service
CORS(app)

# This is the basic index route which can probably be used to check
# if the service is up and running once it is deployed but this is
# not called by the client at any point
@app.route('/')
def index():
    return "WORKING"


# This is the method that handles the sendMail() function and expects 
# a JSON input in the POST request that is made by the client
# Fields required mentioned in the reference document
@app.route('/sendMailOTP', methods=['POST'])
def sendMail():
    # Initializing SMTP 
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Mail ID and credential from where all the mails will be sent are to be given here
    # USE CHRIST ID!!! Personal mails have restrictions on the number of mails that can be sent
    s.login("Your Mail ID Ex- jival.jenson@btech.christuniversity.in", "Your Password")

    # The content variable will hold the JSON request body
    content = request.get_json()
    
    # Access the otp field that is within the JSON request
    otp = content['otp']
    # Access the email field that is within the JSON request
    email = content['email']

    # Email content definition
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

    # Construction of the message to be sent
    msg = Message()
    msg['Subject'] = "Open Elective OTP"
    msg['From'] = 'CHRIST (Deemed to be University)'
    msg['To'] = 'You'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_cont)
    
    # Sending the Mail
    # The mail ID specified above to be given here again
    s.sendmail("Your Mail ID Ex- jival.jenson@btech.christuniversity.in", email, msg.as_string())
    
    # Close SMTP session
    s.quit()
    
    # Sends a success response
    resp = jsonify(success=True)
    return resp


# This is the method that is used to send the confirmation mail with the selected preferences
# Expects a JSON request from the client as a POST request
# Fields required mentioned in the reference document
@app.route('/sendMailConfirmation', methods=['POST'])
def sendConfirmMail():
    # Initializing SMTP 
    s = smtplib.SMTP('smtp.gmail.com', 587)
 
    # Start TLS for security
    s.starttls()

    # Mail ID and credential from where all the mails will be sent are to be given here
    # USE CHRIST ID!!! Personal mails have restrictions on the number of mails that can be sent
    s.login("Your Mail ID Ex- jival.jenson@btech.christuniversity.in", "Your Password")
    
    # The content variable will hold the JSON request body
    content = request.get_json()

    # Access the email field that is within the JSON request
    email = content['email']
    # Access the first_pref field that is within the JSON request (Subject code)
    first_pref = content['first']
    # Access the second_pref field that is within the JSON request (Subject code)
    second_pref = content['second']
    # Access the third_pref field that is within the JSON request (Subject code)
    third_pref = content['third']

    # Dictionary to lookup the name of the subject of the given subject code
    # Change according to the respective year's available subjects
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

    # Getting the names of the subjects from the dictionary
    ffirst = dictionary[first_pref]
    ssecond = dictionary[second_pref]
    tthird = dictionary[third_pref]
    
    # Mail content
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

    # Construction of the message 
    msg = Message()
    msg['Subject'] = "Open Elective Confirmation"
    msg['From'] = 'CHRIST (Deemed to be University)'
    msg['To'] = 'You'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_cont)
    
    # Sending the mail
    # The mail ID specified above to be given here again
    s.sendmail("Your Mail ID Ex- jival.jenson@btech.christuniversity.in", email, msg.as_string())
    
    # Close SMTP session
    s.quit()

    #Sending Success Response
    resp = jsonify(success=True)
    return resp


if __name__ == '__main__':

    # Hosting the app
    app.run(host='0.0.0.0', debug=True, use_reloader=False)

