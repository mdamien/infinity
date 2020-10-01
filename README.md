infinity
========

Infinite depth website made with Flask
Building Your First Website with Flask: Part 4
Creating forms and databases with Flask
Inserting Data From a Form
With Flask, form data can be sent to a template. The form data received will trigger a function that forwards the collected data to a template for rendering on selected web pages.
In the example below, we will use the home page, which can be found at the ‘/’ URL. This renders a web page (user.html) with a form. The data filled in by a user is posted to the ‘/result’ URL. The results() function triggers the output on the resulting URL. The function also collects form data present in request.form using a dictionary style (dictionary object) and sends it to result.html for rendering.
The template renders the form data dynamically into an HTML table. Below is the code for FormTable.py.

Given below is the HTML script of users.html.

Once you submit the form, it will call the result HTML page. The code of the template (result.html) is given below:

Run the Python script, and enter the URL http://localhost:5000/ in the browser.
The output of going to the form will look like this (minus what we typed in):
Image for post
When the submit button is clicked, form data is rendered on result.html in the form of an HTML table.
Image for post
Incorporating a Database
If you recall, in our comparison of Flask vs. Django, Flask is a micro-web framework in Python. This definition implies it does not feature an object-relational mapper (ORM) (whereas Django does).
So if you wish to incorporate an interactive database, then you require the additional installation of an extension. SQLAlchemy has become a popular choice to install. In Flask, the ready-made extension for the addition SQLAlchemy is called Flask-SQLAlchemy.
Installing Flask-SQLAlchem
The installation of Flask-SQLAlchemy requires the use of pip in your active virtual environment created for Flask. To install the extension, enter the following into your active environment for Flask in Python:
pip install flask-sqlalchemy
After the successful installation of Flask-SQLAlchemy, the next installation needed is MySQL. This installation can be achieved using:
pip install mysql
After the successful installation of Flask-SQLAlchemy alongside other dependencies, it is time to create our interactive database.

To know why this app is popular: https://archive.is/yHnUW
