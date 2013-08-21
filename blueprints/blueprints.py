'''
This is a directory that holds all the routes.
'''

from flask import Blueprint, render_template, abort, redirect, Response, jsonify, send_from_directory, make_response
from jinja2 import TemplateNotFound
from flask import Flask, request, json, render_template, redirect, session, url_for
from mongokit import *
from bson import ObjectId
from models.models import connection
from lib.tools import *
from decorators.decorators import *
import logging, datetime, time, json, os

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/')	
@page.route('/index')
def index():
	return build_template('someitem.html')

@page.route('/map')
def map():
	return build_template('map.html')
