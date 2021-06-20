# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf          import FlaskForm
from flask_wtf.file     import FileField, FileRequired
from wtforms            import StringField, TextAreaField, SubmitField, PasswordField, SelectField
from wtforms.validators import InputRequired, Email, DataRequired

class LoginForm(FlaskForm):
	username    = StringField  (u'Username'  , validators=[DataRequired()])
	password    = PasswordField(u'Password'  , validators=[DataRequired()])

class RegisterForm(FlaskForm):
	name        = StringField  (u'Name'      )
	username    = StringField  (u'Username'  , validators=[DataRequired()])
	password    = PasswordField(u'Password'  , validators=[DataRequired()])
	email       = StringField  (u'Email'     , validators=[DataRequired(), Email()])


# rgb colors to be converted to bgr for opencv
colors = [('ff5656', 'light red'),
		  ('ffaa56', 'light orange'),
		  ('ffff56', 'light yellow'),
		  ('56ff56', 'light green'),
		  ('56ffff', 'light cyan'),
		  ('5656ff', 'light blue'),
		  ('aa56ff', 'light purple'),
		  ('ff56ff', 'light pink'),

		  ('ff0000', 'red'),
		  ('ff7f00', 'orange'),
		  ('ffff00', 'yellow'),
		  ('00ff00', 'green'),
		  ('00ffff', 'cyan'),
		  ('0000ff', 'blue'),
		  ('7f00ff', 'purple'),
		  ('ff00ff', 'pink'),

		  ('bf0000', 'dark red'),
		  ('bf5f00', 'dark orange'),
		  ('ffff56', 'dark yellow'),
		  ('00bf00', 'dark green'),
		  ('00bfbf', 'dark cyan'),
		  ('0000bf', 'dark blue'),
		  ('5f00bf', 'dark purple'),
		  ('bf00bf', 'dark pink'),

		  ('ffffff', 'white'),
		  ('000000', 'black')]


class ShadesImageForm(FlaskForm):
	image = FileField(u'Image File')
	color1 = SelectField(u'Color 1', choices=colors)
	color2 = SelectField(u'Color 2', choices=colors)
	color3 = SelectField(u'Color 3', choices=colors)
	color4 = SelectField(u'Color 4', choices=colors)
	color5 = SelectField(u'Color 5', choices=colors)
	color6 = SelectField(u'Color 6', choices=colors)
	color7 = SelectField(u'Color 7', choices=colors)

