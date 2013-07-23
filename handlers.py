__author__ = "Vimal Atreya Ramaka"
__copyright__ = "Copyright (C) 2013 Vimal Atreya Ramaka"
__license__ = "GPLv2"
__version__ = "0.2"

import webapp2
import datetime
import logging
from webapp2_extras import jinja2
from dropbox import session, client
from dbxcard import *

class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **context):
        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)


class HomeHandler(BaseHandler):
	""" Just handles the home page """
	def get(self):
		self.render_response('home.html')


class VerifyHandler(BaseHandler):
	""" Verifies if there is a cookie with uid, else, 
	redirects to dropbox for authentication. """
	def get(self):
		cookie_value = self.request.cookies.get('auth_uid')
		if cookie_value:
			self.render_response('verify.html', name = getUserName(cookie_value))
		else:
			self.redirect('/go/dbx', True)


class SuccessHandler(BaseHandler):
	""" Handles the success message """
	def get(self):
		self.render_response('success.html')


class ErrorPageHandler(BaseHandler):
	""" Shows an error message when redirected to /error """
	def get(self):
		self.render_response('error.html')


class GoToDBXHandler(webapp2.RedirectHandler):
	""" Builds a callback URL and redirects to dropbox for authorization. """
	def get(self):
		self.redirect(getCallbackURL(self.request.host), True)


class AddFilesHandler(webapp2.RedirectHandler):
	""" Checks for auth_uid cookie for uid and adds files to 
	the user's Dropbox"""
	def get(self):

		uid = self.request.cookies.get('auth_uid')
		if uid:
			access_token = getTokenByUser(int(uid))
			# print request_token
			if access_token:
				r = addFiles(access_token)
				self.redirect('/success', True)
			else:
				self.redirect('/error', True)
		else:
			self.redirect('/', True)


class CallbackHandler(BaseHandler):
	""" handles callback from dropbox. if not approved, displays a message
	else check for oauth_token and uid form the URL,
	if an oauth_token exists, obtains a access_token token, sets a cookie and adds files"""
	def get(self):
		not_approved = self.request.get('not_approved')

		if not_approved == 'true':
			self.render_response('not_approved.html')
		else:

			oauth_token = self.request.get('oauth_token')
			uid = self.request.get('uid')

			setuid(oauth_token, uid)

			if oauth_token:

				sess = get_session()
	        	request_token = getTokenObj(oauth_token)
	        	access_token = sess.obtain_access_token(request_token)

	        	markAuthUsed(oauth_token)
	        	setAccessTokens(int(uid), access_token.key, access_token.secret)

	        	setAccount(access_token)

	        	self.response.set_cookie('auth_uid', uid, expires=datetime.datetime.now() + datetime.timedelta(days=365), path='/',
        		domain=self.request.host)

	        	if access_token:
	        		r = addFiles(access_token)
	        		self.redirect('/success', True)
	        	else:
	        		self.redirect('/error', True)


def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Oops! I could swear this page was here!')
    response.set_status(404)

def handle_500(request, response, exception):
    logging.exception(exception)
    response.write('Hey - looks like there is a problem. Can you please start over?')
    response.set_status(500)