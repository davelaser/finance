import logging
import time

from controllers import urls
from controllers import utils


class RequestAll(utils.BaseHandler):

    def get(self, path):
        self.redirect(urls.requestDefault)


class DefaultHandler(utils.BaseHandler):

    def get(self):

        # You can remove this set_request_arguments() method call now, as the BaseHandler.__init__() 
        # calls this for you on every request...
        self.set_request_arguments()

        try:
            args = dict(view_count=True, limit=None)
            self.context['now_time'] = int(time.time())
            template = 'index'
        except Exception, e:
            logging.exception(e)
            raise e
        finally:
            self.render(template)

    def post(self):
        self.redirect(urls.requestDefault)


class RequestLogin(utils.BaseHandler):

    def get(self):
        self.FacebookLogin()


class RequestLogout(utils.BaseHandler):

    def get(self):
        self.FacebookLogout()
