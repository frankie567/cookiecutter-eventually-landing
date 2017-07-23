from email_validator import validate_email, EmailNotValidError
from flask import Flask, jsonify, render_template, request
from mailjet_rest import Client


app = Flask(__name__)
app.config.from_object('{{cookiecutter.project_slug}}.config.Config')

mailjet = Client(
    auth=(app.config['MJ_APIKEY_PUBLIC'], app.config['MJ_APIKEY_PRIVATE']),
    version='v3'
)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            email = validate_email(request.form['email'])['email']
        except EmailNotValidError:
            return jsonify({'detail': 'The email address you provided is invalid.'}), 400

        mailjet_response = mailjet.contactslist_managecontact.create(
            id=app.config['MJ_CONTACTSLIST_ID'],
            data={'Email': email, 'Action': 'addnoforce'}
        )
        if mailjet_response.status_code < 400:
            return jsonify({'detail': 'Thank you!'})
        else:
            return jsonify({'detail': 'An error occured. Please retry later.'}), 400

    return render_template('index.html')
