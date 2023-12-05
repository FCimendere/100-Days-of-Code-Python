
"""
PRACTISE: Building Advance Forms with Flask-WTForms
PROJECT: This is WTForms, Validation, Flask, Bootstrap Practise. 
Forms are created by Flask-WTForms and CSRF protection was added.
Some form areas are created using libraries of WTForms, e.g. Stringfield, and Passwordfield.
forms objects are passed over dynamically via label property.
Validators are used to control whether the email address is correct, the same, has enough characters in it, etc.
Jinja2 uses inherited templates.
Design is improved via Bootstrap Framework.
"""


from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, DataRequired
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = "123456789@!"
bootstrap = Bootstrap5(app)

class LoginForm(FlaskForm):
    email = StringField('Email', [InputRequired(message="You need type your email"), DataRequired(),
                                                   Email()])
    password = PasswordField(label='Password',  validators=[InputRequired(message="Input required")])
    submit = SubmitField(label='Log In')



@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
