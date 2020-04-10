from flask import Flask , render_template , redirect , url_for , request , session , flash
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin


app = Flask(__name__) 

app.config['SECRET_KEY'] = 'mysecret'

# app.config['SQLACHEMY_DATABASE_URI'] = 'example.db'
# app.config['SECRET_KEY'] = 'mysecret'


# db = SQLAlchemy(app)

# class User(db.Model , UserMixin):
#     id = db.Column(db.Integer , primary_key = True)
#     name = db.Column(db.String(20))

# admin = Admin(app)
# admin.add_view(ModelView(User,db.session))



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/admin")
def admin():
    return render_template("admin_page.html") 

@app.route("/welcome")
def welcome():
    return render_template("welcome_page.html")

@app.route("/login" , methods = ['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials !! '
        else :
            session['logged_in'] = True # if user creds match
            flash("Login succesfull ! ")
            return redirect(url_for('admin'))
    return render_template("login.html" , error = error)

@app.route("/logout")
def logout():
    session.pop('logged_in' , None)
    flash("logout successfull ! ")
    return redirect(url_for('welcome'))


if __name__ == '__main__':
    app.run(debug=True)
