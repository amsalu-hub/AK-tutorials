from sqlalchemy import create_engine,text,inspect
from werkzeug.security import generate_password_hash, check_password_hash

db_connection_string="mysql+pymysql://0v59zl6tcengq35onjuf:pscale_pw_Jmimk8Qz14BdH5gSX6DuAwtWl669bnHbCVis49sQ9yX@aws.connect.psdb.cloud/akonlineschooldb?charset=utf8mb4"
engine = create_engine(db_connection_string,
connect_args = { "ssl":{
     "ssl_ca": "/etc/ssl/cert.pem"
}})


def check_user_role(email):
    with engine.connect() as conn:
        result= conn.execute(text("select * from UserRole where Email=:Email"),{"Email":email}).first()
    
    return result[2]

def load_programs(p_name):
    with engine.connect() as conn:
        result= conn.execute(text("select * from Programs where program_name=:progname"),{"progname":p_name})
    return result.all()

def add_program(data):
    with engine.connect() as conn:
        query="insert into Programs(program_name, department, prodescription, duration) values(:program_name, :department, :prodescription, :duration)"
        conn.execute(query,program_name=data["program_name"],department=data["department"],prodescription=data["prodescritpion"],duration=data["duration"])

def add_user(user):
    with engine.connect() as conn:             
        query = text("INSERT INTO Users(First_name, Middle_name, Last_name, Email, Passw) VALUES(:first_name, :middle_name, :last_name, :email, :passw)")
        conn.execute(query, 
                    {'first_name':user['FirstName'],
                    'middle_name':user['MiddleName'], 
                    'last_name':user['LastName'], 
                    'email':user['Email'], 
                    'passw': generate_password_hash(user['Password'])
                    }                    
                    )