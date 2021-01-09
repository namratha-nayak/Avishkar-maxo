from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def stuhome():
    return render_template('stuhome.html')

@app.route('/notepad')
def notepad():
    return render_template('notepad.html')



if __name__ == '__main__':
    app.run(debug = True)





