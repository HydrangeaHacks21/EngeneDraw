# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Python modules
import os, logging 
import cv2
import numpy as np
from random import randint


# Flask modules
from flask import render_template, request, url_for, redirect, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort
from jinja2 import TemplateNotFound

# App modules
from app import app, lm, db, bc
from app.models import User
from app.forms import LoginForm, RegisterForm


# provide login manager with load_user callback
@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Logout user
@app.route('/logout.html')
def logout():
    logout_user()
    return redirect(url_for('index'))


# Register a new user
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    # declare the Registration Form
    form = RegisterForm(request.form)

    msg = None
    success = False

    if request.method == 'GET':
        return render_template('accounts/register.html', form=form, msg=msg)

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)
        email = request.form.get('email', '', type=str)

        # filter User out of database through username
        user = User.query.filter_by(user=username).first()

        # filter User out of database through username
        user_by_email = User.query.filter_by(email=email).first()

        if user or user_by_email:
            msg = 'Error: User exists!'

        else:

            pw_hash = bc.generate_password_hash(password)

            user = User(username, email, pw_hash)

            user.save()

            msg = 'User created, please <a href="' + url_for('login') + '">login</a>'
            success = True

    else:
        msg = 'Input error'

    return render_template('accounts/register.html', form=form, msg=msg, success=success)


# Authenticate user
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    # Declare the login form
    form = LoginForm(request.form)

    # Flask message injected into the page, in case of any errors
    msg = None

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)

        # filter User out of database through username
        user = User.query.filter_by(user=username).first()

        if user:

            if bc.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                msg = "Wrong password. Please try again."
        else:
            msg = "Unknown user"

    return render_template('accounts/login.html', form=form, msg=msg)

# App main route + generic routing
@app.route('/', defaults={'path': 'startPage.html'})
@app.route('/<path>')
def index(path):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    try:

        if not path.endswith('.html'):
            path += '.html'

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template(path)

    except TemplateNotFound:
        return render_template('page-404.html'), 404

    except:
        return render_template('page-500.html'), 500


# Return sitemap
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')

path =(os.path.abspath(__file__))
path = os.path.dirname(path)

app.config["IMAGE_UPLOADS"] = "{}/static/uploads".format(path)
print(app.config["IMAGE_UPLOADS"])

@app.route('/uploadImage.html', methods=["POST", "GET"])
def upload():
    if request.method == "POST":

        img = request.files["formFile"]
        grid = request.form["grid"]
        colour = request.form["colour"]

        img.save(os.path.join(app.config["IMAGE_UPLOADS"], img.filename))

        print(app.config["IMAGE_UPLOADS"])
        print(grid, colour)
        print(type(img))

        return render_template("lineArtOutput.html")

    return render_template('uploadImage.html')

# function to break grayscale image down by value
def simplify(x):
    if x <= 15:
        return 0
    elif 15 < x <= 51:
        return 15
    elif 51 < x <= 102:
        return 51
    elif 102 < x <= 153:
        return 102
    elif 153 < x <= 204:
        return 153
    elif 204 < x <= 51:
        return 204
    else:
        return 255

simplify_vectorized = np.vectorize(simplify)


def swapPositions(list):
    list[1], list[3] = list[3], list[1]
    return list

@app.route('/uploadImageColor.html', methods=["POST", "GET"])
def uploadImageColor():
    if request.method == "POST":
        img = request.files["formFile"]
        colour1 = request.form["colour1"]
        colour2 = request.form["colour2"]
        colour3 = request.form["colour3"]
        colour4 = request.form["colour4"]
        colour5 = request.form["colour5"]
        colour6 = request.form["colour6"]
        colour7 = request.form["colour7"]
        randomize = request.form.get("randomize")

        # set new colors
        if randomize:
            # pick random colors
            print("random colors")
            bgr1 = [randint(0, 255), randint(0, 255), randint(0, 255)]
            bgr2 = [randint(0, 255), randint(0, 255), randint(0, 255)]
            bgr3 = [randint(0, 255), randint(0, 255), randint(0, 255)]
            bgr4 = [randint(0, 255), randint(0, 255), randint(0, 255)]
            bgr5 = [randint(0, 255), randint(0, 255), randint(0, 255)]
            bgr6 = [randint(0, 255), randint(0, 255), randint(0, 255)]
            bgr7 = [randint(0, 255), randint(0, 255), randint(0, 255)]

        else:
            # convert from hex codes to 3 channels, rgb
            bgr1 = list(int(colour1[i:i+2], 16) for i in (0, 2, 4))
            bgr2 = list(int(colour2[i:i+2], 16) for i in (0, 2, 4))
            bgr3 = list(int(colour3[i:i+2], 16) for i in (0, 2, 4))
            bgr4 = list(int(colour4[i:i+2], 16) for i in (0, 2, 4))
            bgr5 = list(int(colour5[i:i+2], 16) for i in (0, 2, 4))
            bgr6 = list(int(colour6[i:i+2], 16) for i in (0, 2, 4))
            bgr7 = list(int(colour7[i:i+2], 16) for i in (0, 2, 4))

            print("brg1: ", bgr1)

            # rearrange accordingly
            bgr1 = swapPositions(bgr1)
            bgr2 = swapPositions(bgr2)
            bgr3 = swapPositions(bgr3)
            bgr4 = swapPositions(bgr4)
            bgr5 = swapPositions(bgr5)
            bgr6 = swapPositions(bgr6)
            bgr7 = swapPositions(bgr7)

        # save object as image
        img.save(os.path.join(app.config["IMAGE_UPLOADS"], img.filename))

        # get image from file
        image2 = cv2.imread(os.path.join(app.config["IMAGE_UPLOADS"], img.filename))

        # convert to grayscale (single channel)
        gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

        # simplify
        mapped_array = simplify_vectorized(gray)

        # format back to 3 channel
        mapped_array = mapped_array.astype(np.uint8)
        backtorgb = cv2.cvtColor(mapped_array, cv2.COLOR_GRAY2RGB)

        # recolor

        cv2.imshow('All Contours', gray)

        cv2.waitKey(0)

        return render_template("colorChangeOutput.html")

    return render_template('uploadImageColor.html')
