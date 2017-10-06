from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))



app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def render_template():
        template = jinja_env.get_template('index.html')
        return template.render()


#@app.route('/')
#def display_user_form():
        #return render_template('index.html')
        #return 'index.html'.format(username='', username_error='', password='',
                #password_error='', verify='', verify_error='', email='', email_error='')
@app.route('/validate-form') 
def display_form():
        return 'index.html'.format(username='',
        username_error='',
        pasword='',
        password_error='',
        verify='',
        verify_error='',
        email='',
        email_error='')



def no_space(input):
        for char in input:
                if char == ' ' or len(input) == 0:
                        return False
                else:
                        return True

def is_correct(email):
        if '@' in email and '.' in email:
                return True
        else:
                return False
 
@app.route('/validate-form', methods=['POST'])
def validate_form():
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

        username_error = ''
        password_error = ''
        verify_error = ''
        email_error = ''


        if not no_space(username):
                username_error = 'Not a valid username'
                username = ''
        else:
                username_error = ''
                
        if len(username) < 3 or len(username) > 20:
                username_error = 'Username must be between 3-20 characters'
                username = ''     
        else:
                 username_error = ''

        if not no_space(password):
                password_error = 'Not a valid password'
                password = ''
        else:
                password_error = ''
        
        if len(password) < 3 or len(password) > 20:
                password_error = 'Password must be between 3-20 characters'
                password = ''
        else:
                password_error = ''

        if verify != password:
                verify_error = 'Passwords do not match'
                verify = ''  
        else:
                verify_error = ''
        
        if not no_space(email):
                email_error = 'Not a valid email'
                email = ''
        else:
                email_error = ''

        if len(email) < 3 or len(email) > 20:
                email_error = 'Email must be between 3-20 characters'
                email = ''
        else:
                email_error = ''

        if email != '':
                if not is_correct(email):
                        email_error = 'Email must contain one "at" symbol and one period'
                        email = ''
                else:
                        email_error = ''
        else:
                email_error = ''
        
        if not username_error and not password_error:
                if not verify_error and not email_error:
                        greeting = username
                        return redirect('/valid-form?greeting={0}'.format(greeting))
                                
        else:
                template = jinja_env.get_template('index.html')
                return 'index.html'.format(username=username,
                        username_error=username_error,
                        password=password,
                        password_error=password_error,
                        verify=verify,
                        verify_error=verify_error,
                        email=email,
                        email_error=email_error)

                
@app.route('/valid-form')
def valid_form():
        greeting = request.args.get('greeting')
        template = jinja_env.get_template('welcome.html')
        return template.render().format(greeting)
        #return '<h1>Welcome, {0} !</h1>'.format(greeting)


#VERIFY the password, (user must retype exactly)
# and VALIDATE the input
        
#IF user's form submission IS NOT valid :
        # ANY FIELD (username, password, or verify password) is empty,
        # username or password isn't valid (contains a space,
        # is less than 3 or more than 20 characters)
        # password and password-confirmation do not match
        # if an email IS provided, it isnt valid... so it contains:
                #a single @
                #a single .
                #contains no spaces
                #is between 3-20 characters long
        #THEN :
                #Error! ...
                #the form submission should be rejected and 
                #re-rendered with feedback of what went wrong

#Each feedback message should be next to field it refers to

#Use templates (index.html and welcome.html) to render
#the HTML for your web app


#CREATE a user signup form: username, password, email
#For the username and email fields, preserve what the user typed
#email type='text'
#password type='password'
#password verification type='password'
#The password fields should be cleared for security reasons



#else:
         #all input is valid, show a welcome page that uses
         #username input to display a welcome message of:
        #"Welcome, [username]!"



app.run()