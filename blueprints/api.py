from flask import Blueprint, render_template, abort, redirect, Response, jsonify, send_from_directory
from jinja2 import TemplateNotFound
from flask import Flask, request, json, render_template, redirect, session, url_for
from mongokit import *
from bson import ObjectId
from models.models import connection
from lib.tools import *
import logging, datetime, time
import json, os
from decorators.decorators import *

api_pages = Blueprint('api_pages', __name__, template_folder='templates')

@api_pages.route('/api/v1/someitem', methods=['GET', 'POST'])
@api_pages.route('/api/v1/someitem/<_id>', methods=['PUT', 'DELETE', 'GET'])
#@require_authorization
def rest_api_someitem(_id=None):

	email = "example@example.com"

	# Restful http post
	if request.method == 'POST':
		dic = json.loads(request.data)
		someitem = connection.SomeItem()
		someitem.update_from_dict(dic, email=email)
		return someitem.commit_model()

	# Restful http put
	if request.method == 'PUT':
		dic = json.loads(request.data)
		someitem = connection.SomeItem.one({'_id' : ObjectId(_id)})
		someitem.update_from_dict(dic, exclude=['date_creation', 'email'])
		return someitem.commit_model()

	# Restful http get
	if request.method == 'GET':
		return connection.SomeItem.as_json(_id, email)
			
	# Restful http delete
	#if request.method == 'DELETE':
	#	return connection.SomeItem.delete(_id)
