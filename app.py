from flask import Flask,render_template, request, redirect, url_for, session 
from flaskext.mysql import MySQL 
import re 
import pymysql
from flask_fontawesome import FontAwesome
from chatbot import chatbot
import logging
app = Flask(__name__)
app.static_folder = 'static'
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

            # msg = print("\033[0;37;40m 'Logged in successfully !'\n")
            return render_template('home.html',name = username, msg=msg) 
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
@app.route("/bot")
def bot():
    return render_template("bot.html")
 
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))
logger = logging.getLogger()
logger.setLevel(logging.INFO)


@app.route('/stuhome')
def stuhome():
    return render_template('stuhome.html')

@app.route('/notepad')
def notepad():
    return render_template('notepad.html')

@app.route('/task')
def task():
    return render_template('task.html')

@app.route('/final')
def final():
    return render_template('final.html')
@app.route('/wordsearch')
def wordsearch():
    return render_template('wordsearch.html')
@app.route('/link')
def link():
    return render_template('link.html')
@app.route('/index1')
def index1():
    return render_template('index1.html')
@app.route('/main')
def main():
    return render_template('main.html')
@app.route('/scl2')
def scl2():
    return render_template('scl2.html')
@app.route('/scl3')
def scl3():
    return render_template('scl3.html')
@app.route('/scl4')
def scl4():
    return render_template('scl4.html')
@app.route('/scl5')
def scl5():
    return render_template('scl5.html')
@app.route('/eng16')
def eng16():
    return render_template('eng16.html')
@app.route('/eng17')
def eng17():
    return render_template('eng17.html')
@app.route('/soc16')
def soc16():
    return render_template('soc16.html')
@app.route('/soc17')
def soc17():
    return render_template('soc17.html')
@app.route('/math16')
def math16():
    return render_template('math16.html')
@app.route('/math17')
def math17():
    return render_template('math17.html')
@app.route('/sci16')
def sci16():
    return render_template('sci16.html')
@app.route('/sci17')
def sci17():
    return render_template('sci17.html')
if __name__ == '__main__':
    app.run(debug = True)





