from flask import Flask,render_template, request, redirect, url_for, session 
from flaskext.mysql import MySQL 
import re 
import pymysql
from flask_fontawesome import FontAwesome
app = Flask(__name__)
fa = FontAwesome(app)
mysql = MySQL() 
app.secret_key = '90e3e00160e18c77f96f7245'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'student_info'
mysql.init_app(app)
@app.route('/', methods =['GET', 'POST']) 
def index(): 
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    msg = '' 
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form: 
        username = request.form['username'] 
        password = request.form['password']  
        cursor.execute('SELECT * FROM student_details WHERE username = % s AND password = % s', (username, password, )) 
        student_details = cursor.fetchone() 
        if student_details: 
            session['loggedin'] = True
            session['id'] = student_details['id'] 
            session['username'] = student_details['username'] 
            msg = 'Logged in successfully !'
            return render_template('home.html', msg = msg) 
        else: 
            msg = 'Incorrect username / password !'
    return render_template('index.html', msg = msg) 
@app.route('/logout') 
def logout(): 
    session.pop('loggedin', None) 
    session.pop('id', None) 
    session.pop('username', None) 
    return redirect(url_for('index')) 
@app.route('/register', methods =['GET', 'POST']) 
def register(): 
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
  
    msg = '' 
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'username' in request.form and 'password' in request.form: 
        name = request.form['name']
        email = request.form['email']
        username = request.form['username'] 
        password = request.form['password'] 

        cursor.execute('SELECT * FROM student_details WHERE username = % s', (username)) 
        student_details = cursor.fetchone() 
        if student_details: 
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email): 
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username): 
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email: 
            msg = 'Please fill out the form !'
        else: 
            cursor.execute('INSERT INTO student_details VALUES (NULL, % s, % s, % s, %s)', (name, email, username, password)) 
            conn.commit() 
            msg = 'You have successfully registered !'
    elif request.method == 'POST': 
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg) 
@app.route('/home')
def home():
    return render_template("home.html")
@app.route('/bot')
def bot():
    return render_template("bot.html")



@app.route('/stuhome')
def stuhome():
    return render_template('stuhome.html')

@app.route('/notepad')
def notepad():
    return render_template('notepad.html')

@app.route('/task')
def task():
    return render_template('task.html')




if __name__ == '__main__':
    app.run(debug = True)





