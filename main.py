from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__, template_folder='template')

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='kushalash555@gmail.com'
app.config['MAIL_PASSWORD']='123456Sa!'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail = Mail(app)



@app.route("/", methods=['GET','POST'])
def index():
   if request.method=="POST":
      name= request.form["name"]
      email= request.form["email"]
      message= request.form["msg"]

      msg = Message(subject="A mail by: "+ name,sender="kushalash555@gmail.com",recipients=[email])
      msg.body=message

      mail.send(msg)
   return render_template('index.html')
   

   

if __name__ == '__main__':
   app.run(debug = True)