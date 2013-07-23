__author__ = "Vimal Atreya Ramaka"
__copyright__ = "Copyright (C) 2013 Vimal Atreya Ramaka"
__license__ = "GPLv2"
__version__ = "0.2"

from google.appengine.ext import ndb

class AuthRecord(ndb.Model):
	uid = ndb.IntegerProperty()
	t_key = ndb.StringProperty()
	t_secret = ndb.StringProperty()
	used = ndb.BooleanProperty(default=False)
	authenticatedOn = ndb.DateTimeProperty(auto_now_add=True)

class Account(ndb.Model):
	uid = ndb.IntegerProperty()
	name = ndb.StringProperty()
	country = ndb.StringProperty()
	link = ndb.StringProperty()
	quota_normal = ndb.FloatProperty()
	quota_shared = ndb.FloatProperty()
	quota_quota	= ndb.FloatProperty()
	createdOn = ndb.DateTimeProperty(auto_now_add=True)

class AccessTokens(ndb.Model):
	uid = ndb.IntegerProperty()
	t_key = ndb.StringProperty()
	t_secret = ndb.StringProperty()
	revoked = ndb.BooleanProperty(default=False)
	gainedOn = ndb.DateTimeProperty(auto_now_add=True)