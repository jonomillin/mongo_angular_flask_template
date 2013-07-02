from flask import Blueprint, render_template, abort, redirect, Response
from jinja2 import TemplateNotFound
import time
from flask import Flask, request, json, render_template, redirect, session
from mongokit import *
import logging
import datetime
from models.models import connection
import re

def build_template(template, **kwargs):
	is_logged_in = logged_in()
	print "Rendering: ", template, " and ", is_logged_in
	inner_template = render_template(template, is_logged_in=is_logged_in, **kwargs)
	#print inner_template
	return render_template('scaffold.html', inner_template=inner_template, is_logged_in=is_logged_in, email=get_email(), **kwargs)

def get_email():
	try:
		return session['email']
	except:
		return "Not logged in"

def logged_in():
	logged = session.get('email', None ) != None
	print "Logged in: ", logged
	return logged


def valid_email(email):
	if len(email) > 7:
		if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
			return True
	return False