# Cookiecutter Eventually landing

Cookiecutter template building a coming soon page with [Eventually template by HTML5 UP!](https://html5up.net/eventually).

The form will add emails to a [Mailjet](https://www.mailjet.com/) contacts list.

## Getting started

Install the latest Cookiecutter if you haven't installed it yet:

```
pip install -U cookiecutter
```

Generate the project:

```
cookiecutter https://github.com/frankie567/cookiecutter-eventually-landing
```

The generator will ask you for the following information:
* **title**: Title of your project and header of the page.
* **project_slug**: Directory and package name of the project. Automatically generated from the title, but you can override it.
* **value_proposition**: Subtitle of the page. Make it punchy 👍
* **mailjet_apikey_public**: Your Mailjet public API key.
* **mailjet_apikey_private**: Your Mailjet private API key.
* *mailjet_contactslist_id*: Mailjet contacts list's id in which the emails will be added.
* **facebook** (*optional*): Facebook link shown at the bottom of the page.
* **twitter** (*optional*): Twitter link shown at the bottom of the page.
* **linkedin** (*optional*): LinkedIn link shown at the bottom of the page.
* **github** (*optional*): GitHub link shown at the bottom of the page.
* **email** (*optional*): Email link shown at the bottom of the page.

## Run the project locally

This is a simple Flask project. First, install the dependencies:

```
pip install -r requirements.txt
```

And there you go:

```
export FLASK_APP=app.py && flask run
```