import time
import random

from eventlet.green import urllib2
from cookies import CookieHandler

from crawley.config import REQUEST_TIMEOUT, MOZILLA_USER_AGENT


class Request(object):
    """
        Custom request object 
    """    
    
    def __init__(self, url, cookie_handler=None):
        
        if cookie_handler is None:
           cookie_handler = CookieHandler() 
        
        self.url = url
        self.headers = {}
        self.headers["User-Agent"] = MOZILLA_USER_AGENT
        self.headers["Accept-Charset"] = "ISO-8859-1,utf-8;q=0.7,*;q=0.3"
        self.headers["Accept-Language"] = "es-419,es;q=0.8"
        
        self.cookie_handler = cookie_handler
    
    def get_response(self, data=None):
        """
            Returns the response object from a request.
            Cookies are supported via a CookieHandler object
        """
        
        self._normalize_url()
        
        request = urllib2.Request(self.url, data, self.headers)        
        opener = urllib2.build_opener(self.cookie_handler)
        
        if REQUEST_TIMEOUT is not None:
            response = opener.open(request, timeout=REQUEST_TIMEOUT)
        else:
            response = opener.open(request)
            
        self.cookie_handler.save_cookies()
        
        return response
        
    def _normalize_url(self):
        """
            Normalize the request url
        """
                
        self.url = urllib2.quote(self.url.encode('utf-8'), safe="%/:=&?~#+!$,;'@()*[]")


class DelayedRequest(Request):
    """
        A delayed custom Request 
    """
    
    def __init__(self, url, cookie_handler=None, delay=0, deviation=0):
        
        self.delay = delay + random.randint(-deviation, deviation)
        Request.__init__(self, url, cookie_handler)
    
    def get_response(self, data=None):
        """
            Waits [delay] miliseconds and then make the request
        """
        
        mili_seconds = self.delay / 1000
        time.sleep(mili_seconds)
        
        return Request.get_response(self, data)
