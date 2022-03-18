# What and how?

I used the MVC paradigm because of the Flask framework.

Firstly I organized my code:
```
scss/ 
static/ 
templates/ 
app.py 
bacchus.db
DESIGN.md
gulpfile.js
helpers.py
README.md
requirements.txt 
```

## SCSS

I used Bootstrap and at some point I wanted to edit the primary color. To do that, I had to use scss, so I created the folder where I import the customized Bootstrap in a `custom.scss`. 

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


