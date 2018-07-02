from flask import render_template,Flask,request,flash
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import message, encoders
import time




class Email:

    def __init__(self):
        '''constructor which performs login
          when the object is created '''
        try:
            self.server = smtplib.SMTP('smtp.gmail.com', 587)
            self.server.starttls()
            self.server.login('atp12192@gmail.com', 'Ankrich5063')
            print "Performing login"
            print "Login successful"
        except:
            print "Something went wrong "



    def send_emails_attachment(self):

        msg = MIMEMultipart()
        msg['Subject'] = "Inquires "
        body ="Here are the "
        msg.attach(MIMEText(body, 'plain'))
        print "Attaching 1st attachment"
        filename = "Enq.txt"
        attachment = open("Enq.txt", "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)
        text = msg.as_string()
        self.server.sendmail("atp12192@gmail.com","ankit.tiwari12192@gmail.com",text)


app = Flask(__name__)















@app.route('/',methods=['GET','POST'])
def my_form():
    # obj = Email()
    # obj.send_emails_attachment()
    return render_template("index.html")


@app.route('/mail',methods=['POST'])
def send_email():


    Name = request.form['contactName']
    email = request.form['contactEmail']
    subject = request.form['contactSubject']
    message = request.form['contactMessage']
    kt = open("Enq.txt","a+")

    data = "\n\n\n*****************************************************\n\nList of Enquiry as on" + str(time.ctime())+"\n" +"Name is :  "+Name+"\n"+"\nEmail is : "+email+"\nSubject is : "+subject+"\nMessage is "+message+"=====================================================\n\n\n"

    # kt.write(str(data))
    print data

    #
    # msg2= " New Enquiry   \n" \
    #       "Name = "+Name+"\nEMail = "+email+"\nMessage = "+message
    # msg['Subject'] = subject
    # msg['From']="atp12192@gmail.com"
    # msg['To']="ankit.tiwari12192@gmail.com"
    # body = msg2
    #
    # msg.attach(MIMEText(body, 'plain'))
    # text = msg.as_string()
    # server.sendmail("atp12192@gmal.com","ankit.tiwari12192@gmail.com", text)


    return render_template("thankyou.html",value=Name)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)