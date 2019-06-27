from flask import Flask, request, redirect, render_template
import cgi
import os
import string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/welcome")
def valid_user():
    username = str(request.args.get('username'))
    return '<h1>Welcome, {0}! </h1>'.format(username)

def contains_space(text):
    return True in [char in text for char in string.whitespace]

def char_count(string):
    if len(string) > 20 or len(string) <= 3:
        return True

def verify_pass(password, verfiy):
    if str(password) != str(verfiy):
        return True

def email_period(string):
    if string.count('.') == 1:
        return True
    else:
        return False

def multi_email_period(string):
    if string.count('.') >= 1:
        return True
    else:
        return False

def email_at_sign(string):
    if string.count('@') == 1:
        return True
    else:
        return False

def multi_at_sign(string):
    if string.count('@') >= 1:
        return True
    else:
        return False



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

        if contains_space(username) == True:
            user_error = "No spaces please!"
            return render_template('signup.html', title="Sign Up", username=username, user_error=user_error, password='', password_error=password_error, verify='', verify_error=verify_error, email=email, email_error=email_error)
        elif char_count(username) == True:
            user_error = "Please enter a username between 3 and 20 characters"
            password = ''
            return render_template('signup.html', title="Sign Up", username=username, user_error=user_error, password='', password_error=password_error, verify='', verify_error=verify_error, email=email, email_error=email_error)
        elif char_count(password) == True:
            password_error = "Please enter a password between 3 and 20 characters"
            verify = ''
            return render_template('signup.html', title="Sign Up", username=username, user_error=user_error, password='', password_error=password_error, verify='', verify_error=verify_error, email=email, email_error=email_error)
        elif verify_pass(password, verify) == True:
            verify_error = "Passwords must match"
            verify = ''
        elif email != '':
            if char_count(email) == True:
                email_error = "Please enter an email address between 3 and 20 characters"
                password = ''
                verify = ''
                return render_template('signup.html', title="Sign Up", username=username, user_error=user_error, password='', password_error=password_error, verify='', verify_error=verify_error, email=email, email_error=email_error)
            elif not email_period(email):
                email_error = "Email must contain ."
                password = ''
                verify = ''
                return render_template('signup.html', title="Sign Up", username=username, user_error=user_error, password='', password_error=password_error, verify='', verify_error=verify_error, email=email, email_error=email_error)
            elif not multi_email_period(email):
                email_error = "Email must contain ."
                password = ''
                verify = ''
                return render_template('signup.html', title="Sign Up", username=username, user_error=user_error, password='', password_error=password_error, verify='', verify_error=verify_error, email=email, email_error=email_error)
            elif not email_at_sign(email):
                email_error = "Email must contain '@'"
                password = ''
                verify = ''
                return render_template('signup.html', title="Sign Up", username=username, user_error=user_error, password='', password_error=password_error, verify='', verify_error=verify_error, email=email, email_error=email_error)
            elif not multi_at_sign(email):
                email_error = "Email must contain only 1 '@'"
                password = ''
                verify = ''
                return render_template('signup.html', title="Sign Up", username=username, user_error=user_error, password='', password_error=password_error, verify='', verify_error=verify_error, email=email, email_error=email_error)
            else:
                return redirect('/welcome?username={0}'.format(username))    
        else:
            return redirect('/welcome?username={0}'.format(username))


        return render_template('signup.html', title="Sign Up", username=username, user_error=user_error, password=password, password_error=password_error, verify=verify, verify_error=verify_error, email=email, email_error=email_error)
    
    else:
        return render_template('signup.html', title="Sign Up")

app.run()