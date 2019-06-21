from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

        user_error = ''
        password_error = ''
        verify_error = ''
        email_error = ''


        return render_template('signup.html', title="Sign Up", username=username, password=password, verify=verify, email=email)
    
    else:
        return render_template('signup.html', title="Sign Up")

app.run()