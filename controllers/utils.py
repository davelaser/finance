import json
import webapp2
import logging
import urllib
import urllib2
import urlparse
import jinja2
import os


from properties import properties
from models import user

from webapp2_extras import sessions

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) +
                                   '/../templates'))


class BaseHandler(webapp2.RequestHandler):
    """
        If you're sub-classing webapp2.RequestHandler you need to implement this __ini__() method, below.
    """
    def __init__(self, request=None, response=None):
        # Initialize the Request and Response objects
        self.initialize(request, response)
        
        # And create your hash context for use with Request arguments or data for the Jinja template
        self.context = {}

        # Now do your own stuff, like set request arguments into a handy dictionary (hash)
        self.set_request_arguments()

    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

    def render(self, template_name):
        template = jinja_environment.get_template(template_name + '.html')
        self.response.out.write(template.render(self.context))
        return

    def set_request_arguments(self):
        try:
            request_args = dict()
            for arg in self.request.arguments():
                request_args[arg] = self.request.get(arg)
            self.context['request_args'] = request_args
            return
        except UnicodeDecodeError, unicode_error:
            self.context['request_args'] = dict()
            logging.exception(unicode_error)
        except Exception, e:
            self.context['request_args'] = dict()
            logging.exception(e)
            raise e

    def FacebookLogin(self):
        verification_code = self.request.get('code')
        args = dict(
            client_id=properties.FACEBOOK_APP_ID,
            redirect_uri=self.request.path_url)
        if verification_code:

            args["client_secret"] = properties.FACEBOOK_APP_SECRET
            args["code"] = verification_code

            headers = {'User-Agent': 'Mozilla/5.0'}
            req = urllib2.Request(
                properties.FACEBOOK_URL + properties.FACEBOOK_OAUTH_URL,
                urllib.urlencode(args), headers)
            response = urllib2.urlopen(req)
            tokens = urlparse.parse_qs(response.read())

            # stores session
            self.session[
                'facebook-token'] = self.context[
                'token'] = tokens['access_token'][0]

            # saves FB profile
            self.context['profile'] = json.load(urllib.urlopen(
                properties.FACEBOOK_URL + "/me?" + urllib.urlencode(
                    dict(access_token=self.context['token']))))

            # adds user
            current = user.User(key_name=str(self.context['profile']["id"]),
                                id=str(self.context['profile']["id"]),
                                name=self.context['profile']["name"],
                                access_token=self.context['token'],
                                profile_url=self.context['profile']["link"])
            current.put()
            self.redirect('/')
        else:
            self.redirect(
                properties.FACEBOOK_URL + properties.FACEBOOK_OAUTH_AUTHORISE +
                urllib.urlencode(args))

    def FacebookLogout(self):
        return
