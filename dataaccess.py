__author__ = "Vimal Atreya Ramaka"
__copyright__ = "Copyright (C) 2013 Vimal Atreya Ramaka"
__license__ = "GPLv2"
__version__ = "0.2"

from models import Account, AuthRecord, AccessTokens

class DictObj(object):
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

def getUserName(uid):
	e = Account.get_by_id(int(uid))
	if e:
		return e.name
	else:
		pass

def setNewAuthRecord(uid, t_key, t_secret):
	ar = AuthRecord(id = t_key, uid = uid, t_key = t_key, t_secret = t_secret, used = False)
	ar.put()

def setAccessTokens(uid, t_key, t_secret):
	a = AccessTokens(id = uid, uid = uid, t_key = t_key, t_secret = t_secret, revoked = False)
	a.put()

def setAccountInfo(info):
	e = Account.get_by_id(info['uid'])
	if e:
		pass
	else:
		account = Account(id = info['uid'], uid = info['uid'], name = info['display_name'], country = info['country'], link = info['referral_link'], 
		quota_normal = info['quota_info']['normal'], quota_shared = info['quota_info']['shared'], quota_quota = info['quota_info']['quota'])
		account.put()

def setuid(tokenk, uid):
	e = AuthRecord.get_by_id(tokenk)
	e.uid = int(str(uid))
	e.put()

def markAuthUsed(tokenk):
	e = AuthRecord.get_by_id(tokenk)
	e.used = True
	e.put()

def getTokenByUser(uid):
	e = AccessTokens.get_by_id(uid)
	t = {}
	t['key'] = e.t_key
	t['secret'] = e.t_secret
	return DictObj(t)

def getTokenObj(tokenk):
	e = AuthRecord.get_by_id(tokenk)
	t = {}
	t['key'] = e.t_key
	t['secret'] = e.t_secret
	return DictObj(t)