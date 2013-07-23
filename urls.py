__author__ = "Vimal Atreya Ramaka"
__copyright__ = "Copyright (C) 2013 Vimal Atreya Ramaka"
__license__ = "GPLv2"
__version__ = "0.2"

import webapp2

from handlers import *

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/go', VerifyHandler),
    ('/callback', CallbackHandler),
    ('/success', SuccessHandler),
    ('/go/dbx', GoToDBXHandler),
    ('/add-files', AddFilesHandler),
    ('/error', ErrorPageHandler)
], debug=False)

app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500