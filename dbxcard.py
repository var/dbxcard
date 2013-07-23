__author__ = "Vimal Atreya Ramaka"
__copyright__ = "Copyright (C) 2013 Vimal Atreya Ramaka"
__license__ = "GPLv2"
__version__ = "0.2"

import sys
import os
from dropbox import session, client
from dataaccess import *

APP_KEY = 'YOUR_APP_KEY'
APP_SECRET = 'YOUR_APP_SECRET'
ACCESS_TYPE = 'app_folder' # should be 'dropbox' or 'app_folder' as configured for your app
FILES_DIR = 'dbxfiles'

def get_session():
    return session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

def get_client(access_token):
    sess = get_session()
    sess.set_token(access_token.key, access_token.secret)
    return client.DropboxClient(sess)

def getCallbackURL(host):
	request_token = getRequestToken()
	setNewAuthRecord(000000, request_token.key, request_token.secret)
	callbackURL = buildCallbackURL(host, request_token)
	return callbackURL

def getRequestToken():
	sess = get_session()
	return sess.obtain_request_token()

def getAccessToken(rtoken):
	return sess.obtain_access_token(rtoken)

def getAccountInfo(access_token):
	db = get_client(access_token)
	info = db.account_info()
	return info

def setAccount(access_token):
	info = getAccountInfo(access_token)
	setAccountInfo(info)

def buildCallbackURL(host, request_token):
	sess = get_session()
	callback = 'http://' + host + '/callback' 
	return sess.build_authorize_url(request_token, oauth_callback=callback)

def addFiles(access_token):
	path = os.path.join(os.path.dirname(__file__), FILES_DIR)
	db = get_client(access_token)
	d = {}
	for x in os.listdir(path):
		f = open(FILES_DIR + '/' + x)
		result = db.put_file('/'+x, f)
		d[x] = result
		f.close()
	return d