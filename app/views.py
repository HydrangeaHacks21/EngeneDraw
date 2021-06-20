# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Python modules
import os, logging 
import cv2
import numpy


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

        return render_template("startPage.html")

    return render_template('uploadImage.html')

@app.route('/uploadImageColor.html', methods=["POST", "GET"])
def uploadImageColor():
    if request.method == "POST":
        img = request.files["formFile"]
        colour1 = request.form["colour1"]

        img.save(os.path.join(app.config["IMAGE_UPLOADS"], img.filename))

        print(img)

        image2 = cv2.imread('app/static/uploaded/hydrangeaImage.jpg')

        gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

        cv2.imshow('All Contours', gray)

        cv2.waitKey(0)

        return render_template("colorChange.html")

    return render_template('uploadImageColor.html')
