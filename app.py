from flask import Flask, render_template, request, redirect, url_for, session
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import text, inspect
from database import engine,add_program,load_programs, add_user,check_user_role

#from sqlalchemy import sqlalchemy

app = Flask(__name__)

app.config.from_object(Config)
#db=sqlalchemy(app)

"""
def load_programs(program_name):
    with engine.connect() as conn:
        result= conn.execute(text("select * from Programs where program_name='"+ program_name +"'"))
    return result.all()
"""
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/registration', methods=['POST'])
def add_users():
    if session["Signedin"]=="true":
        user = request.form
        user_first_name=user["FirstName"]
        add_user(user)
        return render_template("successfully.html", FirstName=user_first_name)
    return render_template("restrictedpage.html")

@app.route('/registration')
def registration():
    return render_template("registration.html")

@app.route('/logout')
def logout():
    session["User_role"]=""
    session["First_name"]=""
    session["Signedin"]=""
    return redirect('/')

@app.route('/login', methods=['POST'])
def login_user():
    
    user_details=request.form
    email=user_details["email"]
    password=user_details["password"]

    with engine.connect() as conn:
        result=conn.execute(text("select * from Users where Email = :Email"),{"Email":email}).first()
        first_name=result[1]
        
    if  email == result[4] and check_password_hash(result[5],password):
        user_role= check_user_role(result[4])
        session["User_role"]=user_role
        session["Email"]=email
        session["First_name"]=first_name
        session["Signedin"]='true'
        if user_role=="admin":
            return render_template("admin/home.html")
        if user_role=="user":
            return render_template("user/home.html")
        #print("Incorrect email or password")
    
@app.route('/login',methods=['GET'])
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/programs")
def programs():
    with engine.connect() as conn:
        programs_list=conn.execute(text("select * from Programs"))
        
    return render_template("programs/programs.html",programs_l=programs_list)

"""
@app.route("/programs/<program_name>")
def programs(program_name):
    programs_list=load_programs(program_name)
    return render_template("programs/programs.html",programs_l=programs_list)
"""
@app.route('/manageprograms')
def manageprograms():
    if session["Signedin"]=="true":
        tvet_programs_list=load_programs("TVET")
        ug_programs_list=load_programs("Undergraduate")
        pg_programs_list=load_programs("Postgraduate")
        return render_template("programs/manageprograms.html",tpl=tvet_programs_list,upl=ug_programs_list,ppl=pg_programs_list)
    return render_template("restrictedpage.html")

@app.route("/editprogram/<id>",methods=['GET','POST'])
def editprogram(id):
    if session["Signedin"]=="true":
        return render_template("editprogram.html")
    return render_template("restrictedpage.html")

@app.route("/detailprogram/<id>",methods=['GET','POST'])
def detailprogram(id):
   if session["Signedin"]=="true":
        return render_template("detailprogram.html")
   return render_template("restrictedpage.html")

@app.route("/deleteprogram/<id>",methods=['GET','POST'])
def deleteprogram(id):
    if session["Signedin"]=="true":
        return render_template("deleteprogram.html")
    return render_template("restrictedpage.html")

@app.route("/trainings")
def trainings():
    return render_template("trainings/trainings.html")

@app.route("/tutorials")
def tutorials():
    return render_template("tutorials/tutorials.html")

@app.route("/enroll/<course>")
def enroll(course):
    if session["Signedin"]=="true":
        return render_template("enroll.html",course=course)
    return render_template("restrictedpage.html")
if __name__=='__main__':
   app.run()