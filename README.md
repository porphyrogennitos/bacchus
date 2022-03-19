# Bacchus

#### [YouTube Video](https://youtu.be/PXDWDRF6Kq0)

Was another name for Dionysus; the Ancient Greek god of wine and festivity. 

This web application lets you add and delete the festivals you've visited in Greece.

## What technologies were used?

Is made in VSCode and written in HTML, CSS, JavaScript, Python (Flask library used) and SQL.

## Installation

I have included a `requirements.txt` so the only thing you have to do is: `pip install -r /path/to/requirements.txt` ([Stack Overflow](https://stackoverflow.com/questions/7225900/how-can-i-install-packages-using-pip-according-to-the-requirements-txt-file-from))

## How to use?

Firstly, you have to register, and to do that, you press the "Εγγραφή" (Eggrafi) button in the homepage. You need to type a correct email and a password (it can have whatever letter and length you want) and then you press again "Εγγραφή". 

TaDa! You know have an account in this magnificent website! Now you'll have to login and to do that, you press "Σύνδεση" (Syndesi) button; type your email and password and "you're in"! 

You'll be redirected to a "complicated" page but don't be daunted! There are two buttons; one with "Πρόσθεσε" (Prosthese, meaning "Add") and the other with "Αφαίρεσε" (Aferese, meaning "delete").

Say you want to add a festival; you press the "Πρόσθεσε" and you have to add the name, the location and/or the date you went. 

If you want to delete a festival, press "Αφαίρεσε" and type exactly the name of the festival you want to be deleted!

Finally, there's a link on left where you can log out. 

## What and how?

I used the MVC paradigm because of the Flask framework.

Firstly I organized my code:
```
scss/
static/
templates/
app.py
bacchus.db
gulpfile.js
helpers.py
README.md
requirements.txt
```

## SCSS

I used Bootstrap 5 and at some point I wanted to edit the primary color. To do that, I had to use scss, so I created the folder where I import the customized Bootstrap in a `custom.scss`.

## static/

Here I have my favicon, CSS and JavaScript.

### JavaScript

Here I've configured the Bootstrap's client-side form validation.

## templates/

### base.html

This is the basic layout; where all the other HTML elements are being imported.

### failure.html

A page with the error message and number.

### header.html

A jumbotron with the header, the login and register buttons.

### index.html

The table that will be display when a user is logged in.

## app.py

Here is all the functionality of the web app.

### index()

* [GET] Shows the festivals table

### add()

* [POST] Adds festivals to the database

### delete()

* [POST] Deletes festivals from database

### header()

* [GET] renders the `header.html`

## gulpfile.js

[Automates SASS compilation](https://code.visualstudio.com/docs/languages/css#_automating-sassless-compilation).

## helpers.py

Contains useful functions like `login_required` which makes some routes accessible only if the user has logged in.

## requirements.txt

All the libraries and frameworks that were used in my virtual environment.

## Things to improve

* Make it in English
* Show a front-end error message in register or login explaining what went wrong
<<<<<<< HEAD
* More functionality like edit the festival you've been or sort the festivals by name, etc.
=======
* More functionality like edit the festival you've been or sort the festivals by name, etc.
>>>>>>> cfd595f (Update README.Md)
