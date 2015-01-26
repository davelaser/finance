#!/usr/bin/env python
import webapp2

from controllers import default
from controllers import urls
from properties import properties

app = webapp2.WSGIApplication([
    (urls.requestDefault, default.DefaultHandler),
    (urls.requestLogin, default.RequestLogin),
    (urls.requestAll, default.RequestAll)
    ],
    config=properties.GAE_SESSION_CONFIG,
    debug=True)