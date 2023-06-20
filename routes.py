from flask import Flask, render_template, request, redirect, url_for, session
from database import engine,add_program,load_programs, add_user,check_user_role
from app import app

@app.route('/')
def home():
    return render_template("admin/home.html")

@app.route('/registration', methods=['POST'])
def add_users():
    user = request.form
    user_first_name=user["FirstName"]
    add_user(user)
    return render_template("successfully.html", FirstName=user_first_name)

@app.route('/registration')
def registration():
    return render_template("registration.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/login', methods=['POST'])
def login_user():
    user_details=request.form
    email=user_details["email"]
    password=user_details["password"]

    with engine.connect() as conn:
        result= conn.execute(text('select * from Users where Email=%(Email)s, Passw=%(Passw)s'),{'Email':email,'Passw':password})
        first_name=result["First_name"]
    if  user_details["email"] == result["Email"] and check_password_hash(password,result["Passw"]):
        user_role= check_user_role(result["id"])
        signedin='true'
        session.add(first_name,user_role,signedin)
        session.commit()
        return render_template("admin/home.html")
    
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
    programs_list=load_programs()
    return render_template("programs/programs.html",programs_l=programs_list)

"""
@app.route("/programs/<program_name>")
def programs(program_name):
    programs_list=load_programs(program_name)
    return render_template("programs/programs.html",programs_l=programs_list)
"""
@app.route('/manageprograms')
def manageprograms():
    return render_template("programs/manageprograms.html")

@app.route("/trainings")
def trainings():
    return render_template("trainings/trainings.html")

@app.route("/tutorials")
def tutorials():
    return render_template("tutorials/tutorials.html")

@app.route("/register")
def register():
    return render_template("registrationform.html")
