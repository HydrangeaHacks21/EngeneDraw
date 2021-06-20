# EngeneDraw

Welcome to EngeneDraw, the AI assisted art teacher that can simplify complex reference images and make it easier to learn how to draw!

## Image transformations

### Extracting simple lineart


![extracting simple lineart](https://github.com/HydrangeaHacks21/EngeneDraw/blob/master/readmeImages/extracting%20simple%20lineart.gif?raw=true)



![Stepwise progression gif](https://github.com/HydrangeaHacks21/EngeneDraw/blob/master/readmeImages/Stepwise%20progression%20gif.gif?raw=true)



![generate grid to improve proportions](https://github.com/HydrangeaHacks21/EngeneDraw/blob/master/readmeImages/generate%20grid%20to%20improve%20proportions.gif?raw=true)



![simplify and recolor](https://github.com/HydrangeaHacks21/EngeneDraw/blob/master/readmeImages/simplify%20and%20recolor.gif?raw=true)



![simplify complex images](https://github.com/HydrangeaHacks21/EngeneDraw/blob/master/readmeImages/simplify%20complex%20images.gif?raw=true)

## Python Scripts (in EngeneDraw_Scripts folder)

## List of key files and descriptions
please excuse that it was poorly named

#### here.py

* Converts an image into grayscale
* Extracts contours
* Adds the contours piecewise onto a set of images
* Produces a final image with all the lineart of an image extracted

#### gridWithCoords.py

* Adds a grid with an adjustable number of columns to help divide an image and make it easier to draw

#### shading.py

* Converts an image into grayscale 
* Simplifies it to a handfull of values

#### colorDump.py

* Adds colors selected by a user to a simplified image to create an art with an abstract effect

## List of folders with sample outputs 

## Website

To test out our website, follow the steps below (instructions adapted from https://github.com/app-generator/flask-pixel-lite):
```bash
$ # Clone the sources
$ git clone https://github.com/HydrangeaHacks21/EngeneDraw.git
$ cd EngeneDraw
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install requirements
$ pip3 install -r requirements.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Run the application
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the app in browser: http://127.0.0.1:5000/
```

## Website demo

