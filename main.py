from flask import render_template,Flask,request,flash
import os
import smtplib
import time

app = Flask(__name__)



@app.route('/',methods=['GET','POST'])
def my_form():

    return render_template("index.html")

@app.route('/mail',methods=['POST'])

def send_email():
    Name = request.form['contactName']
    email = request.form['contactEmail']
    subject = request.form['contactSubject']
    message = request.form['contactMessage']
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('atp12192@gmail.com', 'Tiwari12192')
    data = "\n\n\n*****************************************************\n\nList of Enquiry as on" + str(time.ctime())+"\n" +"Name is :  "+Name+"\n"+"\nEmail is : "+email+"\nSubject is : "+subject+"\nMessage is "+message+"\n\n\n=====================================================\n\n\n"
    print (data)
    message = """From: """ + "Ankut <ank9222@gmail.com>" + """ \nTo: """ + "mail@ankitt.com" + """ \nSubject: """ + subject + """\n\n """ + data + """"""
    server.sendmail("atp12192@gmal.com","mail@ankitt.com", message)
    return render_template("thankyou.html",value=Name)



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run( port=port, debug=False)