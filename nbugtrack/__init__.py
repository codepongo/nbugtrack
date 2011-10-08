# main program

import sys
import os
import router
import urllib
import view

from wsgiref.simple_server import make_server
from wsgiref.util import *

def nbugtrack(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    
    start_response(status, headers)
    
    if environ["QUERY_STRING"] != '':
        query = urllib.unquote(environ["PATH_INFO"])+"?"+urllib.unquote(environ["QUERY_STRING"])
    else:
        query = urllib.unquote(environ["PATH_INFO"])

    response = router.match(query)

    return showView(response) # does a type dispatch and prints the content

if __name__ == '__main__':
    port_to_run = 8765

    try:
        if len(sys.argv) == 2:
            port_to_run = argv[1]
        httpd = make_server('', port_to_run, nbugtrack)
        httpd.serve_forever()
    except KeyboardInterrupt:
        exit()
